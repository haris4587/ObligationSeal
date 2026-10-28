# Official references and design provenance

Checked 2026-10-28:

- https://docs.genlayer.com/developers/intelligent-contracts/equivalence-principle — independent source-based validator verification and `run_nondet_unsafe`.
- https://docs.genlayer.com/developers/intelligent-contracts/features/non-determinism — all web and LLM operations inside nondeterministic execution, with storage copied first.
- https://docs.genlayer.com/developers/intelligent-contracts/features/calling-llms — JSON response format; defensive parsing. The equivalence documentation's independent-verification security requirements take precedence over shape-only illustrative snippets.
- https://docs.genlayer.com/developers/intelligent-contracts/features/web-access — direct raw-byte requests.
- https://docs.genlayer.com/developers/intelligent-contracts/security-and-best-practices/prompt-injection — treat evidence as untrusted data.
- https://docs.genlayer.com/api-references/genlayer-linter — lint, actual SDK validation and schema extraction.
- https://docs.genlayer.com/developers/intelligent-contracts/tools/genlayer-studio — stable Studionet, built-in accounts and Full Consensus.

Pinned SDK: `py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6`, official GenVM v0.2.16. This matches the stable Studio example's runner. Linter 0.11.0 reports informational I200 (a newer runner exists), not a validation failure. Retaining the known compatible runner is intentional. Host client `genlayer-py==0.16.3`; testing `genlayer-test==0.29.2`. Actual SDK exposes `Response.status` and raw `body` bytes; no unsupported `status_code` field or invented fetch options are used.

## Related repositories reviewed

- https://github.com/haris4587/RemedySeal — locked vulnerability remediation and requirement closure.
- https://github.com/haris4587/DataUseSeal — immutable policies, independently evaluated proposed-use packages.
- https://github.com/haris4587/LineageSeal — publisher trust boundary, literal citation checks and semantic validator judgment.
- https://github.com/haris4587/RootCauseSeal — evidence fingerprinting, immutable case registration and hash-linked decisions.

ObligationSeal uses the same native GenVM architecture and explicit security boundaries, but defines a distinct primitive: reusable agreement registration plus separately committed delivery packages, requirement-to-obligation aggregation, four documentary delivery roles, deterministic identity envelopes, explicit affirmative violation criteria, partial completion distinct from unknown evidence, and breach precedence that never treats missing documentation as violation. It does not relabel a remediation, provenance, incident or data-usage judgment.
