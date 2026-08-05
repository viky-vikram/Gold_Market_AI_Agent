# Threat model: <component or feature>

- **Status:** Draft | Reviewed | Accepted
- **Date:** YYYY-MM-DD
- **Author / reviewer:**
- **Task:** GMAA-XXX
- **Scope:** What is in scope, and explicitly what is not.

## Assets

What is worth protecting here? User data, credentials, quota integrity, market-data licence
compliance, model budget, audit trail.

## Trust boundaries

Where does data cross from less-trusted to more-trusted? Note every point where untrusted input
enters — user free text, retrieved news and web content, provider payloads, model output.

| Boundary | From | To  | Controls |
| -------- | ---- | --- | -------- |
|          |      |     |          |

## Threats (STRIDE)

| #   | Threat | Category | Likelihood | Impact | Mitigation | Test ID |
| --- | ------ | -------- | ---------- | ------ | ---------- | ------- |
| 1   |        |          |            |        |            |         |

Categories: Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation
of privilege.

## AurumIQ-specific checks

- [ ] Retrieved content treated as untrusted; cannot alter system instructions or tool permissions
- [ ] Tool calls validated against a strict allowlist and typed argument schemas
- [ ] Row Level Security enforced for user-owned data; cross-user access negatively tested
- [ ] No hidden chain-of-thought, credentials, or unredacted sensitive content persisted or displayed
- [ ] Secrets server-side only; never reachable from the browser
- [ ] SSRF protections on any URL retrieval
- [ ] Budget and quota controls cannot be bypassed by retry or concurrency
- [ ] Provider licence terms respected; redistribution gated by capability metadata

## Residual risk

What remains after mitigations, and who accepted it.
