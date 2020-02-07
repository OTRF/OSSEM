# Event ID 5: Process terminated

## Description
The process terminate event reports when a process terminates. It provides the UtcTime, ProcessGuid and ProcessId of the process.<a href="https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-5-process-terminated">https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-5-process-terminated</a>

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|tag|RuleName|TBD|string|custom tag mapped to event. i.e ATT&CK technique ID|T1114|
|event_date_creation|UtcTime|TBD|date|Time in UTC when event was created|4/11/18 5:37|
|process_guid|ProcessGuid|TBD|string|Process Guid of the process that terminated|{A98268C1-9ECD-5ACD-0000-0010EF6BAF00}|
|process_id|ProcessId|TBD|integer|Process ID used by the os to identify the process that terminated|2428|
|process_name|Image|TBD|string|The name of the executable of the process that terminated|backgroundTaskHost.exe|
|process_path|Image|TBD|string|File path of the process that terminated|C:\Windows\System32\backgroundTaskHost.exe|

## Resources
* [Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-5-process-terminated)
* [TrustedSec Sysmon Community Guide](https://github.com/trustedsec/SysmonCommunityGuide/blob/master/process-termination.md)
