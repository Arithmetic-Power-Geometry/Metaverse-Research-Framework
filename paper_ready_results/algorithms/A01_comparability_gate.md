# Algorithm A01 — Cross-Paper Comparability Gate

Input: studies i and j with tuples C=(P,W,D,H,N,B,M,E).

1. Match problem definition P.
2. Check workload W and dataset/input D compatibility.
3. Check hardware H and network/system conditions N.
4. Check baseline set B.
5. Match metric definition/unit/aggregation M.
6. Match evaluation protocol E.
7. If any material field is incompatible or unresolved, label NUMERIC_RANKING_BLOCKED.
8. Otherwise label COMPARABLE_WITH_QUALIFICATIONS and record residual assumptions.

Output: comparison decision plus explicit mismatch provenance.

Rule: shared metric names alone never establish comparability.
