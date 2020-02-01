# Audit Other Logon/Logoff Events

Audit Other Logon/Logoff Events determines whether Windows generates audit events for other logon or logoff events.

These other logon or logoff events include:

* A Remote Desktop session connects or disconnects.
* A workstation is locked or unlocked.
* A screen saver is invoked or dismissed.
* A replay attack is detected. This event indicates that a Kerberos request was received twice with identical information. This condition could also be caused by network misconfiguration.
* A user is granted access to a wireless network. It can be either a user account or the computer account.
* A user is granted access to a wired 802.1x network. It can be either a user account or the computer account.

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-other-logonlogoff-events)

## Data Dictionaries

| EventId | Description | Minimum OS |
|--------|---------|-------|
| [4649](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4649.md) | A replay attack was detected | Windows Vista, Windows Server 2008 |
| [4778](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4778.md) | A session was reconnected to a Window Station. | Windows Vista, Windows Server 2008 |
| [4779](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4779.md) | A session was disconnected from a Window Station. | Windows Vista, Windows Server 2008 |
| [4800](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4800.md) | The workstation was locked. | Windows Vista, Windows Server 2008 |
| [4801](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4801.md) | The workstation was unlocked. | Windows Vista, Windows Server 2008 |
| [4802](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4802.md) | The screen saver was invoked. | Windows Vista, Windows Server 2008 |
| [4803](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4803.md) | The screen saver was dismissed. | Windows Vista, Windows Server 2008 |
| [4825](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4825.md) | A user was denied the access to Remote Desktop. | Windows Vista SP2, Windows Server 2008 SP2 |
| [5378](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-5378.md) | The requested credentials delegation was disallowed by policy. | Windows Vista, Windows Server 2008|
| [5632](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-5632.md) | A request was made to authenticate to a wireless network. | Windows Vista, Windows Server 2008 |
| [5633](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-5633.md) | A request was made to authenticate to a wired network. | Windows Vista, Windows Server 2008 |