# RUN 17 — FL-Aware Reconstruction Batch 01

## Workflow gate
The workflow and requirements were re-fetched before reconstruction. No workflow or scientific benchmark was executed.

## PNE011
Resource Allocation of Federated Learning for the Metaverse with Mobile Augmented Reality:
- objective combines total energy consumption, completion time and model accuracy;
- decision variables include bandwidth allocation, transmission power, CPU frequency and video-frame resolution;
- method decomposes the non-convex problem into two subproblems;
- convergence analysis and computational complexity are reported;
- numerical comparisons vary objective weights.
This establishes a multi-objective FL/MAR comparator but does not yet supply a source-faithful executable specification.

## New comparator: Hou et al. 2024 JSAC
Efficient Federated Learning for Metaverse via Dynamic User Selection, Gradient Quantization and Resource Allocation:
- six authors verified;
- IEEE JSAC 42(4):850-866;
- DOI 10.1109/JSAC.2023.3345393;
- jointly models user selection, wireless transmission error, gradient quantization error, time and energy budgets;
- sequential decision problem transformed to an MDP with a soft actor-critic solution;
- experiments evaluate dynamic-changing network environments.

## Reconstruction consequence
PNE011 and Hou2024 are related FL/resource-allocation studies but are not automatically numerically comparable. Their objective definitions, decision variables, learning error terms and dynamic-network assumptions must pass P-W-D-H-N-B-M-E before shared benchmarking.

## Bibliography
Two complete records were appended: Hou et al. JSAC 2024 and Chen et al. WWW Companion 2023 FL survey.
