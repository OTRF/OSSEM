# Event ID 8: CreateRemoteThread

## Description
The CreateRemoteThread event detects when a process creates a thread in another process. This technique is used by malware to inject code and hide in other processes. The event indicates the source and target process. It gives information on the code that will be run in the new thread: StartAddress, StartModule and StartFunction. Note that StartModule and StartFunction fields are inferred, they might be empty if the starting address is outside loaded modules or known exported functions.<a href="https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-8-createremotethread">https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-8-createremotethread</a>

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|tag|RuleName|TBD|string|custom tag mapped to event. i.e ATT&CK technique ID|T1114|
|event_date_creation|UtcTime|TBD|date|Time in UTC when event was created|4/11/18 5:25|
|process_guid|SourceProcessGuid|TBD|string|Process Guid of the source process that created a thread in another process|{A98268C1-9586-5ACD-0000-001070A20000}|
|process_id|SourceProcessId|TBD|integer|Process ID used by the os to identify the source process that created a thread in another process|684|
|process_name|SourceImage|TBD|string|The name of the executable for the source process that created a thread in another process|csrss.exe|
|process_path|SourceImage|TBD|string|File path of the source process that created a thread in another process|C:\Windows\System32\csrss.exe|
|target_process_guid|TargetProcessGuid|TBD|string|Process Guid of the target process|{A98268C1-9C2E-5ACD-0000-00100266AB00}|
|target_process_id|TargetProcessId|TBD|integer|Process ID used by the os to identify the target process|240|
|target_process_name|TargetImage|TBD|string|File name of the target process|cmd.exe|
|target_process_path|TargetImage|TBD|string|File path of the target process|C:\Windows\System32\cmd.exe|
|thread_new_id|NewThreadId|TBD|integer|Id of the new thread created in the target process|2336|
|thread_start_address|StartAddress|TBD|string|New thread start address|0x00007FFA356A7E40|
|thread_start_module|StartModule|TBD|string|Start module determined from thread start address mapping to PEB loaded module list|C:\WINDOWS\System32\KERNELBASE.dll|
|thread_start_function|StartFunction|TBD|string|Start function is reported if exact match to function in image export table|CtrlRoutine|

## Resources
* [Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-8-createremotethread)
* [TrustedSec Sysmon Community Guide](https://github.com/trustedsec/SysmonCommunityGuide/blob/master/create-remote-thread.md)
