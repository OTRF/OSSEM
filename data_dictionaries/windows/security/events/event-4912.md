# Event ID 4912: Per User Audit Policy was changed.

## Description
This event generates every time Per User Audit Policy was changed.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|TBD|string|SID of account that made a change to per-user audit policy.|S-1-5-21-3457937927-2839227994-823803824-1104|
|user_name|SubjectUserName|TBD|string|the name of the account that made a change to per-user audit policy.|dadmin|
|user_domain|SubjectDomainName|TBD|string|subject's domain or computer name.|CONTOSO|
|user_logon_id|SubjectLogonId|TBD|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x11ae30|
|target_user_sid|TargetUserSid|TBD|string|SID of account for which the Per User Audit Policy was changed.|S-1-5-21-3457937927-2839227994-823803824-2104|
|policy_category_id|CategoryId|TBD|integer|the name of auditing category which subcategory state was changed.|%%8276|
|policy_subcategory_id|SubcategoryId|TBD|integer|the name of auditing subcategory which state was changed.|%%13312|
|policy_subcategory_guid|SubcategoryGuid|TBD|string|the unique GUID of changed subcategory.|{0CCE922B-69AE-11D9-BED3-505054503030}|
|policy_changes|AuditPolicyChanges|TBD|string|changes which were made for the subcategory.|%%8452|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4912.md)
* [MS Security Auditing Category - Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#policy-change)
* [MS Security Auditing Sub-category - Audit Policy Change](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-policy-change.md)

## Tags
* Policy Change
* Audit Policy Change