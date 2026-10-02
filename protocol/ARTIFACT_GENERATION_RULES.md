# Artifact Generation Rules

1. Final analytical figures/tables are generated from machine-readable repository data.
2. Each artifact records input files and generation script.
3. Candidate hypotheses are visually/textually distinguishable from validated findings.
4. Missing values remain missing; they are not imputed merely for visual completeness.
5. Counts from incomplete seed datasets must be labeled as seed/audit status and must not be presented as field-wide statistics.
6. Every plotted numerical comparison must satisfy the metric/comparability rules.
7. Generated outputs are reproducible from a clean environment through a documented command or workflow.
8. Final artifacts should be readable in double-column publication layout.
9. Source data remain available alongside derived artifacts.
10. Artifact generation must fail rather than silently continue when required columns, invalid categories, duplicate IDs, or broken evidence references are detected.
