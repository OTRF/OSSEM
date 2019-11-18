# Audit Registry

Audit Registry allows you to audit attempts to access registry objects. A security audit event is generated only for objects that have system access control lists (SACLs) specified, and only if the type of access requested, such as Read, Write, or Modify, and the account making the request match the settings in the SACL.

If success auditing is enabled, an audit entry is generated each time any account successfully accesses a registry object that has a matching SACL. If failure auditing is enabled, an audit entry is generated each time any user unsuccessfully attempts to access a registry object that has a matching SACL.

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-registry)

## Data Dictionaries

| EventId | Description | Minimum OS |
|--------|---------|-------|
|[4656](/data_dictionaries/windows/security/events/event-4656.md)| A handle to an object was requested. | Windows Vista, Windows Server 2008 |
|[4658](/data_dictionaries/windows/security/events/event-4658.md)| The handle to an object was closed. | Windows Vista, Windows Server 2008 |
|[4660](/data_dictionaries/windows/security/events/event-4660.md)| An object was deleted. | Windows Vista, Windows Server 2008 |
|[4663](/data_dictionaries/windows/security/events/event-4663.md)| An attempt was made to access an object. | Windows Vista, Windows Server 2008 |
|[4657](/data_dictionaries/windows/security/events/event-4657.md)| A registry value was modified. | Windows Vista, Windows Server 2008 |
| 5039 | A registry key was virtualized. | Windows Vista, Windows Server 2008 |
|[4670](/data_dictionaries/windows/security/events/event-4670.md)| Permissions on an object were changed. | Windows Vista, Windows Server 2008 |