# Bibliography Integrity Policy

The manuscript bibliography is built continuously from the evidence base.

## Admission gate
A record enters `metaverse_comst_master.bib` only after title, publication type, venue, year and DOI/persistent identifier are checked. Author lists must also be complete before normal manuscript citation.

Records with incomplete or conflicting metadata remain in `bibliography_quarantine.csv`.

## Source priority
1. publisher/IEEE/ACM/proceedings record;
2. DOI/Crossref-equivalent authoritative metadata;
3. institutional research portal;
4. DBLP for computer-science bibliographic cross-check;
5. preprint only when no peer-reviewed version exists or for frontier surveillance.

A preprint is not cited instead of a verified journal/conference version.

## Corpus-count rule
Foundational/context papers (e.g., general 6G) may be cited for technical background but are not counted as included Metaverse primary studies unless they satisfy the review inclusion criteria.

## Duplicate rule
Deduplicate by DOI, then persistent ID, then normalized title + first author + year.

## Citation-key stability
Once a verified record is cited in manuscript drafting, its BibTeX key should not change without a migration note.
