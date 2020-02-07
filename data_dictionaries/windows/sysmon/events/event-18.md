# Event ID 18: PipeEvent (Pipe Connected)

## Description
This event logs when a named pipe connection is made between a client and a server.<a href="https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-18-pipeevent-pipe-connected">https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-18-pipeevent-pipe-connected</a>

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|tag|RuleName|TBD|string|custom tag mapped to event. i.e ATT&CK technique ID|T1114|
|event_date_creation|UtcTime|TBD|date|Time in UTC when event was created|4/11/18 6:28|
|process_guid|ProcessGuid|TBD|string|Process Guid of the process that connected the pipe|{A98268C1-959E-5ACD-0000-0010236E0300}|
|process_id|ProcessId|TBD|integer|Process ID used by the os to identify the process that connected the pipe|1896|
|pipe_name|PipeName|TBD|string|Name of the pipe connecged|\srvsvc|
|process_name|Image|TBD|string|File name of the process that connected the pipe|wmiprvse.exe|
|process_path|Image|TBD|string|File path of the process that connected the pipe|C:\WINDOWS\system32\wbem\wmiprvse.exe|

## Resources
* [Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-18-pipeevent-pipe-connected)
* [TrustedSec Sysmon Community Guide](https://github.com/trustedsec/SysmonCommunityGuide/blob/master/named-pipes.md)
