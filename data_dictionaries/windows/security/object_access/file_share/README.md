# Audit File Share

Audit File Share allows you to audit events related to file shares: creation, deletion, modification, and access attempts. Also, it shows failed SMB SPN checks.

There are no system access control lists (SACLs) for shares; therefore, after this setting is enabled, access to all shares on the system will be audited.

Combined with File System auditing, File Share auditing enables you to track what content was accessed, the source (IP address and port) of the request, and the user account that was used for the access.

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-file-share)

## Data Dictionaries

| EventId | Description | Minimum OS |
|--------|---------|-------|
| [5140](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-5140.md) | A network share object was accessed. | Windows Vista, Windows Server 2008 |
| [5142](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-5142.md) | A network share object was added. | Windows 7, Windows Server 2008 R2 |
| [5143](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-5143.md) | A network share object was modified. | Windows 7, Windows Server 2008 R2 |
| [5144](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-5144.md) | A network share object was deleted. | Windows 7, Windows Server 2008 R2 |
| [5168](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-5168.md) | Spn check for SMB/SMB2 failed. | Windows 7, Windows Server 2008 R2 |