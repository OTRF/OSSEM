# Event ID 5: Process terminated
###### Version: 4.32

## Description
The **process terminate** event reports when a process terminates. It provides the UtcTime, ProcessGuid and ProcessId of the process.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|tag|RuleName|string|custom tag mapped to event. i.e ATT&CK technique ID|`T1114`|
|event_date_creation|UtcTime|date|Time in UTC when event was created|`4/11/18 5:37`|
|process_guid|ProcessGuid|string|Process Guid of the process that terminated|`{A98268C1-9ECD-5ACD-0000-0010EF6BAF00}`|
|process_id|ProcessId|integer|Process ID used by the os to identify the process that terminated|`2428`|
|process_path|Image|string|File path of the process that terminated|`C:\Windows\System32\backgroundTaskHost.exe`|

## References
* [Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-5-process-terminated)
* [TrustedSec Sysmon Community Guide](https://github.com/trustedsec/SysmonCommunityGuide/blob/master/process-termination.md)
