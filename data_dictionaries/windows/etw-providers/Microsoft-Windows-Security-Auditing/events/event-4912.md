# Event ID 4912: Per User Audit Policy was changed.

## Description
This event generates every time Per User Audit Policy was changed.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account that made a change to per-user audit policy.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|UnicodeString|the name of the account that made a change to per-user audit policy.|`dadmin`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x11ae30`|
|target_user_sid|TargetUserSid|SID|SID of account for which the Per User Audit Policy was changed.|`S-1-5-21-3457937927-2839227994-823803824-2104`|
|policy_category_id|CategoryId|UnicodeString|the name of auditing category which subcategory state was changed.|`%%8276`|
|policy_subcategory_id|SubcategoryId|UnicodeString|the name of auditing subcategory which state was changed.|`%%13312`|
|policy_subcategory_guid|SubcategoryGuid|GUID|the unique GUID of changed subcategory.|`{0CCE922B-69AE-11D9-BED3-505054503030}`|
|policy_changes|AuditPolicyChanges|UnicodeString|changes which were made for the subcategory.|`%%8452`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4912.md)
* [MS Security Auditing Category - Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#policy-change)
* [MS Security Auditing Sub-category - Audit Policy Change](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-policy-change.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Policy Change
* Audit Policy Change