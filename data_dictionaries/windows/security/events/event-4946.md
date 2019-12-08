# Event ID 4946: A change has been made to Windows Firewall exception list. A rule was added.

## Description

This event generates when new rule was locally added to Windows Firewall.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|profile_changed|ProfileChanged|string|the list of profiles to which new rule was applied.|All|
|rule_id|RuleId|string|the unique new firewall rule identifier.|{F2649D59-1355-4E3C-B886-CDD08B683199}|
|rule_name|RuleName|string|the name of the rule which was added.|Allow All Rule|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4946.md)