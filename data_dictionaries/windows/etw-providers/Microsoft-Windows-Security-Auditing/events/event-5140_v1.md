# Event ID 5140: A network share object was accessed

## Description
Event ID 5140: A network share object was accessed

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account that requested access to network share object.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|UnicodeString|the name of the account that requested access to network share object.|`dadmin`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|`0x541f35`|
|object_type|ObjectType|UnicodeString|The type of an object that was accessed during the operation. Always "File" for this event.|`File`|
|src_ip_addr|IpAddress|UnicodeString|source IP address from which access was performed.|`10.0.0.100`|
|src_port|IpPort|UnicodeString|source TCP or UDP port which was used from remote or local machine to request the access.|`49212`|
|share_name|ShareName|UnicodeString|the name of accessed network share.|`\*\Documents`|
|share_local_path|ShareLocalPath|UnicodeString|the full system (NTFS) path for accessed share. The format is: \??\PATH|`\??\C:\Documents`|
|share_access_mask|AccessMask|HexInt32|the sum of hexadecimal values of requested access rights. See "Table 13. File access codes."|`0x1`|
|user_access_list|AccessList|UnicodeString|the list of access rights which were requested by Subject\Security ID. These access rights depend on Object Type. Has always "ReadData (or ListDirectory)" value for this event.|`%%4416`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5140.md)
* [MS Security Auditing Category - Object Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#object-access)
* [MS Security Auditing Sub-category - Audit File Share](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-file-share.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* version_1
* Object Access
* Audit File Share