# Event ID 4945: A rule was listed when the Windows Firewall started.

## Description
This event generates every time Windows Firewall service starts.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|profile_used|ProfileUsed|string|the name of the profile that the rule belongs to. It always has value "Public", because this event shows rules only for "Public" profile.|`Public`|
|rule_id|RuleId|string|the unique firewall rule identifier.|`NPS-NPSSvc-In-RPC`|
|rule_name|RuleName|string|the name of the rule which was listed when the Windows Firewall started.|`Network Policy Server (RPC)`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4945.md)
* [MS Security Auditing Category - Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#policy-change)
* [MS Security Auditing Sub-category - Audit MPSSVC Rule-Level Policy Change](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-mpssvc-rule-level-policy-change.md)

## Tags
* Policy Change
* Audit MPSSVC Rule-Level Policy Change