# Event ID 4647: User initiated logoff

## Description
Event ID 4647: User initiated logoff

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|TargetUserSid|SID|SID of account that requested the "logoff" operation|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|TargetUserName|UnicodeString|the name of the account that requested the "logoff" operation|`dadmin`|
|user_domain|TargetDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|user_logon_id|TargetLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|`0x29b379`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4647.md)
* [MS Security Auditing Category - Logon/Logoff](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#logonlogoff)
* [MS Security Auditing Sub-category - Audit Logoff](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-logoff.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Logon/Logoff
* Audit Logoff