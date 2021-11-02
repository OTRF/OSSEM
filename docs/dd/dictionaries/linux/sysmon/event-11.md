# Event ID 11: FileCreate
###### Version: 4.81

## Description
**File create** operations are logged when a file is created or overwritten. This event is useful for monitoring autostart locations, like the temporary and download directories, which are common places malware drops during initial infection.

## Data Dictionary
|Field Name|Type|Description|Sample Value|
|---|---|---|---|
|RuleName|string|custom tag mapped to event. i.e ATT&CK technique ID|`T1114`|
|UtcTime|date|Time in UTC when event was created|`2021-10-13T20:06:22.6590000Z`|
|ProcessGuid|string|Process Guid of the process that created the file|`{A98268C1-958A-5ACD-0000-0010C62F0100}`|
|ProcessId|integer|Process ID used by the os to identify the process that created the file.|`1044`|
|Image|string|File path of the process that created the file|`/usr/sbin/rsyslogd`|
|TargetFilename|string|Name of the file|`/run/rsyslogd.pid.tmp`|
|CreationUtcTime|date|File creation time|`2021-10-14T22:39:15.5650000Z`|
|User|string|user that created the file|`root`|
