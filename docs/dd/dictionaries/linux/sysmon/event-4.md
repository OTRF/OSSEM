# Event ID 4: Sysmon service state changed
###### Version: 4.81

## Description
The **service state change** event reports the state of the Sysmon service (started or stopped).

## Data Dictionary
|Field Name|Type|Description|Sample Value|
|---|---|---|---|
|UtcTime|date|Time in UTC when event was created|`2021-10-15T00:26:12.0920000Z`|
|State|string|sysmon service state (i.e. stopped)|`Started`|
|Version|string|sysmon version|`1.0.0`|
|SchemaVersion|string|sysmon config schema version|`4.81`|
