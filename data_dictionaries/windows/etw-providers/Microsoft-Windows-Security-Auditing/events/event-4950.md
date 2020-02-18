# Event ID 4950: A Windows Firewall setting has changed.

## Description
Event ID 4950: A Windows Firewall setting has changed.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|profile_changed|ProfileChanged|UnicodeString|the name of profile in which setting was changed.|`Domain`|
|setting_type|SettingType|UnicodeString|the name of the setting which was modified.|`Default Outbound Action`|
|setting_value|SettingValue|UnicodeString|new value of modified setting.|`Block`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4950.md)
* [MS Security Auditing Category - Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#policy-change)
* [MS Security Auditing Sub-category - Audit MPSSVC Rule-Level Policy Change](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-mpssvc-rule-level-policy-change.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Policy Change
* Audit MPSSVC Rule-Level Policy Change