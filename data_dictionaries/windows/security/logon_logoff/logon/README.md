# Audit Logon

Audit Logon determines whether the operating system generates audit events when a user attempts to log on to a computer.

These events are related to the creation of logon sessions and occur on the computer that was accessed. For an interactive logon, events are generated on the computer that was logged on to. For a network logon, such as accessing a share, events are generated on the computer that hosts the resource that was accessed.

The following events are recorded:

* Logon success and failure.
* Logon attempts by using explicit credentials. This event is generated when a process attempts to log on an account by explicitly specifying that account's credentials. This most commonly occurs in batch configurations such as scheduled tasks, or when using the RunAs command.
* Security identifiers (SIDs) are filtered.

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-logon)

## Data Dictionaries

| EventId | Description | Minimum OS |
|--------|---------|-------|
| [4624](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4624.md) | An account was successfully logged on. | Windows Vista, Windows Server 2008 |
| [4625](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4625.md) | An account failed to log on. | Windows Vista, Windows Server 2008 |
| [4648](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4648.md) | A logon was attempted using explicit credentials. | Windows Vista, Windows Server 2008 |
| 4675 | SIDs were filtered. | Windows Vista, Windows Server 2008 |