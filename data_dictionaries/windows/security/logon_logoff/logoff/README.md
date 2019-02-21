# Audit Logoff

Audit Logoff determines whether the operating system generates audit events when logon sessions are terminated.

These events occur on the computer that was accessed. In the case of an interactive logon, these events are generated on the computer that was logged on to.

There is no failure event in this subcategory because failed logoffs (such as when a system abruptly shuts down) do not generate an audit record.

Logon events are essential to understanding user activity and detecting potential attacks. Logoff events are not 100 percent reliable. For example, the computer can be turned off without a proper logoff and shutdown; in this case, a logoff event is not generated.

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-logoff)

## Data Dictionaries

| EventId | Description | Minimum OS |
|--------|---------|-------|
| [4634](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4634.md) | An account was logged off. | Windows Vista, Windows Server 2008 |
| [4647](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4647.md) | User initiated logoff. | Windows Vista, Windows Server 2008 |