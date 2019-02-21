# Audit Detailed File Share

Audit Detailed File Share allows you to audit attempts to access files and folders on a shared folder.

The Detailed File Share setting logs an event every time a file or folder is accessed, whereas the File Share setting only records one event for any connection established between a client and file share. Detailed File Share audit events include detailed information about the permissions or other criteria used to grant or deny access.

There are no system access control lists (SACLs) for shared folders. If this policy setting is enabled, access to all shared files and folders on the system is audited.

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-detailed-file-share)

## Data Dictionaries

| EventId | Description | Minimum OS |
|--------|---------|-------|
| [5145](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-5145.md) | A network share object was checked to see whether client can be granted desired access. | Windows 7, Windows Server 2008 R2 |