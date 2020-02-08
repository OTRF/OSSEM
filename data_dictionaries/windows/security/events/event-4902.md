# Event ID 4902: The Per-user audit policy table was created.

## Description
This event generates during system startup if Per-user audit policy is defined on the computer.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|pua_count|PuaCount|integer|number of users for which Per-user policies were defined (number of unique users).|`1`|
|pua_policy_id|PuaPolicyId|integer|unique per-User Audit Policy hexadecimal identifier.|`0x703e`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4902.md)
* [MS Security Auditing Category - Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#policy-change)
* [MS Security Auditing Sub-category - Audit Policy Change](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-policy-change.md)

## Tags
* Policy Change
* Audit Policy Change