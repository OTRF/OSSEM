# Audit Directory Service Replication

Audit Directory Service Replication determines whether the operating system generates audit events when replication between two domain controllers begins and ends.

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-directory-service-replication)

## Data Dictionaries

| EventId | Description | Minimum OS |
|--------|---------|-------|
| [4932](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4932.md) | Synchronization of a replica of an Active Directory naming context has begun | Windows Vista, Windows Server 2008 |
| [4933](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4933.md) | Synchronization of a replica of an Active Directory naming context has ended | Windows Vista, Windows Server 2008 |