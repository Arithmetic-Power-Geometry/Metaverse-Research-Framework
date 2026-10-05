# Algorithm A02 — Evidence-Supported Gap Falsification

Input: candidate gap g.

1. Record the exact gap statement and scope.
2. Search closest surveys/reviews.
3. Search primary evaluated studies.
4. Search datasets, benchmarks, testbeds and reusable artifacts.
5. Search standards/final specifications and active work items separately.
6. Search contrary evidence explicitly.
7. Classify evidence maturity, reproducibility and deployment maturity.
8. If contrary evidence directly satisfies g, reject or narrow g.
9. If evidence is partial, rewrite g as an evidence/comparability/reproducibility/deployment limitation.
10. Promote g only when the narrowed statement survives contrary-evidence search.

Output: REJECTED, NARROWED, or SUPPORTED candidate gap with provenance.
