# Audit Group Membership

Audit Group Membership enables you to audit group memberships when they are enumerated on the client computer.

This policy allows you to audit the group membership information in the user's logon token. Events in this subcategory are generated on the computer on which a logon session is created.

For an interactive logon, the security audit event is generated on the computer that the user logged on to. For a network logon, such as accessing a shared folder on the network, the security audit event is generated on the computer hosting the resource.

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-group-membership)

## Data Dictionaries

| EventId | Description | Minimum OS |
|--------|---------|-------|
| 4627 | Group membership information. | Windows Vista, Windows Server 2008 |