# Audit Directory Service Changes

Audit Directory Service Changes determines whether the operating system generates audit events when changes are made to objects in Active Directory Domain Services (AD DS).

Auditing of directory service objects can provide information about the old and new properties of the objects that were changed.

Audit events are generated only for objects with configured system access control lists (SACLs), and only when they are accessed in a manner that matches their SACL settings. Some objects and properties do not cause audit events to be generated due to settings on the object class in the schema.

This subcategory only logs events on domain controllers.

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-directory-service-changes)

## Data Dictionaries

| EventId | Description | Minimum OS |
|--------|---------|-------|
| [5136](data_dictionaries/windows/security/events/event-5136.md) | A directory service object was modified | Windows Vista, Windows Server 2008 |
| [5137](data_dictionaries/windows/security/events/event-5137.md) | A directory service object was created | Windows Vista, Windows Server 2008 |
| [5138](data_dictionaries/windows/security/events/event-5138.md) | A directory service object was undeleted | Windows Vista, Windows Server 2008 |
| [5139](data_dictionaries/windows/security/events/event-5139.md) | A directory service object was moved | Windows Vista, Windows Server 2008 |
| [5141](data_dictionaries/windows/security/events/event-5141.md) | A directory service object was deleted | Windows Vista, Windows Server 2008 |