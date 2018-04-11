---
title: Event ID 4 - Sysmon service state changed
description: The service state change event reports the state of the Sysmon service (started or stopped).
log.type: sysmon
sysmon.version: 7.01
sysmon.rule: cannot be filtered
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/11/2018
---

# Event ID 4: Sysmon service state changed

## Description
The service state change event reports the state of the Sysmon service (started or stopped).[Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-4-sysmon-service-state-changed)

## Event Log Illustration

![alt text](/resources/images/event-4.png "Event 4 illustration")

## Event XML:

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385F-C22A-43E0-BF4C-06F5698FFBD9}" /> 
    <EventID>4</EventID> 
    <Version>3</Version> 
    <Level>4</Level> 
    <Task>4</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2018-04-11T05:36:20.242010600Z" /> 
    <EventRecordID>11753525</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="2152" ThreadID="2156" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>DESKTOP-WARDOG</Computer> 
    <Security UserID="S-1-5-18" /> 
  </System>
  <EventData>
    <Data Name="UtcTime">2018-04-11 05:36:20.231</Data> 
    <Data Name="State">Stopped</Data> 
    <Data Name="Version">7.01</Data> 
    <Data Name="SchemaVersion">4.00</Data> 
  </EventData>
</Event>
```