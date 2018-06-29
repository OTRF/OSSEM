# Audit Other Object Access Events

Audit Other Object Access Events allows you to monitor operations with scheduled tasks, COM+ objects and indirect object access requests.

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-other-object-access-events)

## Data Dictionaries

| EventId | Description | Minimum OS |
|--------|---------|-------|
| 4671 | An application attempted to access a blocked ordinal through the TBS. |  |
| 4691 | Indirect access to an object was requested. |  |
| 5148 | The Windows Filtering Platform has detected a DoS attack and entered a defensive mode; packets associated with this attack will be discarded. |  |
| 5149 | The DoS attack has subsided and normal processing is being resumed. |  |
| 4698 | A scheduled task was created. |  |
| 4699 | A scheduled task was deleted. |  |
| 4700 | A scheduled task was enabled. |  |
| 4701 | A scheduled task was disabled. |  |
| 4702 | A scheduled task was updated. |  |
| 5888 | An object in the COM+ Catalog was modified. |  |
| 5889 | An object was deleted from the COM+ Catalog. |  |
| 5890 | An object was added to the COM+ Catalog. |  |