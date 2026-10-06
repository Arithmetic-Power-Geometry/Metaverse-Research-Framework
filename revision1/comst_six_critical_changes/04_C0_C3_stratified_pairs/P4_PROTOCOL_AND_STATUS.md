# P4 — C0–C3 stratified pair validation

## Frozen design
A 180-pair register has been generated across the frozen corpus strata:
- Networking/edge/XR: 55
- Digital twin: 30
- Semantic communication: 25
- Security/privacy: 30
- Sustainability: 15
- AI/GenAI: 10
- Other empirical: 15

Each pair must be coded on P,W,D,H,N,B,M,E from full-text evidence. Allowed dimension states are 1 (compatible), 0.5 (partially/conditionally compatible), 0 (incompatible), and ? (unresolved). A hard mismatch in P, M, or E blocks direct ranking. Unresolved required dimensions cannot be silently scored.

The register deliberately contains no fabricated C0-C3 labels. The existing six-pair demonstration is not expanded by title/abstract inference.

## Completion gate
P4 is complete only when all 180 rows have full-text evidence for the eight dimensions, a hard-mismatch decision, S_C where defined, final C0/C1/C2/C3 class, and an auditable coder note/source location. Only then may n/% be reported.

## Planned outputs
1. P4_STRATIFIED_PAIR_REGISTER_180.csv
2. P4_C0_C3_COUNTS.csv after coding
3. P4_C0_C3_BY_STRATUM.csv after coding
4. P4_THRESHOLD_SENSITIVITY.csv after coding
5. manuscript table/figure after coding

This separation is intentional: sampling is complete; empirical pair coding remains evidence-dependent.
