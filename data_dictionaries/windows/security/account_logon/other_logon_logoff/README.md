# Audit Other Logon/Logoff Events

These other logon or logoff events include:

* A Remote Desktop session connects or disconnects.
* A workstation is locked or unlocked.
* A screen saver is invoked or dismissed.
* A replay attack is detected. This event indicates that a Kerberos request was received twice with identical information. This condition could also be caused by network misconfiguration.
* A user is granted access to a wireless network. It can be either a user account or the computer account.
* A user is granted access to a wired 802.1x network. It can be either a user account or the computer account.

Logon events are essential to understanding user activity and detecting potential attacks.

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-other-logonlogoff-events)

## Data Dictionaries

| EventId | Description | Minimum OS |
|--------|---------|-------|
| 4649 | A replay attack was detected | Windows Vista, Windows Server 2008 |
| 4778 | A session was reconnected to a Window Station | Windows Vista, Windows Server 2008 |
| 4779 | A session was disconnected from a Window Station | Windows Vista, Windows Server 2008 |
| 4800 | The workstation was locked | Windows Vista, Windows Server 2008 |
| 4801 | The workstation was unlocked | Windows Vista, Windows Server 2008 |
| 4802 | The screen saver was invoked | Windows Vista, Windows Server 2008 |
| 4803 | The screen saver was dismissed | Windows Vista, Windows Server 2008 |
| 5378 | The requested credentials delegation was disallowed by policy | Windows Vista, Windows Server 2008 |
| 5632 | A request was made to authenticate to a wireless network | Windows Vista, Windows Server 2008 |
| 5633 | A request was made to authenticate to a wired network | Windows Vista, Windows Server 2008 |