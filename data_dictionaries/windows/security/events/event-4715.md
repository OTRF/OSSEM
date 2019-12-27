# Event ID 4715: The audit policy (SACL) on an object was changed.

## Description

This event generates every time local audit policy security descriptor changes.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|string|SID of account that requested the "change local audit policy security descriptor (SACL)" operation.|S-1-5-21-3457937927-2839227994-823803824-1104|
|user_name|SubjectUserName|string|the name of the account that requested the "change local audit policy security descriptor (SACL)" operation.|dadmin|
|user_domain|SubjectDomainName|string|subject's domain or computer name.|CONTOSO|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x11ae30|
|object_old_sd|OldSd|string|the old Security Descriptor Definition Language (SDDL) value for the audit policy.|D:(A;;DCSWRPDTRC;;;BA)(D;;DCSWRPDTRC;;;SY)S:NO\_ACCESS\_CONTROL|
|object_new_sd|NewSd|string|new Security Descriptor Definition Language (SDDL) value for the audit policy.|D:(A;;DCSWRPDTRC;;;BA)(A;;DCSWRPDTRC;;;SY)S:NO\_ACCESS\_CONTROL|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4715.md)