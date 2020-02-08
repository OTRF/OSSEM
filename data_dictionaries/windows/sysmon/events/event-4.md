# Event ID 4: Sysmon service state changed

## Description
The service state change event reports the state of the Sysmon service (started or stopped).

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|event_date_creation|UtcTime|date|Time in UTC when event was created|`4/11/18 5:36`|
|service_state|State|string|sysmon service state (i.e. stopped)|`Stopped`|
|file_version|Version|string|sysmon version|`7.01`|
|sysmon_schema_version|SchemaVersion|string|sysmon config schema version|`4`|

## Resources
* [Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-4-sysmon-service-state-changed)
* [TrustedSec Sysmon Community Guide](https://github.com/trustedsec/SysmonCommunityGuide/blob/master/sysmon-events.md#service-state-change)
