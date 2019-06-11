---
title: Event ID 18 - PipeEvent (Pipe Connected)
description: This event logs when a named pipe connection is made between a client and a server.
log.type: sysmon
sysmon.version: 9.01
sysmon.rule: PipeEvent
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/26/2019
---

# Event ID 18: PipeEvent (Pipe Connected)

## Description
This event logs when a named pipe connection is made between a client and a server.[Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-18-pipeevent-pipe-connected)

## Event Log Illustration

<img src="https://github.com/Cyb3rWard0g/OSSEM/blob/master/resources/images/event-18.png" alt="Event 18 illustration" width="625" height="625">

## Event XML

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385f-c22a-43e0-bf4c-06f5698ffbd9}" /> 
    <EventID>18</EventID> 
    <Version>1</Version> 
    <Level>4</Level> 
    <Task>18</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2019-04-27T00:11:22.672074000Z" /> 
    <EventRecordID>3611609</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="2332" ThreadID="3784" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>WARDOG.RIVENDELL.local</Computer> 
    <Security UserID="S-1-5-18" /> 
  </System>
  <EventData>
    <Data Name="RuleName" /> 
    <Data Name="UtcTime">2019-04-27 00:11:22.641</Data> 
    <Data Name="ProcessGuid">{1c9fdc81-9e18-5cc3-0000-001021790100}</Data> 
    <Data Name="ProcessId">1340</Data> 
    <Data Name="PipeName">\srvsvc</Data> 
    <Data Name="Image">C:\WINDOWS\system32\svchost.exe</Data> 
  </EventData>
</Event>
```

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	event_date_creation	|	UtcTime	|	date	|	Time in UTC when event was created	|	4/11/18 6:28	|
|	process_guid	|	ProcessGuid	|	string	|	Process Guid of the process that connected the pipe	|	{A98268C1-959E-5ACD-0000-0010236E0300}	|
|	process_id	|	ProcessId	|	integer	|	Process ID used by the os to identify the process that connected the pipe	|	1896	|
|	pipe_name	|	PipeName	|	string	|	Name of the pipe connecged	|	\srvsvc	|
|	process_name	|	Image	|	string	|	File path of the process that connected the pipe	|	C:\WINDOWS\system32\wbem\wmiprvse.exe	|