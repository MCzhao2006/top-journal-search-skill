# Cell Adapter

## Scope

Unqualified `Cell` means the flagship `Cell` journal. `Cell Press` expands to the publisher portfolio (for example Cancer Cell, Molecular Cell, Neuron, Immunity, Current Biology, Cell Reports, etc.).

Official domain: `cell.com`.

## Search behavior

Use Cell.com's search UI first. A commonly observed direct pattern is:

`https://www.cell.com/action/doSearch?type=quicksearch&text1=<query>&field1=AllField&pageSize=25&startPage=0`

Treat this as a convenience pattern, not a stable API. If blocked, use domain-restricted search plus Crossref/PubMed discovery.

Cell also exposes journal RSS feeds (for example in-press feeds), useful for freshness checks when the request is specifically about newly posted material.

## Cell-specific verification

- Verify `Cell` flagship vs another Cell Press journal.
- Separate Articles from Reviews, Previews, Perspectives, Resource papers, etc.
- Cell Press DOI patterns commonly begin `10.1016/`, shared with many Elsevier journals, so prefix alone is weak evidence of journal identity.
