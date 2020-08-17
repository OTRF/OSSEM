# Event ID 4664: An attempt was made to create a hard link
###### Version: 0

## Description
This event generates when an NTFS hard link was successfully created.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account that made an attempt to create the hard link.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|UnicodeString|the name of the account that made an attempt to create the hard link.|`dadmin`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|`0x43659`|
|file_name|FileName|UnicodeString|the name of a file or folder that new hard link refers to.|`C:\notepad.exe`|
|file_link_name|LinkName|UnicodeString|full path name with new hard link file name.|`C:\Docs\My.exe`|
|transaction_id|TransactionId|GUID|unique GUID of the transaction. This field can help you correlate this event with other events that might contain the same Transaction ID, such as "4660(S): An object was deleted."|`{00000000-0000-0000-0000-000000000000}`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4664.md)
* [MS Security Auditing Category - Object Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#object-access)
* [MS Security Auditing Sub-category - Audit File System](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-file-system.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Object Access
* Audit File System