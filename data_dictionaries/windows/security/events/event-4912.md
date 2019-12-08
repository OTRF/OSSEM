# Event ID 4912: Per User Audit Policy was changed.

## Description

This event generates every time Per User Audit Policy was changed.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|string|SID of account that made a change to per-user audit policy.|S-1-5-21-3457937927-2839227994-823803824-1104|
|user_name|SubjectUserName|string|the name of the account that made a change to per-user audit policy.|dadmin|
|user_domain|SubjectDomainName|string|subject's domain or computer name.|CONTOSO|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x11ae30|
|target_user_sid|TargetUserSid|string|SID of account for which the Per User Audit Policy was changed.|S-1-5-21-3457937927-2839227994-823803824-2104|
|category_id|CategoryId|integer|the name of auditing category which subcategory state was changed.|%%8276|
|subcategory_id|SubcategoryId|integer|the name of auditing subcategory which state was changed.|%%13312|
|subcategory_guid|SubcategoryGuid|string|the unique GUID of changed subcategory.|{0CCE922B-69AE-11D9-BED3-505054503030}|
|subcategory_policy_changes|AuditPolicyChanges|string|changes which were made for the subcategory.|%%8452|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4912.md)