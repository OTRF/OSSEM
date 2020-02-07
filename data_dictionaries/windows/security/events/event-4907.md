# Event ID 4907: Auditing settings on object were changed.

## Description
This event generates when a Security Descriptor (SD) on an object was changed.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|TBD|string|SID of account that made an attempt to create the hard link.|S-1-5-21-3457937927-2839227994-823803824-1104|
|user_name|SubjectUserName|TBD|string|the name of the account that made a change to object's auditing settings.|dadmin|
|user_domain|SubjectDomainName|TBD|string|subject's domain or computer name.|CONTOSO|
|user_logon_id|SubjectLogonId|TBD|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|0x138eb0|
|object_server|ObjectServer|TBD|string|has "Security" value for this event.|Security|
|object_type|ObjectType|TBD|string|The type of an object that was accessed during the operation.|Key|
|object_name|ObjectName|TBD|string|full path and name of the object for which the SACL was modified. Depends on Object Type|\REGISTRY\MACHINE\SYSTEM\ControlSet001\Services\EventLog\Internet Explorer|
|object_handle_id|HandleId|TBD|integer|hexadecimal value of a handle to Object Name. This field can help you correlate this event with other events that might contain the same Handle ID|0x2f8|
|object_old_sd|OldSd|TBD|string|the old Security Descriptor Definition Language (SDDL) value for the object.|S:AI|
|object_new_sd|NewSd|TBD|string|the new Security Descriptor Definition Language (SDDL) value for the object.|S:ARAI(AU;CISA;KA;;;S-1-5-21-3457937927-2839227994-823803824-1104)|
|process_id|ProcessId|TBD|integer|hexadecimal Process ID of the process through which the object's SACL was changed.|0x120c|
|process_path|ProcessName|TBD|string|full path and the name of the executable for the process.|C:\Windows\regedit.exe|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4907.md)
* [MS Security Auditing Category - Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#policy-change)
* [MS Security Auditing Sub-category - Audit Policy Change](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-policy-change.md)

## Tags
* Policy Change
* Audit Policy Change