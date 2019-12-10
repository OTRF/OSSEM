# Event ID 4902: The Per-user audit policy table was created.

## Description

This event generates during system startup if Per-user audit policy is defined on the computer.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|pua_count|PuaCount|integer|number of users for which Per-user policies were defined (number of unique users).|1|
|pua_policy_id|PuaPolicyId|integer|unique per-User Audit Policy hexadecimal identifier.|0x703e|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4902.md)