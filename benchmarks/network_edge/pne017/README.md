# PNE017 Faithful-Reproduction Track

This directory reconstructs the experimental model of PNE017 before any new algorithm is introduced.

## Verified core

The study uses an edge-device collaborative multi-user interactive-VR framework with foreground/background separation, processing queues, a background prediction window, and active removal of expired tiles. Rendering decisions and MEC resource allocation are optimized to minimize sensor-information age and mobile-device power under a motion-to-photon constraint. The proposed method is AQM-CUP, a safe reinforcement-learning method.

A documented public-full-text configuration uses 100 FPS, 10 ms slots, a 20 ms MTP threshold, and an illustrative prediction-window length of five slots.

## Reproduction rule

The implementation remains blocked until the required queue, wireless, compute, objective, state/action, reward/cost and AQM-CUP update equations are directly recovered or transparently reconstructed. No plausible default is accepted as a literature value.

## Purpose

The first executable milestone is reproduction of the source regime, not creation of a new method. Only after source-regime reproduction and baseline verification will controlled benchmark extensions be introduced.
