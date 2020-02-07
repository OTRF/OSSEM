# Event ID 1: Process creation

## Description
The process creation event provides extended information about a newly created process. The full command line provides context on the process execution. The ProcessGUID field is a unique value for this process across a domain to make event correlation easier. The hash is a full hash of the file with the algorithms in the HashType field.<a href="https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-1-process-creation">https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-1-process-creation</a>

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|tag|RuleName|TBD|string|custom tag mapped to event. i.e ATT&CK technique ID|T1114|
|event_date_creation|UtcTime|TBD|date|Time in UTC when event was created|4/11/18 5:25|
|process_guid|ProcessGuid|TBD|string|Process Guid of the process that got spawned/created (child)|{A98268C1-9C2E-5ACD-0000-0010396CAB00}|
|process_id|ProcessId|TBD|integer|Process ID used by the os to identify the created process (child)|4756|
|process_name|Image|TBD|string|The name of the executable without full path related to the process being spawned/created in the event. Considered also the child or source process|conhost.exe|
|process_path|Image|TBD|string|File path of the process being spawned/created. Considered also the child or source process|C:\Windows\System32\conhost.exe|
|file_version|FileVersion|TBD|string|Version of the image associated with the main process (child)|10.0.16299.15 (WinBuild.160101.0800)|
|file_description|Description|TBD|string|Description of the image associated with the main process (child)|Console Window Host|
|file_product|Product|TBD|string|Product name the image associated with the main process (child) belongs to|Microsoft® Windows® Operating System|
|file_company|Company|TBD|string|Company name the image associated with the main process (child) belongs to|Microsoft Corporation|
|file_name_original|OriginalFileName|TBD|string|original file name|wuauclt.exe|
|process_command_line|CommandLine|TBD|string|Arguments which were passed to the executable associated with the main process|??\C:\WINDOWS\system32\conhost.exe 0xffffffff -ForceV1|
|file_current_directory|CurrentDirectory|TBD|string|The path without the name of the image associated with the process|C:\WINDOWS|
|user_name|User|TBD|string|Name of the account who created the process (child) . It usually contains domain name and user name (Parsed to show only username without the domain)|DESKTOP-WARDOG\wardog|
|user_logon_guid|LogonGuid|TBD|string|Logon GUID of the user who created the new process. Value that can help you correlate this event with others that contain the same Logon GUID (Sysmon Events)|{A98268C1-95F2-5ACD-0000-002019620F00}|
|user_logon_id|LogonId|TBD|integer|Login ID of the user who created the new process. Value that can help you correlate this event with others that contain the same Logon ID|0xf6219|
|user_session_id|TerminalSessionId|TBD|integer|ID of the session the user belongs to|1|
|process_integrity_level|IntegrityLevel|TBD|string|Integrity label assigned to a process|Medium|
|hash|Hashes|TBD|string|Hashes captured by sysmon driver|SHA1=B0BF5AC2E81BBF597FAD5F349FEEB32CAC449FA2, MD5=6A255BEBF3DBCD13585538ED47DBAFD7, SHA256=4668BB2223FFB983A5F1273B9E3D9FA2C5CE4A0F1FB18CA5C1B285762020073C, IMPHASH=2505BD03D7BD285E50CE89CEC02B333B|
|process_parent_guid|ParentProcessGuid|TBD|string|ProcessGUID of the process that spawned/created the main process (child)|{A98268C1-9C2E-5ACD-0000-00100266AB00}|
|process_parent_id|ParentProcessId|TBD|integer|Process ID of the process that spawned/created the main process (child)|240|
|process_parent_name|ParentImage|TBD|string|The name of the executable related to the target process|cmd.exe|
|process_parent_path|ParentImage|TBD|string|File path that spawned/created the main process|C:\Windows\System32\cmd.exe|
|process_parent_command_line|ParentCommandLine|TBD|string|Arguments which were passed to the executable associated with the parent process|C:\WINDOWS\system32\cmd.exe|

## Resources
* [Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-1-process-creation)
* [TrustedSec Sysmon Community Guide](https://github.com/trustedsec/SysmonCommunityGuide/blob/master/process-creation.md)
