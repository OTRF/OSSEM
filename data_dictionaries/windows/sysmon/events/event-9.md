# Event ID 9: RawAccessRead

## Description
The RawAccessRead event detects when a process conducts reading operations from the drive using the .\ denotation. This technique is often used by malware for data exfiltration of files that are locked for reading, as well as to avoid file access auditing tools. The event indicates the source process and target device.<a href="https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-9-rawaccessread">https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-9-rawaccessread</a>

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|tag|RuleName|string|custom tag mapped to event. i.e ATT&CK technique ID|`T1114`|
|event_date_creation|UtcTime|date|Time in UTC when event was created|`4/11/18 5:51`|
|process_guid|ProcessGuid|string|Process Guid of the process that conducted reading operations from the drive|`{A98268C1-959B-5ACD-0000-0010EFD50200}`|
|process_id|ProcessId|integer|Process ID used by the os to identify the process that conducted reading operations from the drive|`2708`|
|process_name|Image|string|File name of the process that conducted reading operations from the drive|`svchost.exe`|
|process_path|Image|string|File path of the process that conducted reading operations from the drive|`C:\Windows\System32\svchost.exe`|
|target_device|Device|string|Target device|`\Device\HarddiskVolume2`|

## Resources
* [Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-9-rawaccessread)
* [TrustedSec Sysmon Community Guide](https://github.com/trustedsec/SysmonCommunityGuide/blob/master/raw-access-read.md)
