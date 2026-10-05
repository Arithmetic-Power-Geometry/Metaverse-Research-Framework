# RUN 21 — Corpus Saturation and Bibliography Expansion Batch 14

## Scope
Resolution of held 360-degree viewport/streaming candidates and extension of the immersive-streaming lineage.

## Workflow safety
The live validation workflow and requirements were re-fetched before repository changes. No CI workflow or scientific benchmark was executed.

## Newly admitted complete records
1. Mu Wang, Shuai Peng, Xingyan Chen, Yu Zhao, Mingwei Xu, Changqiao Xu. CoLive: An Edge-Assisted Online Learning Framework for Viewport Prediction in 360-Degree Live Streaming. ICME 2022, pp. 1-6. DOI 10.1109/ICME52920.2022.9859963.
2. Junjie Li, Yumei Wang, Yu Liu. Meta360: Exploring User-Specific and Robust Viewport Prediction in 360-Degree Videos through Bi-Directional LSTM and Meta-Adaptation. ISMAR 2023, pp. 652-661. DOI 10.1109/ISMAR59233.2023.00080.
3. Yuxiang Hu, Yu Liu, Yumei Wang. VAS360: QoE-Driven Viewport Adaptive Streaming for 360 Video. ICMEW 2019, pp. 324-329. DOI 10.1109/ICMEW.2019.00062.
4. Yinjie Zhang, Mingyuan Wu, Beitong Tian, Jiaxi Li, Bo Chen, Qian Zhou, Klara Nahrstedt. SAVG360: Saliency-Aware Viewport-Guidance-Enabled 360-Video Streaming System. IEEE ISM 2023, pp. 36-43. DOI 10.1109/ISM59092.2023.00011.
5. Xiang Xu, Xiaobin Tan, Shunyi Wang, Zhuolin Liu, Quan Zheng. Multi-Features Fusion Based Viewport Prediction with GNN for 360-Degree Video Streaming. MetaCom 2023. DOI 10.1109/MetaCom57706.2023.00023.

## Evidence and artifact consequences
- CoLive uses edge-assisted collaborative online learning and public 360-degree data.
- Meta360 uses BiLSTM + meta-adaptation and diverse datasets.
- VAS360 provides an earlier QoE-driven tiled viewport-adaptive streaming system.
- SAVG360 includes viewport-trace evaluation, a user study, and a publicly linked GitHub repository from the Illinois research group; repository presence must still be audited before reproducibility scoring.
- Xu et al. use public datasets and GNN fusion of content/current-user/cross-user features.

## Synthesis
The lineage now supports a coherent progression:
QoE-aware tiled delivery -> user-aware prediction -> edge collaborative learning -> GNN multi-feature fusion -> meta-adaptation/personalization -> proactive saliency guidance -> privacy-aware/mobile-friendly prediction.
This is more defensible than presenting each paper as an isolated algorithm.

## Next
RUN21 Batch15: tactile/URLLC/edge-rendering foundations plus XR artifact audit candidates, including SAVG360; continue toward 200+.
