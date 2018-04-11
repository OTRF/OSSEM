---
title: Event ID 9 - RawAccessRead
description: The RawAccessRead event detects when a process conducts reading operations from the drive using the \\.\ denotation.
log.type: sysmon
sysmon.version: 7.01
sysmon.rule: RawAccessRead
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/11/2018
---

# Event ID 9: RawAccessRead

## Description
The RawAccessRead event detects when a process conducts reading operations from the drive using the \\.\ denotation. This technique is often used by malware for data exfiltration of files that are locked for reading, as well as to avoid file access auditing tools. The event indicates the source process and target device.[Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-9-rawaccessread)

## Event Log Illustration

![alt text](/resources/images/event-9.png "Event 9 illustration")

## Event XML

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385F-C22A-43E0-BF4C-06F5698FFBD9}" /> 
    <EventID>9</EventID> 
    <Version>2</Version> 
    <Level>4</Level> 
    <Task>9</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2018-04-11T05:51:46.575087700Z" /> 
    <EventRecordID>11758084</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="6028" ThreadID="4132" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>DESKTOP-WARDOG</Computer> 
    <Security UserID="S-1-5-18" /> 
  </System>
  <EventData>
    <Data Name="UtcTime">2018-04-11 05:51:46.571</Data> 
    <Data Name="ProcessGuid">{A98268C1-959B-5ACD-0000-0010EFD50200}</Data> 
    <Data Name="ProcessId">2708</Data> 
    <Data Name="Image">C:\Windows\System32\svchost.exe</Data> 
    <Data Name="Device">\Device\HarddiskVolume2</Data> 
    </EventData>
</Event>
```