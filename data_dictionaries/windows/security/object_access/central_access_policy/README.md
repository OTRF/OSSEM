# Audit Central Access Policy Staging

Audit Central Access Policy Staging allows you to audit access requests where a permission granted or denied by a proposed policy differs from the current central access policy on an object.

If you configure this policy setting, an audit event is generated each time a user accesses an object and the permission granted by the current central access policy on the object differs from that granted by the proposed policy. The resulting audit event is generated as follows:

* Success audits, when configured, record access attempts when the current central access policy grants access, but the proposed policy denies access.
* Failure audits, when configured, record access attempts when:
  * The current central access policy does not grant access, but the proposed policy grants access.
  * A principal requests the maximum access rights they are allowed and the access rights granted by the current central access policy are different than the access rights granted by the proposed policy.

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-central-access-policy-staging)

## Data Dictionaries

| EventId | Description | Minimum OS |
|--------|---------|-------|
| 4818 | Proposed Central Access Policy does not grant the same access permissions as the current Central Access Policy. |  |