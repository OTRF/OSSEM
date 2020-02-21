# Event ID 4803: The screen saver was dismissed

## Description
Event ID 4803: The screen saver was dismissed

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|TargetUserSid|SID|SID of account that requested the "dismiss screensaver" operation.|`S-1-5-21-3457937927-2839227994-823803824-1104<`|
|user_name|TargetUserName|UnicodeString|the name of the account that requested the "dismiss screensaver" operation.|`dadmin`|
|user_domain|TargetDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|user_logon_id|TargetLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|`0x759a9`|
|user_session_id|SessionId|UInt32|unique ID of a session for which screen saver was dismissed. You can see the list of current session IDs using "query session" command in command prompt.|`3`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4803.md)
* [MS Security Auditing Category - Account Logon](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#account-logon)
* [MS Security Auditing Category - Logon/Logoff](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#logonlogoff)
* [MS Security Auditing Sub-category - Audit Other Logon/Logoff Events](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-other-logon/logoff-events.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Account Logon
* Logon/Logoff
* Audit Other Logon/Logoff Events