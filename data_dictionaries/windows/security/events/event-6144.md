# Event ID 6144: Security policy in the group policy objects has been applied successfully.

## Description

This event generates every time settings from the “Security Settings” section in the group policy object are applied successfully to a computer, without any errors.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|error_code|ErrorCode|integer|always has "0" value for this event.|0|
|gpo_list|GPOList|string|the list of Group Policy Objects that include "Security Settings" policies, and that were applied to the computer.|{8AB9311A-E5FB-4A5A-8FB7-027D1B877D6D} DC Main Policy|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-6144.md)