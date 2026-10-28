# Security model

ObligationSeal assesses documentary facts against locked technical criteria. It does not establish contract formation, legal enforceability, publisher identity, actual delivery, test execution, or complete disclosure. It never transfers funds. Synthetic examples are not real customer records.

## Trust boundary

An agreement author selects 1–4 trusted GitHub repositories at immutable registration. Only that account can submit or evaluate its delivery packages. Anyone can independently register a different agreement, but cannot change an existing agreement or consume another owner's retries. Agreement identity binds domain, chain, contract, registering account and full agreement. Clients must select the intended agreement ID and inspect its author; similar titles or references are not unique global identities.

A SHA-256 match authenticates bytes against a commitment. Git commit pinning and an allowed repository constrain publication location, not the human author's identity or honesty. A dishonest trusted publisher can manufacture mutually consistent documents. No cryptographic publisher signatures or Git signature verification are claimed. Private evidence is unsupported; all contract inputs and public documents must be suitable for disclosure.

## Evidence retrieval

Only HTTPS raw.githubusercontent.com URLs with an allowed owner/repository, full lower-case 40-hex Git commit and restricted path segments are accepted. Branches, tags, other hosts, credentials, ports, query strings, percent encoding, empty segments and traversal are rejected. Documents cannot introduce more fetch targets. Response status must be exactly 200; exact bytes and SHA-256 must match before strict UTF-8 parsing. Every document envelope must bind the locked agreement reference/version and submitted delivery/role.

Resource limits: agreement 14,000 UTF-8 bytes, 1–8 requirements, up to four roles per requirement, three criteria fields up to 800 bytes each, package 6,000 bytes, 1–4 documents, 12,000 bytes per response commitment and 32,000 total, model output 16,000 bytes, reason 600 bytes, eight citations per row, 500 bytes per quote. One local model repair; three committed attempts per package. JSON duplicate keys and nonfinite constants are rejected. No consensus side effects occur inside nondeterministic closures.

The pinned SDK has no caller-configurable streaming download bound, timeout or redirect policy. Bounds are checked after the host returns a response, so host fetch restrictions and resource controls remain part of the trusted GenVM platform. The contract cannot prevent host-level oversized transfer before checking length. It does not use a general browser renderer or execute remote content.

## AI and Equivalence Principle

All evidence and agreement prose is marked untrusted data. The system instruction forbids obeying document prompts, using external knowledge or letting a blanket acceptance override failed tests. Strict shape, row identity/order, allowed states, literal quotes and evidence-role coverage are enforced in code. Missing evidence never independently proves violation. A validator fetches and authenticates independently, generates its own assessment without the leader answer, checks every stable requirement state, revalidates leader citations, then semantically judges both audits against sources and criteria. Disagreement or invalid judge output rejects consensus.

These controls reduce attack surface but do not guarantee prompt-injection immunity or eliminate correlated model errors. The semantic meaning of a quote and whether a criterion is met remain AI judgments. Do not describe mocked adversarial tests as empirical live-model security certification. Requirements should be narrow, objective and mutually consistent. Carefully define affirmative violation criteria; a poorly written criterion can cause poor judgments.

## History and availability

Decision hashes bind request, agreement, package, attempt, previous hash and full result. Storage methods only append receipts and advance a head; conclusive decisions cannot be reassessed. Consensus failures revert instead of fabricating an INCONCLUSIVE receipt or spending a committed attempt. INCONCLUSIVE results may retry the same evidence only, with all earlier receipts retained. A new package creates a new request and cannot replace the old request; consumers must not let a submitter cherry-pick away prior breaches.

Confirmed affirmative violations dominate unknown requirements only after all submitted artifacts pass integrity and identity checks. Failed authentication yields INCONCLUSIVE for the whole package. Refusal to finalize, unavailable repositories, inconsistent validators and hosted-network resets are availability risks. Wait for FINALIZED with successful execution, not merely ACCEPTED.

## Reporting

Report vulnerabilities privately to the repository maintainer through GitHub's private vulnerability reporting if enabled. Otherwise open an issue requesting a private contact channel without disclosing exploit details or sensitive evidence. Never submit secrets in test fixtures.
