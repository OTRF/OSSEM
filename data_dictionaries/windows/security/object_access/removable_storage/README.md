# Audit Removable Storage

Audit Removable Storage allows you to audit user attempts to access file system objects on a removable storage device. A security audit event is generated for all objects and all types of access requested, with no dependency on object’s SACL.

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-removable-storage)

## Data Dictionaries

| EventId | Description | Minimum OS |
|--------|---------|-------|
| 4656 | A handle to an object was requested. | Windows Vista, Windows Server 2008 |
| 4658 | The handle to an object was closed. | Windows Vista, Windows Server 2008 |
| 4663 | An attempt was made to access an object. | Windows Vista, Windows Server 2008 |