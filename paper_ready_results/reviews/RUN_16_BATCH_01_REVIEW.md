# Adversarial IEEE/COMST Review — RUN 16 Batch 01

## Recommendation: CONTINUE; METHOD PROMISING, DENOMINATOR NOT YET FROZEN

### Strongest rejection argument
A reproducibility audit can itself become irreproducible if 'code available' is treated as a proxy for rerunnability or if missing artifacts are inferred from unsuccessful searches. The current batch is too small for field-level prevalence claims.

## Findings
| ID | Severity | Objection | Required correction | Status |
|---|---|---|---|---|
| R16-01 | CRITICAL | Repository presence cannot equal reproducibility | Eight-field artifact rubric adopted | CORRECTED |
| R16-02 | HIGH | Current sample is not a frozen denominator | Audit all eligible computational studies before reporting percentages | OPEN |
| R16-03 | HIGH | 'not found' may reflect search failure | Use 'not identified in audited sources as of date' unless absence is explicit | CORRECTED IN RULE |
| R16-04 | HIGH | Independent reproduction is much stronger than author-provided rerun scripts | Keep independent reproduction as separate highest-level field | CORRECTED |
| R16-05 | MEDIUM | Persistent archival identity matters for long-term reproducibility | DOI/archive/release field added | CORRECTED |
| R16-06 | MEDIUM | R0-R4 could be misread as paper-quality ranking | State explicitly that it measures artifact evidence only | CORRECTED |

## Gate
RUN 16 remains OPEN. Do not publish percentages until the eligible corpus and audit denominator are frozen.
