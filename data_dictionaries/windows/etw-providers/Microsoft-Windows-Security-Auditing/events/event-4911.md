# Event ID 4911: Resource attributes of the object were changed.

## Description
This event generates when resource attributes of the file system object were changed.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account that changed the resource attributes of the file system object.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|UnicodeString|the name of the account that changed the resource attributes of the file system object.|`dadmin`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x37925`|
|object_server|ObjectServer|UnicodeString|has "Security" value for this event.|`Security`|
|object_type|ObjectType|UnicodeString|he type of an object that was accessed during the operation. Always "File" for this event.|`File`|
|file_path|ObjectName|UnicodeString|full path and/or name of the object for which resource attributes were changed.|`C:\Audit Files\HBI Data.txt`|
|object_handle_id|HandleId|Pointer|hexadecimal value of a handle to Object Name. This field can help you correlate this event with other events that might contain the same Handle ID, for example, "4663(S): An attempt was made to access an object." This parameter might not be captured in the event, and in that case appears as "0x0".|`0x49c`|
|object_old_sd|OldSd|UnicodeString|the Security Descriptor Definition Language (SDDL) value for the old resource attributes.|`S:AI`|
|object_new_sd|NewSd|UnicodeString|the Security Descriptor Definition Language (SDDL) value for the new resource attributes.|`S:ARAI(RA;ID;;;;WD;("Impact_MS",TI,0x10020,3000))`|
|process_id|ProcessId|Pointer|hexadecimal Process ID of the process through which the resource attributes of the file system object were changed.|`0x67c`|
|process_path|ProcessName|UnicodeString|full path and the name of the executable for the process.|`C:\Windows\System32\svchost.exe`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4911.md)
* [MS Security Auditing Category - Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#policy-change)
* [MS Security Auditing Sub-category - Audit Authorization Policy Change](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-authorization-policy-change.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Policy Change
* Audit Authorization Policy Change