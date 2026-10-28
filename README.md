# ObligationSeal

**Requirement-level documentary delivery verification for immutable agreements, executed by GenLayer validators.**

Lock an agreement, submit a version-bound delivery package, and seal an evidence-grounded assessment. This is a reusable technical assessment primitive, not a legal judgment, proof of honest authorship, execution of tests, or payment system.

## How it works

1. Any user registers explicit requirements grouped into obligations, acceptance criteria, affirmative violation criteria, required evidence roles and trusted publication repositories. The agreement is immutable and content-addressed.
2. The agreement owner submits immutable delivery, completion, test and acceptance document commitments. Evidence can be incomplete; incompleteness cannot establish breach. A correction is a new package, never an overwrite.
3. Inside real GenVM nondeterministic execution, each node independently retrieves commit-pinned sources and verifies HTTP status, exact raw byte length, SHA-256, UTF-8 and agreement/version/delivery/role binding.
4. Leader and validators independently assess every requirement. Code checks schema, exact quotations and required evidence-role coverage. Validators compare the entire ordered state vector and perform a further source-grounded semantic check of the leader's reasoning and citations.
5. Deterministic code derives obligation and overall outcomes and appends a canonical JSON hash-linked receipt. A conclusive request seals; an inconclusive request has at most three committed attempts.

| Outcome | Deterministic rule after successful document authentication |
|---|---|
| BREACHED | At least one requirement has cited affirmative VIOLATED evidence |
| INCONCLUSIVE | No violation, but at least one UNKNOWN requirement |
| PARTIALLY_FULFILLED | No violation or unknown; at least one affirmative PARTIAL requirement |
| FULFILLED | Every requirement SATISFIED, with every required evidence role cited |

Retrieval, integrity, identity-binding and invalid-model failures always produce INCONCLUSIVE, with a machine-readable error. A confirmed violation can establish a localized breach even if other requirements remain unknown; it never certifies those other requirements. Each obligation is derived separately with the same precedence. Partial means evidenced completion of a subset with an explicitly incomplete remainder; a missing document alone means UNKNOWN.

## Interface

| Method | Purpose |
|---|---|
| `register_agreement(agreement_json) -> str` | Lock agreement and return its domain-bound hash |
| `submit_delivery(agreement_id, package_json) -> str` | Owner-only content-addressed submission |
| `evaluate(request_id) -> str` | Owner-only real nondeterministic consensus; returns decision hash |
| `get_agreement(agreement_id) -> str` | Read immutable criteria and registered owner |
| `get_request(request_id) -> str` | Read package, status, attempt count and history head |
| `get_decision(request_id, attempt) -> str` | Read an immutable decision and hash |

No administrator, upgrades, global user quota, tokens, escrow or wallet integrations. Agreement owner means the registering account; registration does not establish consent or legal identity. Consumers must authenticate the agreement ID and owner they intend to rely on.

## Reproduce

Python 3.12+:

```sh
python -m pip install -r requirements-dev.txt
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -p gltest.direct.pytest_plugin -q tests
genvm-lint check contracts/obligation_seal.py --json
genvm-lint schema contracts/obligation_seal.py --json
python scripts/verify_live.py
```

The 59 direct-mode tests use the actual official v0.2.16 SDK with mocked web and AI I/O. They explicitly run validator functions and test manipulated leaders, fingerprints, wrong versions, missing evidence, citation forgery, authorization, sealing, isolation and retries. They do not demonstrate LLM robustness or live consensus by themselves. See the separate [live deployment record](docs/DEPLOYMENT.md).

Start with [examples/agreement.json](examples/agreement.json) and [examples/breached.json](examples/breached.json). The demo is explicitly synthetic: the correct software release is delivered but two regression tests fail. Four additional packages demonstrate fulfillment, partial completion, absent results and an injection-bearing acceptance document.

[Security](SECURITY.md) · [Evidence protocol](docs/EVIDENCE.md) · [Deployment](docs/DEPLOYMENT.md) · [Submission](docs/SUBMISSION.md) · [Official references and architecture review](docs/REFERENCES.md)

MIT licensed.
