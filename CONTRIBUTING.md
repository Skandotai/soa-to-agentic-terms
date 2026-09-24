# Contributing

This mapping is offered as a starting vocabulary, and it improves through disagreement. Thank you for taking the time.

## The most useful contributions

1. **A pairing that breaks.** An SOA concept that nearly fits its agentic equivalent and then doesn't. Say where the analogy stops working and what the agentic side actually needs. These breakages are where the vocabulary needs its own words.
2. **A pairing that's wrong.** Quote it, and say what you'd pair it with instead and why.
3. **A missing term** you rely on, with both sides described.

Open an [issue](https://github.com/Skandotai/soa-to-agentic-terms/issues) for any of these before sending a pull request. Typos and broken links can go straight to a pull request.

## How changes are made

`mapping-table.json` is the canonical source. A change to a pairing means:

1. edit `mapping-table.json`
2. update the matching row in `docs/downloads/soa-agentic-terms.csv` and the rendered row in `docs/index.html`
3. regenerate the terms sheet PDF with `python tools/make_assets.py`

If you're not set up to regenerate the PDF, say so in the pull request and a maintainer will do it.

If a change affects a term that the [Agentic Ontology of Work](https://github.com/Skandotai/agentic-ontology-of-work) maps (see its `crosswalks/soa-to-agentic-terms.csv`), mention it so the crosswalk can be updated too.

## Style

Write in plain US English. Describe each term by what it is and does, not by what it's like. Keep each description to a sentence or two.

## Conduct

Be direct about ideas and generous with people. Disagreement about where the analogy holds is expected and welcome. Personal attacks, harassment, and discrimination aren't. Maintainers may remove comments or contributors that don't meet that bar.

## License

By contributing, you agree that your contributions are licensed under the same terms as the project: CC-BY 4.0 for prose, Apache 2.0 for the structured data.
