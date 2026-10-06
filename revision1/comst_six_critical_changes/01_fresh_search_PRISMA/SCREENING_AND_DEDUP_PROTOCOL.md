# Screening and deduplication protocol

1. Concatenate raw exports while preserving source_database and source_record_id.
2. Normalize DOI: lowercase, remove https://doi.org/, doi:, whitespace.
3. Exact DOI deduplication.
4. For DOI-missing records, normalize title: lowercase, Unicode normalize, strip punctuation, collapse whitespace.
5. Exact normalized-title deduplication.
6. Near-title candidates are flagged for human review; they are never auto-deleted solely by fuzzy similarity.
7. Title/abstract screen against the declared scope.
8. Full-text screen all title/abstract inclusions.
9. Assign exactly one primary full-text exclusion reason.
10. Keep standards/authoritative specifications in a separate normative evidence register.
11. Freeze the prospective validation corpus and calculate PRISMA only from the ledgers.

## Inclusion
Material contribution to at least one review question plus sufficient information to classify technical/evidence fields.

## Primary exclusion reasons
E1 rhetorical Metaverse/XR mention only
E2 outside networked/technical/evidence scope
E3 editorial/news/promotional/non-scholarly
E4 superseded/duplicate report
E5 inaccessible full text after documented attempt
E6 application description without transferable technical/empirical evidence
E7 language/year/type outside prospective protocol
