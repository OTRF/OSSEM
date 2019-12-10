# Event ID 4950: A Windows Firewall setting has changed.

## Description

This event generates when Windows Firewall local setting was changed.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|profile_changed|ProfileChanged|string|the name of profile in which setting was changed.|Domain|
|setting_type|SettingType|string|the name of the setting which was modified.|Default Outbound Action|
|setting_value|SettingValue|string|new value of modified setting.|Block|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4950.md)