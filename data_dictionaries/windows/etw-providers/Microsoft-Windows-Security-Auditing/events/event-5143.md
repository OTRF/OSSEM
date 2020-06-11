# Event ID 5143: A network share object was modified

## Description
This event generates every time network share object was modified.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account that requested the "modify network share object" operation.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|UnicodeString|the name of the account that requested the "modify network share object" operation.|`dadmin`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|`0x38d12`|
|object_type|ObjectType|UnicodeString|The type of an object that was modified. Always "Directory" for this event.|`Directory`|
|share_name|ShareName|UnicodeString|the name of the modified share object. The format is: *\SHARE_NAME|`\*\Documents`|
|share_local_path|ShareLocalPath|UnicodeString|the full system (NTFS) path for the added share object.|`C:\Documents`|
|share_old_remark|OldRemark|UnicodeString|the old value of network share "Comments:" field. Has "N/A" value if it is not set.|`N/A`|
|share_new_remark|NewRemark|UnicodeString|the new value of network share "Comments:" field. Has "N/A" value if it is not set.|`N/A`|
|share_old_max_users|OldMaxUsers|HexInt32|old hexadecimal value of "Limit the number of simultaneous user to:" field. Has "0xFFFFFFFF" value if the number of connections is unlimited.|`0xffffffff`|
|share_new_max_users|NewMaxUsers|HexInt32|new hexadecimal value of "Limit the number of simultaneous user to:" field. Has "0xFFFFFFFF" value if the number of connections is unlimited.|`0xffffffff`|
|share_old_flags|OldShareFlags|HexInt32|old hexadecimal value of "Offline Settings" caching settings window flags.|`0x800`|
|share_new_flags|NewShareFlags|HexInt32|new hexadecimal value of "Offline Settings" caching settings window flags.|`0x800`|
|share_old_sd|OldSD|UnicodeString|the old Security Descriptor Definition Language (SDDL) value for network share security descriptor.|`-`|
|share_new_sd|NewSD|UnicodeString|the new Security Descriptor Definition Language (SDDL) value for network share security descriptor.|`O:BAG:DAD:(D;;FA;;;S-1-5-21-3457937927-2839227994-823803824-1104)(A;OICI;FA;;;WD)(A;OICI;FA;;;BA)`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5143.md)
* [MS Security Auditing Category - Object Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#object-access)
* [MS Security Auditing Sub-category - Audit File Share](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-file-share.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Object Access
* Audit File Share