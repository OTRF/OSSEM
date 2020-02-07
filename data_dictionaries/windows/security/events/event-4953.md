# Event ID 4953: Windows Firewall ignored a rule because it could not be parsed.

## Description
This event generates if Windows Firewall was not able to parse Windows Firewall rule for some reason.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|profile|Profile|TBD|string|the name of the profile of the ignored rule.|All|
|reason_for_rejection|ReasonForRejection|TBD|string|the reason, why the rule was ignored.|An error occurred.|
|rule_id|RuleId|TBD|string|the unique identifier for ignored firewall rule.|{08CBB349-D158-46BE-81E1-2ABC59BDD523}|
|rule_name|RuleName|TBD|string|the name of the rule which was ignored.|-|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4953.md)
* [MS Security Auditing Category - Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#policy-change)
* [MS Security Auditing Sub-category - Audit MPSSVC Rule-Level Policy Change](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-mpssvc-rule-level-policy-change.md)

## Tags
* Policy Change
* Audit MPSSVC Rule-Level Policy Change