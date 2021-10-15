# Event ID 9: RawAccessRead
###### Version: 4.81

## Description
The **RawAccessRead** event detects when a process conducts reading operations from the drive. This technique is often used by malware for data exfiltration of files that are locked for reading, as well as to avoid file access auditing tools. The event indicates the source process and target device.

## Data Dictionary
|Field Name|Type|Description|Sample Value|
|---|---|---|---|
|RuleName|string|custom tag mapped to event. i.e ATT&CK technique ID|`T1114`|
|UtcTime|date|Time in UTC when event was created|`2021-10-13T20:14:04.3360000Z`|
|ProcessGuid|string|Process Guid of the process that conducted reading operations from the drive|`{A98268C1-959B-5ACD-0000-0010EFD50200}`|
|ProcessId|integer|Process ID used by the os to identify the process that conducted reading operations from the drive|`2708`|
|Image|string|File path of the process that conducted reading operations from the drive|`/sbin/dumpe2fs`|
|Device|string|Target device|`/dev/sda1`|
|User|string|Name of the account that read.|`root`|
