---
title: Event ID 16 - Sysmon Config State Changed
description: This event logs when the local sysmon configuration is updated.
log.type: sysmon
sysmon.version: 7.01
sysmon.rule: cannot be filtered
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/11/2018
---

# Event ID 16 - Sysmon Config State Changed

## Description
This event logs when the local sysmon configuration is updated.

## Event Log Illustration

![alt text](/resources/images/event-16.png "Event 16 illustration")

## Event XML

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385F-C22A-43E0-BF4C-06F5698FFBD9}" /> 
    <EventID>16</EventID> 
    <Version>3</Version> 
    <Level>4</Level> 
    <Task>16</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2018-04-11T06:22:44.899735300Z" /> 
    <EventRecordID>11771907</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="424" ThreadID="5472" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>DESKTOP-WARDOG</Computer> 
    <Security UserID="S-1-5-21-3825400013-1856045589-1834093677-1001" /> 
  </System>
  <EventData>
    <Data Name="UtcTime">2018-04-11 06:22:44.887</Data> 
    <Data Name="Configuration">C:\Tools\sysmon_config\StartLogging.xml</Data> 
    <Data Name="ConfigurationFileHash">SHA1=647B4A564FA2684252EFB1EA550A06EC432418C8</Data> 
  </EventData>
</Event>
```