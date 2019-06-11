---
title: Event ID 8 - CreateRemoteThread
description: The CreateRemoteThread event detects when a process creates a thread in another process.
log.type: sysmon
sysmon.version: 9.01
sysmon.rule: CreateRemoteThread
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/26/2019
---

# Event ID 8: CreateRemoteThread

## Description
The CreateRemoteThread event detects when a process creates a thread in another process. This technique is used by malware to inject code and hide in other processes. The event indicates the source and target process. It gives information on the code that will be run in the new thread: StartAddress, StartModule and StartFunction. Note that StartModule and StartFunction fields are inferred, they might be empty if the starting address is outside loaded modules or known exported functions.[Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-8-createremotethread)

## Event Log Illustration

!<img src="https://github.com/Cyb3rWard0g/OSSEM/blob/master/resources/images/event-8.png" alt="Event 8 illustration" width="625" height="625">

## Event XML

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385f-c22a-43e0-bf4c-06f5698ffbd9}" /> 
    <EventID>8</EventID> 
    <Version>2</Version> 
    <Level>4</Level> 
    <Task>8</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2019-04-27T00:10:32.379011500Z" /> 
    <EventRecordID>3606757</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="2336" ThreadID="3652" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>DESKTOP-LFD11QP.RIVENDELL.local</Computer> 
    <Security UserID="S-1-5-18" /> 
  </System>
  <EventData>
    <Data Name="RuleName" /> 
    <Data Name="UtcTime">2019-04-27 00:10:32.363</Data> 
    <Data Name="SourceProcessGuid">{1c9fdc81-9d71-5cc3-0000-00109cad0000}</Data> 
    <Data Name="SourceProcessId">604</Data> 
    <Data Name="SourceImage">C:\Windows\System32\csrss.exe</Data> 
    <Data Name="TargetProcessGuid">{1c9fdc81-9d71-5cc3-0000-0010bbbc0000}</Data> 
    <Data Name="TargetProcessId">804</Data> 
    <Data Name="TargetImage">C:\Windows\System32\services.exe</Data> 
    <Data Name="NewThreadId">6992</Data> 
    <Data Name="StartAddress">0x00007FFB26853970</Data> 
    <Data Name="StartModule">C:\WINDOWS\System32\KERNELBASE.dll</Data> 
    <Data Name="StartFunction">CtrlRoutine</Data> 
  </EventData>
</Event>
```

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	event_date_creation	|	UtcTime	|	date	|	Time in UTC when event was created	|	4/11/18 5:25	|
|	process_guid	|	SourceProcessGuid	|	string	|	Process Guid of the source process that created a thread in another process	|	{A98268C1-9586-5ACD-0000-001070A20000}	|
|	process_id	|	SourceProcessId	|	integer	|	Process ID used by the os to identify the source process that created a thread in another process	|	684	|
|	process_name	|	SourceImage	|	string	|	The name of the executable for the source process that created a thread in another process	|	csrss.exe	|
|	process_path	|	SourceImage	|	string	|	File path of the source process that created a thread in another process	|	C:\Windows\System32\csrss.exe	|
|	target_process_guid	|	TargetProcessGuid	|	string	|	Process Guid of the target process	|	{A98268C1-9C2E-5ACD-0000-00100266AB00}	|
|	target_process_id	|	TargetProcessId	|	integer	|	Process ID used by the os to identify the target process	|	240	|
|	target_process_name	|	TargetImage	|	string	|	File name of the target process	|	cmd.exe	|
|	target_process_path	|	TargetImage	|	string	|	File path of the target process	|	C:\Windows\System32\cmd.exe	|
|	thread_new_id	|	NewThreadId	|	integer	|	Id of the new thread created in the target process	|	2336	|
|	thread_start_address	|	StartAddress	|	string	|	New thread start address	|	0x00007FFA356A7E40	|
|	thread_start_module	|	StartModule	|	string	|	Start module determined from thread start address mapping to PEB loaded module list	|	C:\WINDOWS\System32\KERNELBASE.dll	|
|	thread_start_function	|	StartFunction	|	string	|	Start function is reported if exact match to function in image export table	|	CtrlRoutine	|