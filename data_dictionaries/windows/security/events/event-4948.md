# Event ID 4948: A change has been made to Windows Firewall exception list. A rule was deleted.

## Description

This event generates when Windows Firewall rule was deleted.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|profile_changed|ProfileChanged|string|the list of profiles to which deleted rule was applied.|All|
|rule_id|RuleId|string|the unique identifier for deleted firewall rule.|{F2649D59-1355-4E3C-B886-CDD08B683199}|
|rule_name|RuleName|string|the name of the rule which was deleted.|Allow All Rule|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4948.md)