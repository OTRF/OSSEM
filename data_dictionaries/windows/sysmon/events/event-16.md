# Event ID 16 - Sysmon Config State Changed

## Description
This event logs when the local sysmon configuration is updated.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|event_date_creation|UtcTime|date|Time in UTC when event was created|`4/11/18 5:25`|
|sysmon_configuration|Configuration|string|name of the sysmon config file being updated|`C:\Tools\sysmon_config\StartLogging.xml`|
|sysmon_configuration_hash|ConfigurationFileHash|string|hash (SHA1) of the sysmon config file being updated|`SHA1=647B4A564FA2684252EFB1EA550A06EC432418C8`|

## Resources
* [TrustedSec Sysmon Community Guide](https://github.com/trustedsec/SysmonCommunityGuide/blob/master/sysmon-events.md#service-state-change)
