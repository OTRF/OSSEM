# Event ID 4953: Windows Firewall ignored a rule because it could not be parsed.

## Description

This event generates if Windows Firewall was not able to parse Windows Firewall rule for some reason.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|profile|Profile|string|the name of the profile of the ignored rule.|All|
|reason_for_rejection|ReasonForRejection|string|the reason, why the rule was ignored.|An error occurred.|
|rule_id|RuleId|string|the unique identifier for ignored firewall rule.|{08CBB349-D158-46BE-81E1-2ABC59BDD523}|
|rule_name|RuleName|string|the name of the rule which was ignored.|-|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4953.md)