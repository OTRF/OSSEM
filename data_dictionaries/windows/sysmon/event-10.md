---
title: Event ID 10 - ProcessAccess
description: The process accessed event reports when a process opens another process.
log.type: sysmon
sysmon.version: 7.01
sysmon.rule: ProcessAccess
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/11/2018
---

# Event ID 10: ProcessAccess

## Description
The process accessed event reports when a process opens another process, an operation that’s often followed by information queries or reading and writing the address space of the target process. This enables detection of hacking tools that read the memory contents of processes like Local Security Authority (Lsass.exe) in order to steal credentials for use in Pass-the-Hash attacks. Enabling it can generate significant amounts of logging if there are diagnostic utilities active that repeatedly open processes to query their state, so it generally should only be done so with filters that remove expected accesses.[Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-10-processaccess)

## Event Log Illustration

<img src="https://github.com/Cyb3rWard0g/OSSEM/blob/master/resources/images/event-10.png" alt="Event 10 illustration" width="625" height="625">

## Event XML

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385F-C22A-43E0-BF4C-06F5698FFBD9}" /> 
    <EventID>10</EventID> 
    <Version>3</Version> 
    <Level>4</Level> 
    <Task>10</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2018-04-11T05:18:56.568570800Z" /> 
    <EventRecordID>11739559</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="2152" ThreadID="3392" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>DESKTOP-WARDOG</Computer> 
    <Security UserID="S-1-5-18" /> 
  </System>
  <EventData>
    <Data Name="UtcTime">2018-04-11 05:18:56.566</Data> 
    <Data Name="SourceProcessGUID">{A98268C1-9587-5ACD-0000-001004C40000}</Data> 
    <Data Name="SourceProcessId">916</Data> 
    <Data Name="SourceThreadId">2804</Data> 
    <Data Name="SourceImage">C:\WINDOWS\system32\svchost.exe</Data> 
    <Data Name="TargetProcessGUID">{A98268C1-9597-5ACD-0000-00101D690200}</Data> 
    <Data Name="TargetProcessId">2288</Data> 
    <Data Name="TargetImage">C:\ProgramData\Microsoft\Windows Defender\platform\4.12.17007.18022-0\MsMpEng.exe</Data> 
    <Data Name="GrantedAccess">0x1000</Data> 
    <Data Name="CallTrace">C:\WINDOWS\SYSTEM32\ntdll.dll+a0344|C:\WINDOWS\System32\KERNELBASE.dll+64794|c:\windows\system32\lsm.dll+10e93|c:\windows\system32\lsm.dll+f9ea|C:\WINDOWS\System32\RPCRT4.dll+76d23|C:\WINDOWS\System32\RPCRT4.dll+d9390|C:\WINDOWS\System32\RPCRT4.dll+a81c|C:\WINDOWS\System32\RPCRT4.dll+273b4|C:\WINDOWS\System32\RPCRT4.dll+2654e|C:\WINDOWS\System32\RPCRT4.dll+26cfb|C:\WINDOWS\System32\RPCRT4.dll+3083f|C:\WINDOWS\System32\RPCRT4.dll+313a6|C:\WINDOWS\System32\RPCRT4.dll+2d12e|C:\WINDOWS\System32\RPCRT4.dll+2e853|C:\WINDOWS\System32\RPCRT4.dll+5cc68|C:\WINDOWS\SYSTEM32\ntdll.dll+365ce|C:\WINDOWS\SYSTEM32\ntdll.dll+34b46|C:\WINDOWS\System32\KERNEL32.DLL+11fe4|C:\WINDOWS\SYSTEM32\ntdll.dll+6efc1</Data> 
  </EventData>
</Event>
```

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	event_creation_time	|	UtcTime	|	date	|	Time in UTC when event was created	|	4/11/18 5:18	|
|	process_guid	|	SourceProcessGuid	|	string	|	Process Guid of the source process that opened another process. It is derived from a truncated part of the machine GUID, the process start-time and the process token ID.	|	{A98268C1-9587-5ACD-0000-001004C40000}	|
|	process_id	|	SourceProcessId	|	integer	|	Process ID used by the os to identify the source process that opened another process. Derived partially from the EPROCESS kernel structure	|	916	|
| thread_id	|	SourceThreadId	|	integer	|	ID of the specific thread inside of the source process that opened another process	|	2804	|
|	process_name	|	SourceImage	|	string	|	File name of the source process that created a thread in another process	|	svchost.exe	|
|	process_path	|	SourceImage	|	string	|	File path of the source process that created a thread in another process	|	C:\WINDOWS\system32\svchost.exe	|
|	target_process_guid	|	TargetProcessGuid	|	string	|	Process Guid of the target process	|	{A98268C1-9597-5ACD-0000-00101D690200}	|
|	target_process_id	|	TargetProcessId	|	integer	|	Process ID used by the os to identify the target process	|	2288	|
|	target_process_name	|	TargetImage	|	string	|	File name of the target process	|	4.12.17007.18022-0\MsMpEng.exe	|
|	target_process_path	|	TargetImage	|	string	|	File path of the target process	|	C:\ProgramData\Microsoft\Windows Defender\platform\4.12.17007.18022-0\MsMpEng.exe	|
|	process_granted_access	|	GrantedAccess	|	string	|	The access flags (bitmask) associated with the process rights requested for the target process	|	0x1000	|
|	process_call_trace	|	CallTrace | string	|	Stack trace of where open process is called. Included is the DLL and the relative virtual address of the functions in the call stack right before the open process call	|	C:\WINDOWS\SYSTEM32\ntdll.dll+a0344 \| C:\WINDOWS\System32\KERNELBASE.dll+64794\| c:\windows\system32\lsm.dll+10e93\| c:\windows\system32\lsm.dll+f9ea\| C:\WINDOWS\System32\RPCRT4.dll+76d23\| C:\WINDOWS\System32\RPCRT4.dll+d9390\| C:\WINDOWS\System32\RPCRT4.dll+a81c\| C:\WINDOWS\System32\RPCRT4.dll+273b4\| C:\WINDOWS\System32\RPCRT4.dll+2654e\| C:\WINDOWS\System32\RPCRT4.dll+26cfb\| C:\WINDOWS\System32\RPCRT4.dll+3083f\| C:\WINDOWS\System32\RPCRT4.dll+313a6\| C:\WINDOWS\System32\RPCRT4.dll+2d12e\| C:\WINDOWS\System32\RPCRT4.dll+2e853\| C:\WINDOWS\System32\RPCRT4.dll+5cc68\| C:\WINDOWS\SYSTEM32\ntdll.dll+365ce\| C:\WINDOWS\SYSTEM32\ntdll.dll+34b46\| C:\WINDOWS\System32\KERNEL32.DLL+11fe4\| C:\WINDOWS\SYSTEM32\ntdll.dll+6efc1	|
