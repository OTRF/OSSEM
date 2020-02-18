# Event ID 4957: Windows Firewall did not apply the following rule.

## Description
Event ID 4957: Windows Firewall did not apply the following rule.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|rule_id|RuleId|UnicodeString|the unique identifier for not applied firewall rule.|`CoreNet-Teredo-In`|
|rule_name|RuleName|UnicodeString|the name of the rule which was not applied.|`Core Networking - Teredo (UDP-In)`|
|rule_attr|RuleAttr|UnicodeString|the reason why the rule was not applied.|`Local Port`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4957.md)
* [MS Security Auditing Category - Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#policy-change)
* [MS Security Auditing Sub-category - Audit MPSSVC Rule-Level Policy Change](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-mpssvc-rule-level-policy-change.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Policy Change
* Audit MPSSVC Rule-Level Policy Change