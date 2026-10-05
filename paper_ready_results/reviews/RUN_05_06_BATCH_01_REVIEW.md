# Adversarial IEEE/COMST Review — RUN 05/06 Batch 01

## Recommendation: MAJOR REVISION / CONTINUE

### Strongest rejection argument
The corpus now contains many sophisticated algorithms, but reported performance improvements are not mutually comparable because objectives, QoE definitions, constraints, workload semantics, resource dimensions and experimental environments differ. A paper that reproduces percentage gains side-by-side would be misleading.

## Findings
| ID | Severity | Objection | Required correction | Status |
|---|---|---|---|---|
| R0506-01 | CRITICAL | Cross-paper numerical ranking is currently invalid | Use family-level comparability and P-W-D-H-N-B-M-E gates | CORRECTED IN DESIGN |
| R0506-02 | HIGH | PNE011/PNE015 appear related but their application/system models differ | Complete equation/parameter reconstruction before common benchmark | OPEN |
| R0506-03 | HIGH | PNE016/PNE017 both VR but optimize different decision structures and constraints | Extract exact state/action/objective/workload/environment | OPEN |
| R0506-04 | HIGH | Reported '18-fold QoE' for PNE016 is metric/scenario-specific | Never transport this gain across studies | CORRECTED |
| R0506-05 | HIGH | Several records still lack verified complete authors in current batch | Keep them out of master BibTeX until verified | OPEN |
| R0506-06 | MEDIUM | Adjacent wireless-VR work may not satisfy Metaverse inclusion criterion | Apply inclusion rule explicitly | OPEN |

## Gate
RUN 05 and RUN 06 remain OPEN. The batch is suitable for a manuscript comparison table only if it reports structural comparability rather than winner rankings.
