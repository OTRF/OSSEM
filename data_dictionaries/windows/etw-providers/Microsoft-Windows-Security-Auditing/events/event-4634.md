# Event ID 4634: An account was logged off

## Description
This event shows that logon session was terminated and no longer exists.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|TargetUserSid|SID|SID of account that was logged off.|`S-1-5-90-1`|
|user_name|TargetUserName|UnicodeString|the name of the account that was logged off|`DQM-1`|
|user_domain|TargetDomainName|UnicodeString|subject's domain or computer name.|`Window Manager`|
|user_logon_id|TargetLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|`0x1a0992`|
|logon_type|LogonType|UInt32|the type of logon which was performed.|`2`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4634.md)
* [MS Security Auditing Category - Logon/Logoff](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#logonlogoff)
* [MS Security Auditing Sub-category - Audit Logoff](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-logoff.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Logon/Logoff
* Audit Logoff