# Adversarial IEEE/COMST Review — RUN 17 Batch 01

## Recommendation: CONTINUE; DO NOT BENCHMARK YET

### Strongest rejection argument
The FL papers share a Metaverse label but optimize materially different systems. A common numerical benchmark would be scientifically weak unless source equations, workload definitions and evaluation parameters are reconstructed first.

| ID | Severity | Objection | Required correction | Status |
|---|---|---|---|---|
| R17-01 | CRITICAL | PNE011/Hou2024/HFedMS are not yet benchmark-compatible | Apply full P-W-D-H-N-B-M-E gate | OPEN |
| R17-02 | HIGH | PNE011 exact equations/parameter table not yet fully reconstructed | Recover source-faithful model before implementation | OPEN |
| R17-03 | HIGH | Hou2024 adds gradient quantization/user-selection dynamics absent from PNE011 abstraction | Keep separate problem dimensions | CORRECTED IN TABLE |
| R17-04 | HIGH | HFedMS is a learning-system design, not merely resource allocation | Do not collapse into same algorithm ranking | CORRECTED |
| R17-05 | MEDIUM | Numerical superiority claims are scenario-specific | Report provenance, not expected benchmark outcome | CORRECTED |

## Gate
No benchmark execution is authorized from RUN 17 Batch 01.
