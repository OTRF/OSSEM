# Event ID 4719: System audit policy was changed.

## Description
Event ID 4719: System audit policy was changed.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account that made a change to local audit policy.|`S-1-5-18`|
|user_name|SubjectUserName|UnicodeString|he name of the account that made a change to local audit policy.|`DC01$`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x3e7`|
|policy_category_id|CategoryId|UnicodeString|the name of auditing Category which subcategory was changed.|`%%8274`|
|policy_subcategory_id|SubcategoryId|UnicodeString|the name of auditing Subcategory which was changed|`%%12807`|
|policy_subcategory_guid|SubcategoryGuid|GUID|the unique subcategory GUID|`{0CCE9223-69AE-11D9-BED3-505054503030}`|
|policy_changes|AuditPolicyChanges|UnicodeString|changes which were made for "Subcategory"|`%%8448, %%8450`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4719.md)
* [MS Security Auditing Category - Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#policy-change)
* [MS Security Auditing Sub-category - Audit Policy Change](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-policy-change.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Policy Change
* Audit Policy Change