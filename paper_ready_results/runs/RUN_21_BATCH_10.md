# RUN 21 — Corpus Saturation and Bibliography Expansion Batch 10

## Scope
Resolution of held XR/5G/semantic prototype records, NUMA edge allocation, and 5G/6G feasibility evidence.

## Safety
The live workflow and requirements were re-fetched before changes. No CI workflow or scientific benchmark was executed.

## Newly admitted complete records
1. Xincheng Huang, James Riddell, Robert Xiao. Virtual Reality Telepresence: 360-Degree Video Streaming with Edge-Compute Assisted Static Foveated Compression. IEEE TVCG 29(11):4525-4534, 2023. DOI 10.1109/TVCG.2023.3320255.
2. Usama Farooq, Timo Bräysy, Paula Alavesa. QoS Evaluation of a 5G Test Network for Metaverse Applications: Delay and Jitter Comparison with Wi-Fi and Ethernet. ComComAp 2025, pp. 236-242. DOI 10.1109/ComComAp68359.2025.11353171.
3. Yuxuan Li, Sheng Jiang, Baoling Liu, Bizhu Wang, Le Wang, Mingquan Rao. Semantic Communication-Enabled Cloud-Edge-End Collaborative Metaverse Services Architecture. SPAWC 2025, pp. 1-5. DOI 10.1109/SPAWC66079.2025.11143472.
4. Jia Xu, Hao Wu, Jixian Zhang. Truthful Mechanism for Service Utility Maximization in Edge-Enabled Metaverse Based on NUMA. Future Generation Computer Systems 174:108015, 2026. DOI 10.1016/j.future.2025.108015.
5. Maria Christopoulou, Ioannis Koufos, George Xilouris, Nikos Dimitriou. 5G/6G Architecture Evolution for XR and Metaverse: Feasibility Study, Security, and Privacy Challenges for Smart Culture Applications. IEEE Access 13:103077-103094, 2025. DOI 10.1109/ACCESS.2025.3578595.

## Evidence maturity consequences
- Huang et al. is an end-to-end ~6K 360-degree VR telepresence prototype over 5G mmWave + edge compute, with PSNR/FOVVideoVDP evaluation and a user study.
- Farooq et al. is a measured network testbed using a Unity server and Meta Quest 3; it compares Ethernet, Wi-Fi 6 and local 5G one-way delay/jitter.
- Li et al. verifies SC-CEE-Meta using Meta Quest Pro and reports semantic/video quality behavior under poor channels.
- Xu et al. contributes truthful NUMA-aware offline/online auction mechanisms and simulation evidence.
- Christopoulou et al. is a 5G/6G XR feasibility study, not an operational 6G deployment.

## Guardrail
Prototype/testbed/user-study evidence must remain distinct from simulation, feasibility analysis and operational deployment. Source-reported numeric improvements are provenance, not cross-paper benchmark results.

## Still unresolved
PNE018 remains unresolved at complete metadata level. It must not be promoted by guessing.
Other quarantine records and broader foundational snowballing continue in the next batch.

## Next
RUN21 Batch11: resolve PNE018 and remaining quarantine, then foundational XR/VR/edge/6G backward snowballing and dataset/testbed references.
