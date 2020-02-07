# Event ID 4948: A change has been made to Windows Firewall exception list. A rule was deleted.

## Description
This event generates when Windows Firewall rule was deleted.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|profile_changed|ProfileChanged|TBD|string|the list of profiles to which deleted rule was applied.|All|
|rule_id|RuleId|TBD|string|the unique identifier for deleted firewall rule.|{F2649D59-1355-4E3C-B886-CDD08B683199}|
|rule_name|RuleName|TBD|string|the name of the rule which was deleted.|Allow All Rule|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4948.md)
* [MS Security Auditing Category - Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#policy-change)
* [MS Security Auditing Sub-category - Audit MPSSVC Rule-Level Policy Change](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-mpssvc-rule-level-policy-change.md)

## Tags
* Policy Change
* Audit MPSSVC Rule-Level Policy Change