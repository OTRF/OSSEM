# Audit Authorization Policy Change

Audit Authorization Policy Change allows you to audit assignment and removal of user rights in user right policies, changes in security token object permission, resource attributes changes and Central Access Policy changes for file system objects.

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-authorization-policy-change)

## Data Dictionaries

| EventId | Description | Minimum OS |
|--------|---------|-------|
| 4670 | Permissions on an object were changed. | Windows 8, Windows Server 2012 |
| 4703 | A user right was adjusted. | Windows 10 |
| 4704 | A user right was assigned. | Windows Vista, Windows Server 2008 |
| 4705 | A user right was removed. | Windows Vista, Windows Server 2008 |
| 4911 | Resource attributes of the object were changed. | Windows 8, Windows Server 2012 |
| 4913 | Central Access Policy on the object was changed. | Windows 8, Windows Server 2012 |