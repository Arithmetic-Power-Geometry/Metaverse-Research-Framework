# 1. Fresh database search and complete PRISMA

## Objective
Create a prospective, reproducible search record independent of the unrecoverable historical search trajectory.

## Required databases
- IEEE Xplore
- Scopus
- Web of Science
- ACM Digital Library
- Optional supplementary publisher searches: ScienceDirect and SpringerLink

## Required fields per database execution
database, search_date, exact_query, returned_n, exported_n, file_name, deduplicated_n, title_abstract_included_n, full_text_assessed_n, excluded_n, final_included_n, notes

## Procedure
1. Freeze search date and exact search strings before screening.
2. Export all results with DOI/title/author/year/venue/abstract when available.
3. Concatenate exports without deleting source provenance.
4. Deduplicate by DOI first, then normalized title.
5. Screen title/abstract with explicit inclusion/exclusion decisions.
6. Screen full text and record one primary exclusion reason per excluded record.
7. Produce PRISMA counts from the ledger only.
8. Archive raw exports, deduplication output, screening ledger, and query log.

## Non-negotiable rule
Do not reconstruct or estimate counts from the existing 200-reference library. A valid PRISMA diagram must be generated only from executed database exports.
