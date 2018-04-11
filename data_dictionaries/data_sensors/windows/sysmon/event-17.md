---
title: Event ID 17 - PipeEvent (Pipe Created)
description: This event generates when a named pipe is created.
log.type: sysmon
sysmon.version: 7.01
sysmon.rule: PipeEvent
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/11/2018
---

# Event ID 17: PipeEvent (Pipe Created)

## Description
This event generates when a named pipe is created. Malware often uses named pipes for interprocess communication.[Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-17-pipeevent-pipe-created)

## Event Log Illustration

![alt text](/OSSEM/resources/images/event-17.png "Event 17 illustration")

## Event XML

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385F-C22A-43E0-BF4C-06F5698FFBD9}" /> 
    <EventID>17</EventID> 
    <Version>1</Version> 
    <Level>4</Level> 
    <Task>17</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2018-04-11T06:21:28.950312900Z" /> 
    <EventRecordID>11769418</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="6028" ThreadID="4132" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>DESKTOP-WARDOG</Computer> 
    <Security UserID="S-1-5-18" /> 
  </System>
  <EventData>
    <Data Name="UtcTime">2018-04-11 06:21:28.947</Data> 
    <Data Name="ProcessGuid">{A98268C1-A968-5ACD-0000-0010BD4EC200}</Data> 
    <Data Name="ProcessId">1224</Data> 
    <Data Name="PipeName"><Anonymous Pipe></Data> 
    <Data Name="Image">C:\WINDOWS\system32\cmd.exe</Data> 
  </EventData>
</Event>
```