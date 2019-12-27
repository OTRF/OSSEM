# Event ID 4957: Windows Firewall did not apply the following rule.

## Description

This event generates when Windows Firewall starts or apply new rule, and the rule cannot be applied for some reason.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|rule_id|RuleId|string|the unique identifier for not applied firewall rule.|CoreNet-Teredo-In|
|rule_name|RuleName|string|the name of the rule which was not applied.|Core Networking - Teredo (UDP-In)|
|rule_attr|RuleAttr|string|the reason why the rule was not applied.|Local Port|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4957.md)