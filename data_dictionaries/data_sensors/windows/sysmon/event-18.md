---
title: Event ID 18 - PipeEvent (Pipe Connected)
description: This event logs when a named pipe connection is made between a client and a server.
log.type: sysmon
sysmon.version: 7.01
sysmon.rule: PipeEvent
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/11/2018
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
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385F-C22A-43E0-BF4C-06F5698FFBD9}" /> 
    <EventID>18</EventID> 
    <Version>1</Version> 
    <Level>4</Level> 
    <Task>18</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2018-04-11T06:28:22.963327100Z" /> 
    <EventRecordID>11773738</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="6028" ThreadID="4132" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>DESKTOP-WARDOG</Computer> 
    <Security UserID="S-1-5-18" /> 
  </System>
  <EventData>
    <Data Name="UtcTime">2018-04-11 06:28:22.960</Data> 
    <Data Name="ProcessGuid">{A98268C1-959E-5ACD-0000-0010236E0300}</Data> 
    <Data Name="ProcessId">1896</Data> 
    <Data Name="PipeName">\srvsvc</Data> 
    <Data Name="Image">C:\WINDOWS\system32\wbem\wmiprvse.exe</Data> 
  </EventData>
</Event>
```