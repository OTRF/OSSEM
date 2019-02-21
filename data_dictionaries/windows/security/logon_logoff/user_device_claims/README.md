# Audit User/Device Claims

Audit User/Device Claims allows you to audit user and device claims information in the account’s logon token. Events in this subcategory are generated on the computer on which a logon session is created. For an interactive logon, the security audit event is generated on the computer that the user logged on to.

For a network logon, such as accessing a shared folder on the network, the security audit event is generated on the computer hosting the resource.

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-user-device-claims)

## Data Dictionaries

| EventId | Description | Minimum OS |
|--------|---------|-------|
| [4626](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4626.md) | User/Device claims information. | Windows 8, Windows Server 2012 |