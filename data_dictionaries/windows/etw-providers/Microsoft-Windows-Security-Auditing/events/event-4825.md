# Event ID 4825: A user was denied the access to Remote Desktop.
###### Version: 0

## Description
This event is generated when an authenticated user who is not allowed to log on remotely attempts to connect to this computer through Remote Desktop.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_name|AccountName|UnicodeString|the name of the account that requested the "invoke screensaver" operation.|`dadmin`|
|user_domain|AccountDomain|UnicodeString|SID of account that requested the "invoke screensaver" operation|`CONTOSO`|
|user_logon_id|LogonID|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|`0x109d9755e`|
|src_ip_addr|ClientAddress|UnicodeString|IP address of the computer from which the session was disconnected|`10.10.10.10`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4825.md)
* [MS Security Auditing Category - System](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#system)
* [MS Security Auditing Sub-category - Audit Other System Events](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-other-system-events.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* System
* Audit Other System Events