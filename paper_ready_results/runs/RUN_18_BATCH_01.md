# RUN 18 — PNE016 Reconstruction Batch 01

## Source
Nan Liu, Tom H. Luan, Yuntao Wang, Yiliang Liu, Zhou Su. QoE-Oriented Cooperative VR Rendering and Dynamic Resource Leasing in Metaverse. IEEE Transactions on Mobile Computing 24(10):10247-10263, 2025. DOI 10.1109/TMC.2025.3569695.

## Verified system structure
- cooperative VR scene pre-rendering between users and Planets (edge servers);
- EdgeVRQoE combines rendering delay and visual quality;
- multidimensional leased resources include GPU, CPU and outbound bandwidth;
- resource leasing is formulated as a double-layer decision problem;
- solution uses a hybrid-action multi-agent reinforcement-learning dynamic resource auction mechanism;
- evaluation is by extensive simulation;
- the paper reports at least 18-fold QoE improvement over compared schemes.

## Fidelity rule
The reported 18-fold value is provenance evidence only. It is not a benchmark target, expected reproduction result, or validation tolerance.

## Reconstruction status
BLOCKED for execution. Exact EdgeVRQoE equation, rendering/service models, state/action/reward definitions, auction mechanism details, simulator parameters, baselines, hyperparameters, randomization/seeds and stopping/evaluation protocol must be source-recovered before implementation.

## Cross-paper implication
PNE016 cannot be numerically ranked against PNE011 merely because both allocate resources: PNE016 leases GPU/CPU/outbound bandwidth for VR rendering and optimizes a named QoE construct, whereas PNE011 allocates wireless/compute/resolution variables for FL-MAR under energy/time/accuracy objectives.
