"""Render the downloads and images the site links to, in the shared
Skan.ai palette, from the canonical sources.

    pip install playwright markdown pillow && python -m playwright install chromium
    python tools/make_assets.py [--chromium /path/to/chrome]

Writes:
    docs/downloads/soa-agentic-terms.pdf                          terms sheet, from mapping-table.json
    docs/downloads/skan-agentic-ai-terminology-whitepaper.pdf     from whitepaper.md
    docs/assets/social-preview.png                                link preview, 1280x640
    docs/favicon.png, docs/favicon.ico, docs/apple-touch-icon.png

For the PDFs to use the site's typefaces, install Inter, Inter Tight, and
JetBrains Mono locally first; otherwise the browser's fallback fonts are used.
"""

from __future__ import annotations

import argparse
import html
import io
import json
import re
from pathlib import Path

import markdown
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
e = html.escape

BASE_CSS = """
@page { size: Letter; margin: 0.75in 0.8in 0.85in; }
:root { --grape:#9677ff; --amethyst:#4e287a; --night:#161714; --muted:#5e5f58; --rule:#d8dad1; }
body { font-family: "Inter", Arial, sans-serif; color: var(--night); font-size: 10.5pt; line-height: 1.55; margin: 0; }
h1, h2, h3 { font-family: "Inter Tight", Arial, sans-serif; letter-spacing: -0.01em; }
a { color: var(--amethyst); text-decoration: none; }
.eyebrow { font-family: "Inter Tight", Arial, sans-serif; text-transform: uppercase; letter-spacing: .12em; font-size: 8.5pt; font-weight: 600; color: var(--amethyst); margin: 0 0 6pt; }
.eyebrow b { color: var(--grape); }
"""

SHEET_CSS = BASE_CSS + """
h1 { font-size: 22pt; margin: 0 0 4pt; }
.intro { color: var(--muted); font-size: 9.5pt; margin: 0 0 14pt; max-width: 6in; }
.head, .row { display: grid; grid-template-columns: 1fr 1fr; column-gap: 22pt; }
.head { border-bottom: 2px solid var(--grape); padding-bottom: 4pt; }
.head p { margin: 0; font-family: "Inter Tight", Arial, sans-serif; font-size: 8pt; font-weight: 600; letter-spacing: .12em; text-transform: uppercase; color: var(--muted); }
.head p + p { color: var(--amethyst); }
.row { border-bottom: 1px solid var(--rule); padding: 7pt 0; break-inside: avoid; }
.term { font-family: "Inter Tight", Arial, sans-serif; font-weight: 600; font-size: 10.5pt; margin: 0 0 2pt; }
.row div + div .term { color: var(--amethyst); }
.desc { font-size: 8.8pt; color: #383a35; margin: 0; line-height: 1.45; }
"""

PAPER_CSS = BASE_CSS + """
.cover { height: 9in; display: flex; flex-direction: column; justify-content: center; break-after: page; }
.cover .bar { width: 48pt; height: 4pt; background: var(--grape); margin: 0 0 18pt; border-radius: 2pt; }
.cover h1 { font-size: 34pt; margin: 0 0 10pt; font-weight: 600; }
.cover .sub { font-size: 15pt; color: var(--amethyst); margin: 0 0 28pt; max-width: 4.8in; font-family: "Inter Tight", Arial, sans-serif; }
.cover .meta { font-size: 9pt; color: var(--muted); border-top: 1px solid var(--rule); padding-top: 10pt; max-width: 4.8in; }
.cover .meta p { margin: 2pt 0; }
h2 { font-size: 15pt; margin: 22pt 0 6pt; break-after: avoid; }
p, li { orphans: 3; widows: 3; }
table { border-collapse: collapse; width: 100%; font-size: 9pt; margin: 8pt 0 14pt; }
th, td { text-align: left; padding: 5pt 7pt; border-bottom: 1px solid var(--rule); vertical-align: top; }
th { font-family: "Inter Tight", Arial, sans-serif; color: var(--muted); border-bottom: 1.5px solid #c3c6bb; }
"""

ICON_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="{s}" height="{s}">
  <rect width="64" height="64" rx="14" fill="#161714"/>
  <path d="M14 22 H38 M26 42 H50" stroke="#c3c6bb" stroke-width="3.2" stroke-linecap="round"/>
  <path d="M34 16 L42 22 L34 28 M46 36 L54 42 L46 48" fill="none" stroke="#9677ff" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="14" cy="22" r="6" fill="#97c8ff"/>
  <circle cx="26" cy="42" r="6" fill="#97c8ff"/>
