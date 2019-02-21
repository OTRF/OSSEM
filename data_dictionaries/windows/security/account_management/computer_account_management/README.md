# Audit Computer Account Management

Audit Computer Account Management determines whether the operating system generates audit events when a computer account is created, changed, or deleted.

This policy setting is useful for tracking account-related changes to computers that are members of a domain

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-computer-account-management)

## Data Dictionaries

| EventId | Description | Minimum OS |
|--------|---------|-------|
| 4741 | A computer account was created | Windows Vista, Windows Server 2008 |
| [4742](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4742.md) | A computer account was changed | Windows Vista, Windows Server 2008 |
| [4743](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4743.md) | A computer account was deleted | Windows Vista, Windows Server 2008 |