# Event ID 4767: A user account was unlocked

## Description
This event generates every time a user account is unlocked. For user accounts, this event generates on domain controllers, member servers, and workstations.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_name|TargetUserName|string|the name of the account that was unlocked.|`Auditor`|
|user_domain|TargetDomainName|string|target account's domain or computer name.|`CONTOSO`|
|user_sid|TargetSid|string|SID of account that was unlocked.|`S-1-5-21-3457937927-2839227994-823803824-2104`|
|user_reporter_sid|SubjectUserSid|string|SID of account that performed the unlock operation.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_reporter_name|SubjectUserName|string|the name of the account that performed the unlock operation.|`dadmin`|
|user_reporter_domain|SubjectDomainName|string|subject's domain or computer name.|`CONTOSO`|
|user_reporter_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x30d5f`|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4767.md)
* [MS Security Auditing Category - Account Management](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#account-management)
* [MS Security Auditing Sub-category - Audit User Account Management](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-user-account-management.md)

## Tags
* Account Management
* Audit User Account Management