# Event ID 5379: Credential Manager credentials were read

## Description
Event ID 5379: Credential Manager credentials were read

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account that performed a read operation on stored credentials in CM|`S-1-5-18`|
|user_name|SubjectUserName|UnicodeString|the name of the account that performed a read operation on stored credentials in CM|`ACCT001$`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name|`SHIRE`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|`0x3e7`|
|credentials_read|TargetName|UnicodeString|stored credentials that were read|`WindowsLive:(token):name=xxxxxasas;serviceuri=*`|
|credentials_read_type|Type|UInt32||`0`|
|credential_read_returned_count|CountOfCredentialsReturned|UInt32||`0`|
|object_operation_type|ReadOperation|UnicodeString||`%%8100`|
|credentials_read_returned_code|ReturnCode|UInt32||`0`|
|process_creation_time|ProcessCreationTime|FILETIME||`2019-02-25T22:33:21.621488200Z`|
|process_id|ClientProcessId|UInt32||`4432`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-5379.md)
* [MS Security Auditing Category - System](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#system)
* [MS Security Auditing Sub-category - Audit Other System Events](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-other-system-events.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* System
* Audit Other System Events