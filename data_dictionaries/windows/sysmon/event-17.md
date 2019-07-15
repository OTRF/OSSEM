---
title: Event ID 17 - PipeEvent (Pipe Created)
description: This event generates when a named pipe is created.
log.type: sysmon
sysmon.version: 10.0
sysmon.rule: PipeEvent
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/26/2019
---

# Event ID 17: PipeEvent (Pipe Created)

## Description
This event generates when a named pipe is created. Malware often uses named pipes for interprocess communication.[Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-17-pipeevent-pipe-created)

## Event Log Illustration

<img src="https://github.com/Cyb3rWard0g/OSSEM/blob/master/resources/images/event-17.png" alt="Event 17 illustration" width="625" height="625">

## Event XML

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385f-c22a-43e0-bf4c-06f5698ffbd9}" /> 
    <EventID>17</EventID> 
    <Version>1</Version> 
    <Level>4</Level> 
    <Task>17</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2019-04-27T00:11:22.711620600Z" /> 
    <EventRecordID>3611610</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="2332" ThreadID="3784" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>WARDOG.RIVENDELL.local</Computer> 
    <Security UserID="S-1-5-18" /> 
  </System>
  <EventData>
    <Data Name="RuleName" /> 
    <Data Name="UtcTime">2019-04-27 00:11:22.672</Data> 
    <Data Name="ProcessGuid">{1c9fdc81-9e18-5cc3-0000-001021790100}</Data> 
    <Data Name="ProcessId">1340</Data> 
    <Data Name="PipeName">\browser</Data> 
    <Data Name="Image">C:\WINDOWS\system32\svchost.exe</Data> 
  </EventData>
</Event>
```

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
| tag	|	RuleName |	string	| custom tag mapped to event. i.e ATT&CK technique ID	|	T1114 |
|	event_date_creation	|	UtcTime	|	date	|	Time in UTC when event was created	|	4/11/18 6:21	|
|	process_guid	|	ProcessGuid	|	string	|	Process Guid of the process that created the pipe	|	{A98268C1-A968-5ACD-0000-0010BD4EC200}	|
|	process_id	|	ProcessId	|	integer	|	Process ID used by the os to identify the process that created the pipe	|	1224	|
|	pipe_name	|	PipeName	|	string	|	Name of the pipe created	|	Anonymous Pipe	|
|	process_name	|	Image	|	string	|	File path of the process that created the pipe	|	C:\WINDOWS\system32\cmd.exe	|
| event_type | EventType | string | ConnectType | ConnectType |