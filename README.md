# SOA-to-Agentic AI Terminology Mapping

**Published by [Skan.ai](https://www.skan.ai)** · Prose licensed [CC-BY 4.0](LICENSE) · Structured data licensed [Apache 2.0](LICENSE-APACHE)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21823088.svg)](https://doi.org/10.5281/zenodo.21823088)

**[Read it as a page →](https://skandotai.github.io/soa-to-agentic-terms/)**

## Why this exists

The agentic AI landscape today has no shared vocabulary. "Agent," "workflow," "orchestration," and "task" mean different things depending on which vendor or team is using them. That inconsistency is already producing integration failures, procurement confusion, and governance blind spots — the same symptoms enterprise computing had before Service-Oriented Architecture gave it a common grammar in the early 2000s.

SOA's success wasn't only technical. Terms like *service contract*, *loose coupling*, and *service composition* became universally understood, which let organizations design and govern complex distributed systems with shared confidence. The standards that followed — SOAP, WSDL, BPEL — turned those concepts into implementable technology.

Agentic AI faces the same problem SOA solved once already, with one difference: agents don't just execute predefined operations the way services do. They adapt, learn, and make autonomous decisions. That extension is real, and it's why this mapping is a starting point rather than a finished standard.

## What this is

A term-by-term translation of proven SOA concepts into their agentic equivalents — twenty-eight mapped pairs, from `Service → Agent` through `Governance → Agentic Governance` — with a short description of each term on both sides. Related concepts sit next to each other, so the list reads as one vocabulary rather than a pile of definitions. See [`mapping-table.json`](mapping-table.json) for the structured version.

This is explicitly **not** a claim that Skan invented these agentic terms, or that SOA belongs to Skan. It's the use of a precedent the industry already validated, offered to accelerate standardization in a domain that badly needs it.

## What this isn't

A complete architectural standard. The mapping is a vocabulary, not a governance framework, an interaction protocol spec, or a certification scheme. Those are harder problems — agent classification and autonomy levels, interaction and negotiation protocols, adaptive orchestration patterns, governance and audit frameworks, and performance/quality standards — and they remain open. See [`context.md`](context.md) for the short version of the argument, or the [whitepaper](whitepaper.md) ([PDF](docs/downloads/skan-agentic-ai-terminology-whitepaper.pdf)) for the full one — including what SOA got wrong, and why those failures matter here.

## Related project

The Agentic Ontology of Work (AOW) defines how these terms relate to each other. It includes a five-level autonomy scale, rules for human oversight, and checks that trace each result to its business objective. It is published as an OWL ontology with SHACL shapes and JSON Schemas.

- Repository: https://github.com/Skandotai/agentic-ontology-of-work
- Website: https://skandotai.github.io/agentic-ontology-of-work/
- Crosswalk from the 28 agentic terms to AOW: https://github.com/Skandotai/agentic-ontology-of-work/blob/main/crosswalks/soa-to-agentic-terms.csv

## What's here

```
soa-to-agentic-terms/
├── mapping-table.json            the mapping — 28 term pairs, structured
├── context.md                    the short version: why this mapping exists
├── whitepaper.md                 the full paper on standardizing Agentic AI terminology
├── CITATION.cff                  citation metadata (powers GitHub's "Cite this repository")
├── CONTRIBUTING.md               how to propose a change
├── tools/make_assets.py          renders the PDFs and images from the JSON and the whitepaper
└── docs/                         the published site
    ├── index.html                  the mapping, rendered
    ├── about/index.html            the thinking behind it
    └── downloads/                  terms sheet (PDF), terms (CSV), whitepaper (PDF)
```

`mapping-table.json` is the canonical source. The rendered table, the CSV, and the terms sheet are all derived from it, so if they ever disagree, the JSON is right. `tools/make_assets.py` regenerates the terms sheet and whitepaper PDFs.

## Contributing

This is offered as a starting vocabulary, not a finished one. If you think a mapping is wrong, incomplete, or missing — open an issue or a pull request. See [CONTRIBUTING.md](CONTRIBUTING.md). Disagreement on where SOA concepts break down for agentic systems is expected and useful.

## License

Prose and documentation: [CC-BY 4.0](LICENSE). Structured data (`mapping-table.json`, and the CSV): [Apache 2.0](LICENSE-APACHE).

In plain terms, both permit the same thing: copy it, adapt it, build on it, use it commercially — just credit Skan, Inc. and say if you changed it. You don't need to ask.

## Citing this work

Archived on Zenodo, so it can be cited durably:

- **[10.5281/zenodo.21823088](https://doi.org/10.5281/zenodo.21823088)** — always resolves to the latest version
- **[10.5281/zenodo.21823089](https://doi.org/10.5281/zenodo.21823089)** — this release, v2.0.0

`CITATION.cff` carries the same metadata in machine-readable form, and GitHub's "Cite this repository" button reads it.
