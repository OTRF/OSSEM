# Event ID 4767: A user account was unlocked

## Description
Event ID 4767: A user account was unlocked

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_name|TargetUserName|UnicodeString|the name of the account that was unlocked.|`Auditor`|
|user_domain|TargetDomainName|UnicodeString|target account's domain or computer name.|`CONTOSO`|
|user_sid|TargetSid|SID|SID of account that was unlocked.|`S-1-5-21-3457937927-2839227994-823803824-2104`|
|user_reporter_sid|SubjectUserSid|SID|SID of account that performed the unlock operation.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_reporter_name|SubjectUserName|UnicodeString|the name of the account that performed the unlock operation.|`dadmin`|
|user_reporter_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|user_reporter_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x30d5f`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4767.md)
* [MS Security Auditing Category - Account Management](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#account-management)
* [MS Security Auditing Sub-category - Audit User Account Management](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-user-account-management.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Account Management
* Audit User Account Management