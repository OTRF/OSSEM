# Audit Kernel Object

Audit Kernel Object determines whether the operating system generates audit events when users attempt to access the system kernel, which includes mutexes and semaphores.

Only kernel objects with a matching system access control list (SACL) generate security audit events. The audits generated are usually useful only to developers.

Typically, kernel objects are given SACLs only if the AuditBaseObjects or AuditBaseDirectories auditing options are enabled.

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-kernel-object)

## Data Dictionaries

| EventId | Description | Minimum OS |
|--------|---------|-------|
| 4656 | A handle to an object was requested. | Windows Vista, Windows Server 2008 |
| 4658 | The handle to an object was closed. | Windows Vista, Windows Server 2008 |
| 4660 | An object was deleted. | Windows Vista, Windows Server 2008 |