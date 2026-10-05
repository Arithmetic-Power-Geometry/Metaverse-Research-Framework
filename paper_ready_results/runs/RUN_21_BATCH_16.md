# RUN 21 — Batch 16: Artifact Audit Expansion

## Safety
Workflow SHA 8a1c11bd40e1db920d266d7f7569ffa844ddb98a and requirements SHA 0cab7f8037954b11051a5f5ce482741ea930f182 were re-fetched before changes. No CI workflow or scientific benchmark was executed.

## Wu et al. 2026 / SaliencyFov
Paper: Saliency-Guided Foveated Video Encoding for Low-Latency and Immersive Cloud VR, IEEE TVCG 32(5):3368-3378, DOI 10.1109/TVCG.2026.3679056.

Audit observations:
- public GitHub repository confirmed: WuZemyp/SaliencyFov
- public source code: yes
- explicit MIT license: yes
- build/dependency metadata: Cargo.toml and Cargo.lock present
- execution/build documentation: README plus linked build/install guidance
- pretrained model artifacts: best_model.pt and best_model_ts.pt present
- platform integration: repository is based on/forks ALVR and paper states integration into an open-source cloud-VR gaming platform
- paper reports comprehensive experiments and IRB-approved user study
- persistent scholarly archive for repository: not established in this audit
- independent reproduction: not established

Conservative reproducibility classification: R3 candidate, pending exact field-by-field scoring and persistent-archive check. Do not promote to R4 without independent reproduction.

## SAVG360
Paper-linked public repository was previously identified, but this pass did not establish sufficient direct repository metadata for a full field-by-field score. Status remains deep-audit pending; no score inflation.

## Methodological consequence
Repository presence is not reproducibility. The audit records code, data, configuration, randomness, environment, instructions, persistence and independent reproduction separately.

## Next
RUN21 Batch17: continue primary literature saturation while deep-auditing remaining artifact-positive studies; add persistent archive checks and eligible-denominator bookkeeping.
