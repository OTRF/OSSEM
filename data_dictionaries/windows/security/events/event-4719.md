# Event ID 4719: System audit policy was changed.

## Description
This event generates when the computer's audit policy changes.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|TBD|string|SID of account that made a change to local audit policy.|S-1-5-18|
|user_name|SubjectUserName|TBD|string|he name of the account that made a change to local audit policy.|DC01$|
|user_domain|SubjectDomainName|TBD|string|subject's domain or computer name.|CONTOSO|
|user_logon_id|SubjectLogonId|TBD|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x3e7|
|policy_category_id|CategoryId|TBD|integer|the name of auditing Category which subcategory was changed.|%%8274|
|policy_subcategory_id|SubcategoryId|TBD|integer|the name of auditing Subcategory which was changed|%%12807|
|policy_subcategory_guid|SubcategoryGuid|TBD|string|the unique subcategory GUID|{0CCE9223-69AE-11D9-BED3-505054503030}|
|policy_changes|AuditPolicyChanges|TBD|integer|changes which were made for "Subcategory"|%%8448, %%8450|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4719.md)
* [MS Security Auditing Category - Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#policy-change)
* [MS Security Auditing Sub-category - Audit Policy Change](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-policy-change.md)

## Tags
* Policy Change
* Audit Policy Change