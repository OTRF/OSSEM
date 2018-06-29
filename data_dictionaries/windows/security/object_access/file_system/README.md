# Audit File System

Audit File System determines whether the operating system generates audit events when users attempt to access file system objects.

Audit events are generated only for objects that have configured system access control lists (SACLs), and only if the type of access requested (such as Write, Read, or Modify) and the account making the request match the settings in the SACL.

If success auditing is enabled, an audit entry is generated each time any account successfully accesses a file system object that has a matching SACL. If failure auditing is enabled, an audit entry is generated each time any user unsuccessfully attempts to access a file system object that has a matching SACL.

These events are essential for tracking activity for file objects that are sensitive or valuable and require extra monitoring.

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-file-system)

## Data Dictionaries

| EventId | Description | Minimum OS |
|--------|---------|-------|
| 4656 | A handle to an object was requested. | Windows Vista, Windows Server 2008 |
| 4658 | The handle to an object was closed. | Windows Vista, Windows Server 2008 |
| 4660 | An object was deleted. | Windows Vista, Windows Server 2008 |
| 4663 | An attempt was made to access an object. | Windows Vista, Windows Server 2008 |
| 4664 | An attempt was made to create a hard link. | Windows Vista, Windows Server 2008 |
| 4985 | The state of a transaction has changed. | Windows Vista, Windows Server 2008 |
| 5051 | A file was virtualized. | Windows Vista, Windows Server 2008 |
| 4670 | Permissions on an object were changed. | Windows Vista, Windows Server 2008 |