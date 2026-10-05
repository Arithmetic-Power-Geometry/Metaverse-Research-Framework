# Algorithm A03 — Artifact Reproducibility Audit

Input: eligible study s.

1. Verify scholarly identity and DOI.
2. Locate author/publisher-linked artifacts and record provenance.
3. Audit independently: code; data; configuration/parameters; seeds/randomness; environment/dependencies; execution instructions; persistent archive; independent reproduction.
4. Never infer unobserved fields from repository presence.
5. Distinguish explicit absence from NOT_IDENTIFIED_IN_AUDITED_SOURCES.
6. Score only after all eight fields are inspected.
7. Assign R0-R4 using the frozen rubric.
8. R4 requires independent reproduction plus a complete rerun path.
9. Report audit state and eligible denominator with prevalence.

Output: field-level record, score/class, unresolved fields and provenance.

Reproducibility class is not a scientific-quality ranking.
