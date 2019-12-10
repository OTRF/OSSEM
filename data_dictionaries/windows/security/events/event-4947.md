# Event ID 4947: A change has been made to Windows Firewall exception list. A rule was modified.

## Description

This event generates when Windows Firewall rule was modified.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|profile_changed|ProfileChanged|string|the list of profiles to which changed rule is applied.|All|
|rule_id|RuleId|string|the unique identifier for modified firewall rule.|{F2649D59-1355-4E3C-B886-CDD08B683199}|
|rule_name|RuleName|string|the name of the rule which was modified.|Allow All Rule|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4947.md)