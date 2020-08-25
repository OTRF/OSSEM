# Event ID 4817: Auditing settings on object were changed.
###### Version: 0

## Description
This event generates when the Global Object Access Auditing.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account that made a change to Global Object Access Auditing policy.|`S-1-5-18`|
|user_name|SubjectUserName|UnicodeString|the name of the account that made a change to Global Object Access Auditing policy.|`DC01$`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x3e7`|
|object_server|ObjectServer|UnicodeString|has "LSA" value for this event.|`LSA`|
|object_type|ObjectType|UnicodeString|The type of an object to which this event applies. Always "Global SACL" for this event.|`Global SACL`|
|object_name|ObjectName|UnicodeString|Key - if "Registry" Global Object Access Auditing policy was changed. File - if "File system" Global Object Access Auditing policy was changed.|`Key`|
|object_old_sd|OldSd|UnicodeString|the old Security Descriptor Definition Language (SDDL) value for the Global Object Access Auditing policy.|`None`|
|object_new_Sd|NewSd|UnicodeString|the new Security Descriptor Definition Language (SDDL) value for the Global Object Access Auditing policy.|`S:(AU;SA;RC;;;S-1-5-21-3457937927-2839227994-823803824-1104)`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4817.md)
* [MS Security Auditing Category - Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#policy-change)
* [MS Security Auditing Sub-category - Audit Policy Change](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-policy-change.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Policy Change
* Audit Policy Change