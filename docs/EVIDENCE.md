# Evidence protocol and reproducibility

An agreement defines reference, immutable version, title, publisher repository allowlist, and 1–8 ordered requirement objects. Each requirement has globally unique `id`, grouping `obligation`, `description`, `acceptance`, affirmative `violation` criterion and nonempty `roles` drawn from delivery/completion/test/acceptance. All fields are mandatory. A new agreement is required to change any criterion or trust source.

A delivery package contains `delivery_id` and an ordered `evidence` array. Each role occurs at most once. Each entry commits `role`, `url`, `sha256`, `bytes`. One to four sources are allowed so missing evidence remains assessable as unknown. SATISFIED requires citations from every required role; PARTIAL and VIOLATED require a relevant required role, and independent semantic validation.

Each fetched file is a UTF-8 JSON object containing exactly:

```json
{"reference":"OS-DEMO-2026","version":"1","delivery_id":"D-001","role":"test","content":"Human-readable documentary record"}
```

SHA-256 and byte length cover the entire file, including JSON formatting and trailing newline. Citation strings refer to exact contiguous substrings of decoded `content`, not JSON escape sequences or external URLs. Citation `source` is a zero-based evidence index. Full source URL, digest, role and size are in the immutable package; together they resolve every citation. Envelopes establish documentary binding, not legal identity or truthfulness.

## Content addressing

Canonicalization is Python JSON with sorted keys, separators `,`/`:`, `ensure_ascii=True`, `allow_nan=False`, UTF-8 encoding. Keys must be unique. Array order is preserved; the format deliberately permits only JSON-compatible bounded input and does not claim RFC 8785 number canonicalization.

- Agreement ID: SHA-256 of canonical `{domain:"ObligationSeal/1/agreement",chain,contract,owner,agreement}`.
- Request ID: SHA-256 of canonical `{domain:"ObligationSeal/1/delivery",agreement_id,package}`. The agreement ID already binds chain, contract and owner.
- Package hash: SHA-256 of canonical package alone.
- Decision hash: SHA-256 of canonical `decision` object **before** adding `decision_hash` to its enclosing receipt.
- Every decision includes request ID, agreement ID, package hash, attempt, previous decision hash and full accepted result. The first `previous` is the empty string. `get_request().head` points to the latest receipt.

## Synthetic scenarios

| Package | Documentary distinction | Intended outcome |
|---|---|---|
| breached | Correct delivery/completion; 10 passed, 2 failed tests; acceptance withheld | BREACHED |
| fulfilled | Correct delivery/completion; 12 passed, 0 failed; final acceptance | FULFILLED |
| partial | Correct delivery; eight passed, four explicitly unexecuted | PARTIALLY_FULFILLED |
| missing | Test results and final acceptance unavailable | INCONCLUSIVE |
| injection | Failed tests plus an administrator-impersonation instruction | BREACHED |

Only the live scenario recorded in DEPLOYMENT is a real consensus result. Other intended outcomes are fixture designs and deterministic/mock test expectations, not reported network executions. The contract does not run the depicted export code or regression suite.

Regenerate text fixtures with `python scripts/build_demo.py`. After publishing them, generate pinned packages with `python scripts/build_demo.py FULL_COMMIT_SHA`. Recompute each fingerprint from raw bytes, never copy a Git blob SHA as a SHA-256. Run `python scripts/verify_live.py` to independently read finalized state, compare source bytes, recompute all addresses/hashes and retrieve every live evidence URL.
