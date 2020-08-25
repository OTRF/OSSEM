# Event ID 5144: A network share object was deleted
###### Version: 0

## Description
This event generates every time a network share object is deleted.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account that requested the "delete network share object" operation|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|UnicodeString|the name of the account that requested the "delete network share object" operation.|`dadmin`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|`0x38d12`|
|share_name|ShareName|UnicodeString|the name of the deleted share object. The format is: *\SHARE_NAME|`\*\Documents`|
|share_local_path|ShareLocalPath|UnicodeString|the full system (NTFS) path for the deleted share object.|`C:\Documents`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5144.md)
* [MS Security Auditing Category - Object Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#object-access)
* [MS Security Auditing Sub-category - Audit File Share](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-file-share.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Object Access
* Audit File Share