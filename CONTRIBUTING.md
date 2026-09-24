# Contributing

Contributions to the SOA-to-Agentic AI Terminology Mapping are welcome.

## Types of contribution

1. **Pairings that do not hold.** An SOA concept whose agentic equivalent differs in an important way. Describe where the correspondence fails and what the agentic term requires.
2. **Incorrect pairings.** Quote the pairing, propose a replacement, and give the reason.
3. **Missing terms.** Propose the SOA term, the agentic term, and a description of each.

Please open an issue at https://github.com/Skandotai/soa-to-agentic-terms/issues before submitting a pull request. Corrections to typos and broken links may be submitted directly as pull requests.

## Making changes

`mapping-table.json` is the canonical source. To change a pairing:

1. Edit `mapping-table.json`.
2. Update the matching row in `docs/downloads/soa-agentic-terms.csv` and in `docs/index.html`.
3. Regenerate the terms sheet PDF with `python tools/make_assets.py`.

If you cannot regenerate the PDF, state this in the pull request. A maintainer will regenerate it.

The Agentic Ontology of Work maps each agentic term to an ontology class in `crosswalks/soa-to-agentic-terms.csv` (https://github.com/Skandotai/agentic-ontology-of-work). If a change affects a mapped term, note it in the pull request so the crosswalk can be updated.

## Style

Use plain US English. Describe each term by what it is and does, in one or two sentences.

## Conduct

Discussion should remain professional and focused on the work. Harassment, personal attacks, and discrimination are not permitted. Maintainers may remove comments or contributors that do not meet this standard.

## License

Contributions are licensed under the same terms as the project: CC-BY 4.0 for prose and Apache 2.0 for the structured data.
