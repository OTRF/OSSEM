---
title: Event ID 5 - Process terminated
description: The process terminate event reports when a process terminates.
log.type: sysmon
sysmon.version: 9.01
sysmon.rule: ProcessTerminate
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/26/2019
---

# Event ID 5: Process terminated

## Description
The process terminate event reports when a process terminates. It provides the UtcTime, ProcessGuid and ProcessId of the process.[Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-5-process-terminated)

## Event Log Illustration

<img src="https://github.com/Cyb3rWard0g/OSSEM/blob/master/resources/images/event-5.png" alt="Event 5 illustration" width="625" height="625">

## Event XML:

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385f-c22a-43e0-bf4c-06f5698ffbd9}" /> 
    <EventID>5</EventID> 
    <Version>3</Version> 
    <Level>4</Level> 
    <Task>5</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2019-04-27T00:50:17.341188700Z" /> 
    <EventRecordID>3620347</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="1432" ThreadID="6344" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>WARDOG.RIVENDELL.local</Computer> 
    <Security UserID="S-1-5-18" /> 
  </System>
  <EventData>
    <Data Name="RuleName" /> 
    <Data Name="UtcTime">2019-04-27 00:50:02.357</Data> 
    <Data Name="ProcessGuid">{1c9fdc81-a73a-5cc3-0000-001029ad5f00}</Data> 
    <Data Name="ProcessId">4472</Data> 
    <Data Name="Image">C:\Windows\System32\rundll32.exe</Data> 
  </EventData>
</Event>
```

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	event_creation_time	|	UtcTime	|	date	|	Time in UTC when event was created	|	4/11/18 5:37	|
|	process_guid	|	ProcessGuid	|	string	|	Process Guid of the process that terminated	|	{A98268C1-9ECD-5ACD-0000-0010EF6BAF00}	|
|	process_id	|	ProcessId	|	integer	|	Process ID used by the os to identify the process that terminated	|	2428	|
| process_name | Image | string | The name of the executable of the process that terminated | backgroundTaskHost.exe |
| process_path | Image | string | File path of the process that terminated | C:\Windows\System32\backgroundTaskHost.exe |