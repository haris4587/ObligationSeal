# GenLayer Intelligent Contracts submission

**Title:** ObligationSeal

**One-line description:** A reusable GenLayer Intelligent Contract that verifies immutable agreement obligations against authenticated, version-bound documentary delivery evidence.

**Notes / Description (under 1,000 characters):**

ObligationSeal locks explicit obligations, requirement-level acceptance and affirmative violation criteria, and trusted evidence repositories. Delivery packages commit full Git SHAs, SHA-256 and exact byte lengths. GenLayer leader and validators independently retrieve and authenticate version-bound delivery, completion, test and acceptance documents, assess every requirement, and validate grounded quotations. Deterministic rules derive FULFILLED, PARTIALLY_FULFILLED, BREACHED or INCONCLUSIVE; missing documents never establish breach. Canonical JSON, domain-bound IDs and append-only decision hashes make results reproducible. Includes authorization, isolated requests, bounded retries, injection defenses, synthetic examples and 59 SDK tests. Deployed on Studionet: real Full Consensus finalized BREACHED from two documented test failures. Technical evidence assessment only; no legal judgment, tokens, escrow or payments.

## Links and checks

- Repository: https://github.com/haris4587/ObligationSeal
- Contract: https://explorer-studio.genlayer.com/address/0x65467a491Fac9eDd5dc603699c8E7B817BCd63A5
- Deployment: https://explorer-studio.genlayer.com/tx/0x3d856ba97963080deef86405b1d276a1b021ec3652428e0d9a90e9e67e3ecc2f
- Full Consensus: https://explorer-studio.genlayer.com/tx/0xfc94b3505dacb18322d77c4c36c5ebb6db3e6c7cc0200c65d81dc6dd38ae7cf5
- [All transaction, source-match and evidence verification](DEPLOYMENT.md)
- [SHA-256, source URLs and byte lengths](../examples/breached.json)
- [Decision with grounded quotations](../evidence/decision-1.json)
- [59 passing official SDK direct tests](../evidence/unit-tests.txt)
- [GenVM lint and actual SDK validation](../evidence/genvm-check.json)
- [Extracted schema](../evidence/schema.json)
- [Security and limitations](../SECURITY.md)

Source SHA-256: `a066225f9713d8fba67680530cdd043c349be1ca0473be95df23e12b094e5457`

Decision hash: `11647703d946593f83f1e3f039fcd5e9d330d7d9ec2bad0c8ea9d0650f117457`

Exact source/fixture commit: `cd16b38661980a20ec678cb5f8f5d39691dc4bef`. The final delivery separately reports the final documentation commit SHA, whose contract source is byte-identical.
