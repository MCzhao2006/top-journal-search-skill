# Query Playbook

## 1. Normalize the request

Capture these fields when present:

- journal scope: flagship vs family
- concept / disease / method / molecule / population
- exact title, DOI, author, year
- date window
- article type: research, review, editorial, guideline, correspondence, etc.
- desired output: one exact paper, recent papers, evidence synthesis, metadata verification

Do not force missing filters. Start broad enough to find candidates.

## 2. Exact lookup recipes

### DOI
Search the DOI as an exact token. Prefer DOI resolution or the publisher's article page. Verify that the destination journal matches the requested journal.

### Exact title
Try in order:

1. full title in quotes
2. first 8-12 distinctive words
3. first author surname + 3-5 title keywords
4. DOI from Crossref/PubMed if the title is still ambiguous

### Author
Use surname + distinctive topic + approximate year. Author-only searches can be noisy; verify the byline on the article page.

## 3. Concept search recipes

Build 2-4 queries, not one enormous query:

1. **Precise:** core entity + intervention/mechanism + outcome
2. **Synonym:** replace acronyms, spelling variants, or disease synonyms
3. **Broad:** entity + outcome only
4. **Method-specific:** add trial type/model/assay when relevant

For clinical questions, optionally add population and study design after the broad query returns candidates.

## 4. Ranking

Rank by:

1. exact journal match
2. direct relevance to the user's claim/question
3. article type appropriate to the task
4. recency when recency matters
5. methodological fit / evidence level
6. accessibility of enough text to verify the match

Do not rank primarily by citation count.

## 5. Verify support strength

Use these labels when matching a paper to a claim:

- **Direct support:** the paper directly tests the claim in the relevant population/model.
- **Partial support:** supports one component but not the whole claim.
- **Background support:** establishes context, prevalence, mechanism, or prior knowledge.
- **Not suitable:** title/topic is related, but the result does not substantiate the claim.

## 6. Time-sensitive searches

For “latest”, “recent”, “this week”, “this year”, etc.:

- record the search date
- sort by publication date, not search-engine ranking
- verify the newest few results on official pages
- distinguish “online first / published online” from issue date when both exist
- do not call an accepted/in-press manuscript “published” unless the journal does
