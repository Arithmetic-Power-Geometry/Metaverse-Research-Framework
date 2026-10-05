# PNE011 Source-Faithful Reconstruction Register — Batch 02

## Verified model
The optimization is
min over {B_n,p_n,f_n,s_n}: w1 E + w2 T - rho A,
with total-bandwidth, transmit-power, CPU-frequency and two-resolution constraints.

The source models total energy as transmission plus local-computation energy and total completion time across the FL process. The reported accuracy surrogate is 1 - 1.578 exp(-6.5e-3 s_n).

## Verified experiment
The parameter register in `pne011_parameter_provenance.csv` records only values directly exposed by the source. No missing parameter is imputed.

## Baseline
The reported MinPixel baseline uses minimum resolution and equal bandwidth allocation, with CPU frequency or transmit power randomized/set according to the sweep being performed.

## Execution gate
**BLOCKED.** Before implementation:
1. transcribe every equation for E, T, transmission rate and computation energy;
2. transcribe Algorithm 1 and Algorithm 2 without algebraic simplification;
3. capture stopping tolerances/maximum iterations if fully recoverable;
4. encode all baseline branches;
5. independently compare the implementation equations against the source;
6. only then mark scientific_ready=true.

No numerical reproduction is authorized by this register.
