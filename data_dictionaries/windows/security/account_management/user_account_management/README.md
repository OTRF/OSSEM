# Audit User Account Management

Audit User Account Management determines whether the operating system generates audit events when specific user account management tasks are performed.

This policy setting allows you to audit changes to user accounts. Events include the following:

* A user account is created, changed, deleted, renamed, disabled, enabled, locked out or unlocked.
* A user account’s password is set or changed.
* A security identifier (SID) is added to the SID History of a user account, or fails to be added.
* The Directory Services Restore Mode password is configured.
* Permissions on administrative user accounts are changed.
* A user's local group membership was enumerated.
* Credential Manager credentials are backed up or restored.

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-user-account-management)

## Data Dictionaries

| EventId | Description | Minimum OS |
|--------|---------|-------|
| [4720](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4720.md) | A user account was created. | Windows Vista, Windows Server 2008 |
| [4722](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4722.md) | A user account was enabled. | Windows Vista, Windows Server 2008 |
| [4723](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4723.md) | An attempt was made to change an account's password. | Windows Vista, Windows Server 2008 |
| [4724](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4724.md) | An attempt was made to reset an account's password. | Windows Vista, Windows Server 2008 |
| [4725](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4725.md) | A user account was disabled. | Windows Vista, Windows Server 2008 |
| [4726](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4726.md) | A user account was deleted. | Windows Vista, Windows Server 2008 |
| [4738](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4738.md) | A user account was changed. | Windows Vista, Windows Server 2008 |
| [4740](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4740.md) | A user account was locked out. | Windows Vista, Windows Server 2008 |
| 4765 | SID History was added to an account. | Windows Vista, Windows Server 2008 |
| 4766 | An attempt to add SID History to an account failed. | Windows Vista, Windows Server 2008 |
| [4767](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4767.md) | A user account was unlocked. | Windows Vista, Windows Server 2008 |
| 4780 | The ACL was set on accounts which are members of administrators groups. | Windows Vista, Windows Server 2008 |
| [4781](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4781.md) | The name of an account was changed: | Windows Vista, Windows Server 2008 |
| [4794](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4794.md) | An attempt was made to set the Directory Services Restore Mode. | Windows Vista, Windows Server 2008 |
| 4797 | An attempt was made to query the existence of a blank password for an account. | Windows 8, Windows Server 2012 |
| [4798](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4798.md) | A user's local group membership was enumerated. | Windows 10 |
| [5376](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-5376.md) | Credential Manager credentials were backed up. | Windows Vista, Windows Server 2008 |
| [5377](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-5377.md) | Credential Manager credentials were restored from a backup. | Windows Vista, Windows Server 2008 |
| [5378](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-5378.md) | The requested credentials delegation was disallowed by policy | Windows 10, Windows Server 2016 |
| [5379](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-5379.md) | Credential Manager credentials were read | Windows 10, Windows Server 2016 |