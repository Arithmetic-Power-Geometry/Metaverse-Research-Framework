# RUN 16 — Artifact Audit Batch 02

## Scope
Expanded the artifact audit around FL/privacy/benchmark precedents and re-checked PNE011, PNE016 and PNE017.

## Verified findings
- PNE011 final IEEE publication is verified; a curated Metaverse privacy-computing repository links the paper, but a dedicated implementation was not established in the audited sources.
- HFedMS is a stronger artifact candidate: the curated repository explicitly links both paper and code; the IEEE final paper evaluates streamed non-i.i.d. FEMNIST on 368 simulated devices against eight benchmarks.
- PNE016 and PNE017 have authoritative final publication/preprint evidence for their methods and experiments, but reusable code/data/configuration packages were not identified in the current audit.
- MetaverseBench complete metadata is now resolved: Hainan Ye and Lei Wang, TBench 3(3), 100138, DOI 10.1016/j.tbench.2023.100138.

## Wording rule
Failure to identify an artifact is recorded as **not identified in audited sources**, never as proof that no artifact exists.

## Bibliography
Three fully verified records were appended: Privacy Computing Meets Metaverse; HFedMS; and MetaverseBench. The MetaverseBench quarantine entry was removed after author verification.

## Next
Deep-audit HFedMS and MetaverseBench repositories/artifacts, then continue eligible primary studies. Do not publish prevalence percentages until corpus denominator freezes.
