# Security, Privacy, Identity, Trust, and Interoperability Hypotheses

Status: hypotheses for systematic testing.

## SIH-01 — Interoperability–privacy tension

Cross-platform identity and state portability can improve continuity but may increase linkability and cross-context profiling. Test whether interoperability studies explicitly quantify or model privacy loss caused by stronger identity/state linkage.

## SIH-02 — Portability is often syntactic rather than behavioral

Asset/avatar interoperability may demonstrate format or data transfer without preserving behavior, permissions, provenance, or application semantics. Test preservation dimensions separately.

## SIH-03 — Security evaluation is disconnected from QoE/system overhead

Security/privacy mechanisms may be evaluated by detection/privacy metrics without jointly reporting latency, compute, communication, energy, or XR QoE impact. Test metric co-coverage.

## SIH-04 — Digital-twin freshness and integrity are coupled

A fresh but malicious update and an authentic but stale update can both damage physical-virtual correctness. Test whether studies jointly model timeliness, integrity, provenance, and downstream decision impact.

## SIH-05 — Agent identity/memory portability is an emerging gap

As autonomous/LLM agents become persistent Metaverse actors, safe portability may require identity, capability, memory, authorization, provenance, and policy semantics to migrate together. Search for standards and implemented evidence before treating this as a gap.

## SIH-06 — Cross-domain trust assumptions are hidden

Many methods may assume a single administrative or trust domain. Test whether threat models change when users/assets/services cross operators, worlds, clouds, edge providers, or jurisdictions.

## SIH-07 — Standards-to-experiment gap

Standards and interoperability specifications may define requirements not measured in academic experiments, while academic algorithms may optimize properties absent from standards conformance tests. Build a requirement × experimental-metric matrix.
