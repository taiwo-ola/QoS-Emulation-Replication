# Replication Package: Emulation-Based Performance Evaluation of CBWFQ and LLQ Under Severe Network Overload

This repository contains the complete experimental artifacts, Cisco IOS MQC configurations, aggregated $N = 30$ statistical datasets, and Python visualization scripts supporting the research manuscript evaluating Class-Based Weighted Fair Queuing (CBWFQ) and Low-Latency Queuing (LLQ).

## Directory Structure
- `/configs`: Contains the hierarchical Cisco IOS Modular QoS CLI (MQC) configurations (`SHAPE-WITH-OSPF`, `CBWFQ_POLICY`, and `LLQ_POLICY`) applied on core router R1.
- `/data`: Contains the aggregated $N = 30$ independent experimental run statistics (Means, Standard Deviations, and 95% Confidence Intervals) matching Tables 1, 2, and 3.
- `/scripts`: Contains the Python script (`generate_figures.py`) used to generate Figures 1 through 6.

## Software Requirements
- **GNS3** (Version 2.2.x) with Dynamips hypervisor engine[cite: 3].
- **Cisco IOS c7200** image (`c7200-adventerprisek9-mz.152-4.S6.bin`)[cite: 3].
- **iPerf3** for synthetic multi-class traffic generation[cite: 3].
- **Python 3.x** with `matplotlib` and `numpy` libraries for data plotting.