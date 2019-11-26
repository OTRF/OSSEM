# Audit Authentication Policy Change

Audit Authentication Policy Change determines whether the operating system generates audit events when changes are made to authentication policy.

Changes made to authentication policy include:

* Creation, modification, and removal of forest and domain trusts.
* Changes to Kerberos policy under Computer Configuration\Windows Settings\Security Settings\Account Policies\Kerberos Policy.
* When any of the following user logon rights is granted to a user or group:
  * Access this computer from the network
  * Allow logon locally
  * Allow logon through Remote Desktop
  * Logon as a batch job
  * Logon as a service
* Namespace collision, such as when an added trust collides with an existing namespace name.

This setting is useful for tracking changes in domain-level and forest-level trust and privileges that are granted to user accounts or groups.

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-authentication-policy-change)

## Data Dictionaries

| EventId | Description | Minimum OS |
|--------|---------|-------|
| 4670 | Permissions on an object were changed | Windows Vista, Windows Server 2008 |
| 4706 | A new trust was created to a domain. | Windows Vista, Windows Server 2008 |
| 4707 | A trust to a domain was removed. | Windows Vista, Windows Server 2008 |
| 4713 | Kerberos policy was changed. | Windows Vista, Windows Server 2008 |
| 4716 | Trusted domain information was modified. | Windows Vista, Windows Server 2008 |
|[4717](/data_dictionaries/windows/security/events/event-4717.md)| System security access was granted to an account. | Windows Vista, Windows Server 2008 |
|[4718](/data_dictionaries/windows/security/events/event-4718.md)| System security access was removed from an account. | Windows Vista, Windows Server 2008 |
| 4739 | Domain Policy was changed. | Windows Vista, Windows Server 2008 |
| 4864 | A namespace collision was detected. | Windows Vista, Windows Server 2008 |
| 4865 | A trusted forest information entry was added. | Windows Vista, Windows Server 2008 |
| 4866 | A trusted forest information entry was removed. | Windows Vista, Windows Server 2008 |
| 4867 | A trusted forest information entry was modified. | Windows Vista, Windows Server 2008 |