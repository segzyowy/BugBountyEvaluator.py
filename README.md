# GenLayer Intelligent Bug Bounty Triage Oracle

An on-chain Intelligent Contract deployed on GenLayer Testnet that uses decentralized LLM consensus to automatically triage vulnerability reports and determine bug severity for security bounties.

## Overview
Traditional bug bounty programs suffer from slow manual review queues and subjective triage. This contract provides transparent, decentralized validation of vulnerability reports using GenLayer's Optimistic Democracy.

## Features
- **Decentralized AI Triage:** Evaluates vulnerability reports using `gl.nondet.exec_prompt` and `gl.eq_principle.strict_eq`.
- **Severity Classification:** Assesses attack vectors and recommends payout allocations based on reproducibility.
- **On-Chain Audit Records:** Stores report outcomes in native GenVM `TreeMap` storage.

## Functions
- `submit_bug_report(researcher_handle, target_component, vulnerability_summary, reproduction_steps)`: Write method submitting report for validator consensus evaluation.
- `get_report(report_id)`: View method returning the triage analysis and severity.
- `get_stats()`: View method returning total processed and validated bounties.

## Deployment Details
- **Network:** GenLayer Testnet
- **Contract Address:** `0x5B70BE3EBBe90373f6DDcdcd72807b3C6FD0CFb3`
- **Explorer:** [View on GenLayer Studio Explorer](https://explorer-studio.genlayer.com/address/0x5B70BE3EBBe90373f6DDcdcd72807b3C6FD0CFb3)
- **Runtime:** Python (GenVM)
- **Status:** Finalized
