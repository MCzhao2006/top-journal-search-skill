# Existing Public Skill Review

Research date: 2026-10-09.

The public Agent Skill ecosystem already contains many journal-oriented skills, but most found examples focus on manuscript fit, writing, submission conventions, citation formatting, or multi-source academic search rather than a Wikipedia-style publisher-site retrieval workflow.

Examples reviewed during design:

- `nature-academic-search` on SkillMD: multi-source academic search / citation verification workflows.
- `nature-citation`: claim-to-citation matching across Nature/CNS-related titles.
- `science`, `cell`, `jama`, `nejm`, `pnas` by brycewang-stanford: venue-fit and manuscript-targeting guidance.
- Lancet writing and Research-in-Context skills in Awesome-Journal-Skills: manuscript-structure and evidence-panel guidance.

Design decision:

- Reuse the **patterns**, not the text: progressive routing, source hierarchy, strict flagship-vs-family scoping, explicit verification, and current-guideline re-checks.
- Add what the existing examples generally lack: website-search routing, exact article-location workflow, access-failure fallbacks, normalized metadata discovery, and article-page verification.
- Keep this package focused on **finding and verifying information**, not on writing a paper for a particular journal.

Public references used to verify search behavior include official support/help pages from Nature, NEJM, JAMA Network, and PNAS, plus current publisher pages and public registry pages. Search URL implementations can change, so adapters explicitly treat direct URL templates as convenience hints rather than stable APIs.
