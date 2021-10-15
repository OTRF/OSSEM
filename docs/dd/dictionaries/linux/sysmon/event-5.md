# Event ID 5: Process terminated
###### Version: 4.81

## Description
The **process terminate** event reports when a process terminates. It provides the UtcTime, ProcessGuid and ProcessId of the process.

## Data Dictionary
|Field Name|Type|Description|Sample Value|
|---|---|---|---|
|RuleName|string|custom tag mapped to event. i.e ATT&CK technique ID|`T1114`|
|UtcTime|date|Time in UTC when event was created|`2021-10-13T20:06:22.6470000Z`|
|ProcessGuid|string|Process Guid of the process that terminated|`{A98268C1-9ECD-5ACD-0000-0010EF6BAF00}`|
|ProcessId|integer|Process ID used by the os to identify the process that terminated|`2428`|
|Image|string|File path of the process that terminated|`rsyslogd`|
|User|string|Name of the account that terminated the process.|`syslog`|
