# Event ID 4907: Auditing settings on object were changed.

## Description
This event generates when a Security Descriptor (SD) on an object was changed.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account that made an attempt to create the hard link.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|UnicodeString|the name of the account that made a change to object's auditing settings.|`dadmin`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|`0x138eb0`|
|object_server|ObjectServer|UnicodeString|has "Security" value for this event.|`Security`|
|object_type|ObjectType|UnicodeString|The type of an object that was accessed during the operation.|`Key`|
|object_name|ObjectName|UnicodeString|full path and name of the object for which the SACL was modified. Depends on Object Type|`\REGISTRY\MACHINE\SYSTEM\ControlSet001\Services\EventLog\Internet Explorer`|
|object_handle_id|HandleId|Pointer|hexadecimal value of a handle to Object Name. This field can help you correlate this event with other events that might contain the same Handle ID|`0x2f8`|
|object_old_sd|OldSd|UnicodeString|the old Security Descriptor Definition Language (SDDL) value for the object.|`S:AI`|
|object_new_sd|NewSd|UnicodeString|the new Security Descriptor Definition Language (SDDL) value for the object.|`S:ARAI(AU;CISA;KA;;;S-1-5-21-3457937927-2839227994-823803824-1104)`|
|process_id|ProcessId|Pointer|hexadecimal Process ID of the process through which the object's SACL was changed.|`0x120c`|
|process_path|ProcessName|UnicodeString|full path and the name of the executable for the process.|`C:\Windows\regedit.exe`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4907.md)
* [MS Security Auditing Category - Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#policy-change)
* [MS Security Auditing Sub-category - Audit Policy Change](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-policy-change.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Policy Change
* Audit Policy Change