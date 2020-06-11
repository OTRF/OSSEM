# Event ID 6144: Security policy in the group policy objects has been applied successfully.

## Description
This event generates every time settings from the "Security Settings" section in the group policy object are applied successfully to a computer, without any errors.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|error_code|ErrorCode|UInt32|always has "0" value for this event.|`0`|
|gpo_list|GPOList|UnicodeString|the list of Group Policy Objects that include "Security Settings" policies, and that were applied to the computer.|`{8AB9311A-E5FB-4A5A-8FB7-027D1B877D6D} DC Main Policy`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-6144.md)
* [MS Security Auditing Category - Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#policy-change)
* [MS Security Auditing Sub-category - Audit Other Policy Change Events](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-other-policy-change-events.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Policy Change
* Audit Other Policy Change Events