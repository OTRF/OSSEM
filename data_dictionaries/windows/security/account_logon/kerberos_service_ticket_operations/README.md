# Audit Kerberos Service Ticket Operations

Events are generated every time Kerberos is used to authenticate a user who wants to access a protected network resource. Kerberos service ticket operation audit events can be used to track user activity.

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-kerberos-service-ticket-operations)

## Data Dictionaries

| EventId | Description | Minimum OS |
|--------|---------|-------|
| 4769 | A Kerberos service ticket was requested | Windows Vista, Windows Server 2008 |
| 4770 | A Kerberos service ticket was renewed | Windows Vista, Windows Server 2008 |
| 4773 | A Kerberos service ticket request failed | Windows Vista, Windows Server 2008 |