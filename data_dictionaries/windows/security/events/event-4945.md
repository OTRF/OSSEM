# Event ID 4945: A rule was listed when the Windows Firewall started.

## Description

This event generates every time Windows Firewall service starts.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|profile_used|ProfileUsed|string|the name of the profile that the rule belongs to. It always has value “Public”, because this event shows rules only for “Public” profile.|Public|
|rule_id|RuleId|string|the unique firewall rule identifier.|NPS-NPSSvc-In-RPC|
|rule_name|RuleName|string|the name of the rule which was listed when the Windows Firewall started.|Network Policy Server (RPC)|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4945.md)