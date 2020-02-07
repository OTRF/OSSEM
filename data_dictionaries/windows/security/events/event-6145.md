# Event ID 6145: One or more errors occurred while processing security policy in the group policy objects.

## Description
This event generates every time settings from the "Security Settings" section in the group policy object are applied to a computer with one or more errors.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|error_code|ErrorCode|TBD|integer|specific error code which shows the error which happened during Group Policy processing.|1332|
|gpo_list|GPOList|TBD|string|the list of Group Policy Objects that include "Security Settings" policies, and that were applied with errors to the computer.|{6AC1786C-016F-11D2-945F-00C04fB984F9} Default Domain Controllers Policy {31B2F340-016D-11D2-945F-00C04FB984F9} Default Domain Policy|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-6145.md)
* [MS Security Auditing Category - Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#policy-change)
* [MS Security Auditing Sub-category - Audit Other Policy Change Events](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-other-policy-change-events.md)

## Tags
* Policy Change
* Audit Other Policy Change Events