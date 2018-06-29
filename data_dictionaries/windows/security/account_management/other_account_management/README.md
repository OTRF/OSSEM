# Audit Other Account Management Events

Audit Other Account Management Events determines whether the operating system generates user account management audit events

This subcategory allows you to audit next events:

* The password hash of a user account was accessed. This happens during an Active Directory Management Tool password migration.
* The Password Policy Checking API was called. Password Policy Checking API allows an application to check password compliance against an application-provided account database or single account and verify that passwords meet the complexity, aging, minimum length, and history reuse requirements of a password policy.

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-other-account-management-events)

## Data Dictionaries

| EventId | Description | Minimum OS |
|--------|---------|-------|
| [4782](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4782.md) | The password hash an account was accessed. | Windows Vista, Windows Server 2008 |
| [4793](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4793.md) | The Password Policy Checking API was called. | Windows Vista, Windows Server 2008 |