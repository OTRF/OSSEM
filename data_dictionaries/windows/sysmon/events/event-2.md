# Event ID 2: A process changed a file creation time

## Description
The change file creation time event is registered when a file creation time is explicitly modified by a process. This event helps tracking the real creation time of a file. Attackers may change the file creation time of a backdoor to make it look like it was installed with the operating system. Note that many processes legitimately change the creation time of a file; it does not necessarily indicate malicious activity.<a href="https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-2-a-process-changed-a-file-creation-time">https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-2-a-process-changed-a-file-creation-time</a>

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|event_date_creation|UtcTime|TBD|date|Time in UTC when event was created|4/11/18 5:04|
|process_guid|ProcessGuid|TBD|string|Process Guid of the process that changed the file creation time|{A98268C1-975A-5ACD-0000-0010DB073A00}|
|process_id|ProcessId|TBD|integer|Process ID used by the os to identify the process changing the file creation time|1252|
|process_name|Image|TBD|string|File name of the process that changed the file creation time|powershell.exe|
|process_path|Image|TBD|string|File path of the process that changed the file creation time|C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe|
|file_name|TargetFilename|TBD|string|full path name of the file|C:\Users\wardog\AppData\Roaming\Microsoft\Windows\Recent\CustomDestinations\7G23PHTPHSQ3S2RVKKPS.temp|
|file_date_creation|CreationUtcTime|TBD|date|new creation time of the file|11/13/17 16:57|
|file_previous_date_creation|PreviousCreationUtcTime|TBD|date|previous creation time of the file|4/11/18 5:04|

## Resources
* [Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-2-a-process-changed-a-file-creation-time)
* [TrustedSec Sysmon Community Guide](https://github.com/trustedsec/SysmonCommunityGuide/blob/master/file-create-time-change.md)
