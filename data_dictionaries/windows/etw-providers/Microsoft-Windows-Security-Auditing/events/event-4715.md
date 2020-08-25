# Event ID 4715: The audit policy (SACL) on an object was changed.
###### Version: 0

## Description
This event generates every time local audit policy security descriptor changes.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account that requested the "change local audit policy security descriptor (SACL)" operation.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|UnicodeString|the name of the account that requested the "change local audit policy security descriptor (SACL)" operation.|`dadmin`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x11ae30`|
|object_old_sd|OldSd|UnicodeString|the old Security Descriptor Definition Language (SDDL) value for the audit policy.|`D:(A;;DCSWRPDTRC;;;BA)(D;;DCSWRPDTRC;;;SY)S:NO_ACCESS_CONTROL`|
|object_new_sd|NewSd|UnicodeString|new Security Descriptor Definition Language (SDDL) value for the audit policy.|`D:(A;;DCSWRPDTRC;;;BA)(A;;DCSWRPDTRC;;;SY)S:NO_ACCESS_CONTROL`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4715.md)
* [MS Security Auditing Category - Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#policy-change)
* [MS Security Auditing Sub-category - Audit Policy Change](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-policy-change.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Policy Change
* Audit Policy Change