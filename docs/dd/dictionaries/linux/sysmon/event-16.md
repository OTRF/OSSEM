# Event ID 16 - Sysmon Config State Changed
###### Version: 4.81

## Description
This event logs when the local **sysmon configuration is updated**.

## Data Dictionary
|Field Name|Type|Description|Sample Value|
|---|---|---|---|
|UtcTime|date|Time in UTC when event was created|`2021-10-13T21:04:30.3520000Z`|
|Configuration|string|name of the sysmon config file being updated|`config2.xml`|
|ConfigurationFileHash|string|hash (SHA1) of the sysmon config file being updated|``|
