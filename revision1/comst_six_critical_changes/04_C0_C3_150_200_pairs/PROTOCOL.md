# 4. C0-C3 validation on 150-200 stratified pairs

## Target
Code 180 study pairs, stratified rather than all 19,900 possible pairs.

## Strata
- same domain / same task
- same domain / different task
- same dataset / different method
- same metric name / different metric semantics
- same task / different hardware or network
- cross-domain near-neighbor pairs
- deliberately incompatible negative controls
- known compatible positive controls where available

## Pair-level output
For each pair code P,W,D,H,N,B,M,E as 0,0.5,1,? plus hard_mismatch and C_class.

## Validation
At least 30-50 pairs should be independently coded by coder 2.

## Threshold analysis
Evaluate 0.70, 0.75, 0.80 and compare with expert pair-level judgments. Do not claim a threshold is validated merely because hard mismatches dominate.
