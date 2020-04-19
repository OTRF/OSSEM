---
title: Event ID 16 - Sysmon Config State Changed
description: This event logs when the local sysmon configuration is updated.
log.type: sysmon
sysmon.version: 9.01
sysmon.rule: cannot be filtered
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/26/2019
---

# Event ID 16 - Sysmon Config State Changed

## Description
This event logs when the local sysmon configuration is updated.

## Event Log Illustration

<img src="https://github.com/Cyb3rWard0g/OSSEM/blob/master/resources/images/event-16.png" alt="Event 16 illustration" width="625" height="625">

## Event XML

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385f-c22a-43e0-bf4c-06f5698ffbd9}" /> 
    <EventID>16</EventID> 
    <Version>3</Version> 
    <Level>4</Level> 
    <Task>16</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2019-04-27T00:48:17.287470500Z" /> 
    <EventRecordID>3611662</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="6988" ThreadID="5844" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>WARDOG.RIVENDELL.local</Computer> 
    <Security UserID="S-1-5-21-1727583317-3931901456-1912079981-1119" /> 
  </System>
  <EventData>
    <Data Name="UtcTime">2019-04-27 00:48:17.287</Data> 
    <Data Name="Configuration">c:\Users\cbrown\Downloads\start_logging.xml</Data> 
    <Data Name="ConfigurationFileHash">SHA1=803AC0F31896AC15B187E6B3FB23494852D1DBE1</Data> 
  </EventData>
</Event>
```

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
| @timestamp                | UtcTime               | date   | Time in UTC when event was created                  | 2020-04-01 09:01:01.576                       |
| sysmon_configuration      | Configuration         | string | name of the sysmon config file being updated        | C:\Tools\sysmon_config\StartLogging.xml       |
| sysmon_configuration_hash | ConfigurationFileHash | string | hash (SHA1) of the sysmon config file being updated | SHA1=647B4A564FA2684252EFB1EA550A06EC432418C8 |