</svg>"""

PREVIEW_PAIRS = [("Service", "Agent"), ("Service Registry", "Agent Catalog"), ("SLA", "Agent QoS"),
                 ("Circuit Breaker", "Agent Fallback Protocol")]


def page_html(css: str, body: str) -> str:
    return f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>'


def terms_sheet(data: dict) -> str:
    rows = "".join(
        f'<div class="row"><div><p class="term">{e(m["soa_term"])}</p><p class="desc">{e(m["soa_description"])}</p></div>'
        f'<div><p class="term">{e(m["agentic_term"])}</p><p class="desc">{e(m["agentic_description"])}</p></div></div>'
        for m in data["mappings"])
    body = (f'<p class="eyebrow">Skan<b>.ai</b></p><h1>{e(data["title"])}</h1>'
            f'<p class="intro">{len(data["mappings"])} Service-Oriented Architecture concepts and their agentic equivalents. '
            f'Version {e(data["version"])}. Related concepts are grouped together, so you can read down either column. '
            f'CC-BY 4.0 · doi.org/10.5281/zenodo.21823088</p>'
            f'<div class="head"><p>SOA era</p><p>Agentic era</p></div>{rows}')
    return page_html(SHEET_CSS, body)


def whitepaper() -> str:
    text = (ROOT / "whitepaper.md").read_text(encoding="utf-8")
    lines = text.splitlines()
    title = lines[0].lstrip("# ").strip()
    subtitle = next(l for l in lines[1:] if l.startswith("## ")).lstrip("# ").strip()
    # Drop the title, subtitle, and the "published by / also as PDF" line; the cover replaces them.
    body_md = "## " + re.split(r"\n## ", text, maxsplit=2)[2]
    body_html = markdown.markdown(body_md, extensions=["tables", "sane_lists"])
    cover = (f'<div class="cover"><p class="eyebrow">Skan<b>.ai</b></p><div class="bar"></div>'
             f'<h1>{e(title)}</h1><p class="sub">{e(subtitle)}</p><div class="meta">'
             f'<p>Published by Skan, Inc. · skan.ai</p>'
             f'<p>Companion to the SOA-to-Agentic AI Terminology Mapping · github.com/Skandotai/soa-to-agentic-terms</p>'
             f'<p>Related: Agentic Ontology of Work · https://skandotai.github.io/agentic-ontology-of-work/</p>'
             f'<p>Licensed CC-BY 4.0. Attribution to Skan, Inc. required for reuse.</p></div></div>')
    return page_html(PAPER_CSS, cover + body_html)


PREVIEW_HTML = """<!DOCTYPE html><html><head><meta charset="utf-8"><style>
body {{ margin:0; width:1280px; height:640px; background:#161714; color:#f7fbf5; font-family:"Inter", Arial, sans-serif; overflow:hidden; }}
.wrap {{ padding:64px 80px; }}
.eyebrow {{ font-family:"Inter Tight", Arial, sans-serif; letter-spacing:.14em; text-transform:uppercase; font-size:20px; color:#9677ff; font-weight:600; margin:0 0 14px; }}
h1 {{ font-family:"Inter Tight", Arial, sans-serif; font-size:66px; line-height:1.05; margin:0 0 34px; font-weight:600; letter-spacing:-.02em; }}
.pair {{ display:grid; grid-template-columns: 1fr 70px 1fr; align-items:center; border-top:1px solid #34362f; padding:13px 0; font-family:"Inter Tight", Arial, sans-serif; font-size:30px; }}
.pair .s {{ text-align:right; color:#c3c6bb; }}
.pair .a {{ color:#b9a6ff; font-weight:600; }}
.pair .arrow {{ text-align:center; color:#9677ff; }}
.foot {{ position:absolute; left:80px; right:80px; bottom:36px; font-size:19px; color:#a9aba2; display:flex; justify-content:space-between; }}
.foot b {{ color:#9677ff; font-weight:600; }}
</style></head><body><div class="wrap">
<p class="eyebrow">A shared vocabulary for the agentic enterprise</p>
<h1>SOA-to-Agentic AI Terminology Mapping</h1>
{pairs}
</div>
<div class="foot"><span>Skan<b>.ai</b> · 28 term pairs · CC-BY 4.0</span><span>doi.org/10.5281/zenodo.21823088</span></div>
</body></html>"""


def render(chromium: str | None) -> None:
    data = json.loads((ROOT / "mapping-table.json").read_text(encoding="utf-8"))
    footer = ('<div style="font-size:8px;width:100%;padding:0 0.8in;color:#5e5f58;font-family:Arial;'
              'display:flex;justify-content:space-between"><span>{left}</span>'
              '<span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>')
    margin = {"top": "0.75in", "bottom": "0.85in", "left": "0.8in", "right": "0.8in"}
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=chromium) if chromium else p.chromium.launch()
        pg = browser.new_page()
        pg.set_content(terms_sheet(data))
        pg.wait_for_timeout(300)
        pg.pdf(path=str(DOCS / "downloads/soa-agentic-terms.pdf"), format="Letter", print_background=True,
               display_header_footer=True, header_template="<span></span>", margin=margin,
               footer_template=footer.format(left=f"SOA-to-Agentic AI Terminology Mapping {data['version']} · Skan, Inc. · CC-BY 4.0"))

        pg = browser.new_page()
        pg.set_content(whitepaper())
        pg.wait_for_timeout(300)
        pg.pdf(path=str(DOCS / "downloads/skan-agentic-ai-terminology-whitepaper.pdf"), format="Letter",
               print_background=True, display_header_footer=True, header_template="<span></span>", margin=margin,
               footer_template=footer.format(left="Agentic AI Terminology · Skan, Inc. · CC-BY 4.0"))

        pairs = "".join(f'<div class="pair"><span class="s">{e(s)}</span><span class="arrow">→</span><span class="a">{e(a)}</span></div>'
                        for s, a in PREVIEW_PAIRS)
        pg = browser.new_page(viewport={"width": 1280, "height": 640})
        pg.set_content(PREVIEW_HTML.format(pairs=pairs))
        pg.wait_for_timeout(300)
        pg.screenshot(path=str(DOCS / "assets/social-preview.png"))

        pngs = {}
        for size in (32, 48, 180):
            pg = browser.new_page(viewport={"width": size, "height": size})
            pg.set_content(f'<html><body style="margin:0;background:transparent">{ICON_SVG.format(s=size)}</body></html>')
            pngs[size] = pg.screenshot(omit_background=True)
        browser.close()

    (DOCS / "favicon.png").write_bytes(pngs[32])
    (DOCS / "apple-touch-icon.png").write_bytes(pngs[180])
    from PIL import Image

    Image.open(io.BytesIO(pngs[48])).save(DOCS / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    print("rendered PDFs, social preview, and icons")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--chromium", help="path to a Chromium executable")
    render(ap.parse_args().chromium)
