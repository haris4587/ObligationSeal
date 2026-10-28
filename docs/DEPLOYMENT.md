# Confirmed Studionet deployment

Network: stable GenLayer Studionet, chain ID **61999**, RPC `https://studio.genlayer.com/api`. Deployment and all three writes used Studio's built-in account, **Normal (Full Consensus)**, simulation off. No wallet-connect, external wallet, payment or token deployment was used. One instance was deployed; no source upgrade was performed.

- Contract: [0x65467a491Fac9eDd5dc603699c8E7B817BCd63A5](https://explorer-studio.genlayer.com/address/0x65467a491Fac9eDd5dc603699c8E7B817BCd63A5)
- Sender: `0x647C6E2B4C62edFc774613d8B53d5f32e67edFFc`
- Source and fixture commit: [`cd16b38661980a20ec678cb5f8f5d39691dc4bef`](https://github.com/haris4587/ObligationSeal/commit/cd16b38661980a20ec678cb5f8f5d39691dc4bef)
- Source SHA-256: `a066225f9713d8fba67680530cdd043c349be1ca0473be95df23e12b094e5457`

The final documentation commit retains this exact source. Its SHA is provided in the final delivery and can always be resolved from GitHub main. A commit cannot contain its own SHA without a self-reference; the stable source/fixture commit above anchors reproducibility independently of later documentation-only commits.

| Operation | Finalized transaction |
|---|---|
| Deploy | [0x3d856ba97963080deef86405b1d276a1b021ec3652428e0d9a90e9e67e3ecc2f](https://explorer-studio.genlayer.com/tx/0x3d856ba97963080deef86405b1d276a1b021ec3652428e0d9a90e9e67e3ecc2f) |
| Register agreement | [0xb298e7f2de5dcb5a5a81deb4342dc100aac7c82453bad3b65734c2ed0ad701a7](https://explorer-studio.genlayer.com/tx/0xb298e7f2de5dcb5a5a81deb4342dc100aac7c82453bad3b65734c2ed0ad701a7) |
| Submit delivery | [0xe660371490033223a5f1937978ace0a27bcee16f14c79e8193f01cff9b4d6b52](https://explorer-studio.genlayer.com/tx/0xe660371490033223a5f1937978ace0a27bcee16f14c79e8193f01cff9b4d6b52) |
| Full Consensus evaluate | [0xfc94b3505dacb18322d77c4c36c5ebb6db3e6c7cc0200c65d81dc6dd38ae7cf5](https://explorer-studio.genlayer.com/tx/0xfc94b3505dacb18322d77c4c36c5ebb6db3e6c7cc0200c65d81dc6dd38ae7cf5) |

## Meaningful consensus result

Finalized result: **BREACHED**. Requirement R1 SATISFIED / obligation O1 FULFILLED: delivery and completion both identify release 1.2.0 and the CSV export module. Requirement R2 VIOLATED / obligation O2 BREACHED: the test record affirmatively reports **10 passed, 2 failed, 12 total**, including two named failures. The breach comes from those failures, not the withheld acceptance document.

- Agreement ID: `f407b8740f3758237a5b6589bfdd0cb9bc024a6a937d97d9648bcd17ddf12e53`
- Request ID: `230056ba65a5e65dcfb179f0298dfd657eae4d625c4616884cbfcebf92fcd05d`
- Package hash: `13798c89cda7cc19f77603c4f7dd5ea7bcfa5620ec5b1f5d397d707d6ad06bca`
- Attempt: 1; previous hash: empty.
- Decision hash: `11647703d946593f83f1e3f039fcd5e9d330d7d9ec2bad0c8ea9d0650f117457`

RPC and Explorer confirm FINALIZED, successful execution and `leader_only: false`; consensus result is `MAJORITY_AGREE`. Evaluation records three agree votes and two idle validators cancelled with `CONSENSUS_VALIDATOR_QUORUM_REACHED`. Idle cancellations are not reported as five completed AI audits. Successful leader and validator receipts include real nondeterministic outputs and AI execution statistics.

## Verification materials

- [Machine-readable summary](../evidence/live-summary.json)
- [Read-only verification script](../scripts/verify_live.py)
- [Verification report](../evidence/verification.json) and [console result](../evidence/live-verification.txt)
- [Exact deployed source](../evidence/deployed-source.py)
- [Finalized agreement](../evidence/finalized-agreement.json), [request](../evidence/finalized-request.json), [decision](../evidence/decision-1.json)
- [Studio screenshot](../evidence/studio-finalized.jpg)
- Transaction snapshots: [deploy](../evidence/deploy-transaction.json), [register](../evidence/register-transaction.json), [submit](../evidence/submit-transaction.json), [evaluate](../evidence/evaluate-transaction.json).

Run `python scripts/verify_live.py`. The script only reads public state; it verifies finalized majority consensus, successful agree receipts, source equality with the GitHub source commit, all content hashes and literal quotes. Hosted Studionet may reset; committed snapshots remain evidence of observed execution, not a promise of permanent network availability.

## Deploy another instance

1. Install pinned dev requirements and run tests, lint and schema commands in README.
2. Open stable Studio, import `contracts/obligation_seal.py`, select Normal (Full Consensus), deploy with no constructor arguments using its built-in account.
3. Call `register_agreement` with `examples/agreement.json`. The returned ID varies by contract/account/chain; use the actual returned ID, not this deployment's ID.
4. Call `submit_delivery` with that ID and one package from `examples`. The returned request ID binds the registered agreement and package.
5. Call `evaluate` with the returned request ID. Keep simulation off. Wait for FINALIZED and inspect successful execution plus consensus receipt.
6. Select Finalized state and read `get_request` and `get_decision(request_id,1)`. Independently verify the source and canonical hashes before relying on results.
