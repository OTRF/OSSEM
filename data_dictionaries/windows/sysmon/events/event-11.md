# Event ID 11: FileCreate

## Description
File create operations are logged when a file is created or overwritten. This event is useful for monitoring autostart locations, like the Startup folder, as well as temporary and download directories, which are common places malware drops during initial infection.<a href="https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-11-filecreate">https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-11-filecreate</a>

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|tag|RuleName|string|custom tag mapped to event. i.e ATT&CK technique ID|`T1114`|
|event_date_creation|UtcTime|date|Time in UTC when event was created|`4/11/18 6:01`|
|process_guid|ProcessGuid|string|Process Guid of the process that created the file|`{A98268C1-958A-5ACD-0000-0010C62F0100}`|
|process_id|ProcessId|integer|Process ID used by the os to identify the process that created the file (child)|`1044`|
|process_name|Image|string|File name of the process that created the file|`svchost.exe`|
|process_path|Image|string|File path of the process that created the file|`C:\WINDOWS\System32\svchost.exe`|
|file_name|TargetFilename|string|Name of the file|`C:\Windows\Prefetch\CONHOST.EXE-1F3E9D7E.pf`|
|file_date_creation|CreationUtcTime|date|File creation time|`12/4/17 17:38`|

## Resources
* [Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-11-filecreate)
* [TrustedSec Sysmon Community Guide](https://github.com/trustedsec/SysmonCommunityGuide/blob/master/file-create.md)
