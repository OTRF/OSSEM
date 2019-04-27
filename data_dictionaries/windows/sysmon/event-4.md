---
title: Event ID 4 - Sysmon service state changed
description: The service state change event reports the state of the Sysmon service (started or stopped).
log.type: sysmon
sysmon.version: 9.01
sysmon.rule: cannot be filtered
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/26/2019
---

# Event ID 4: Sysmon service state changed

## Description
The service state change event reports the state of the Sysmon service (started or stopped).[Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-4-sysmon-service-state-changed)

## Event Log Illustration

<img src="https://github.com/Cyb3rWard0g/OSSEM/blob/master/resources/images/event-4.png" alt="Event 4 illustration" width="625" height="625">

## Event XML:

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385f-c22a-43e0-bf4c-06f5698ffbd9}" /> 
    <EventID>4</EventID> 
    <Version>3</Version> 
    <Level>4</Level> 
    <Task>4</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2019-04-27T00:11:19.522529500Z" /> 
    <EventRecordID>3606988</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="2332" ThreadID="3784" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>WARDOG.RIVENDELL.local</Computer> 
    <Security UserID="S-1-5-18" /> 
  </System>
  <EventData>
    <Data Name="UtcTime">2019-04-27 00:11:19.522</Data> 
    <Data Name="State">Started</Data> 
    <Data Name="Version">9.01</Data> 
    <Data Name="SchemaVersion">4.20</Data> 
  </EventData>
</Event>
```

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	event_creation_time	|	UtcTime	|	date	|	Time in UTC when event was created	|	4/11/18 5:36	|
|	service_state	|	State	|	string	|	sysmon service state (i.e. stopped)	|	Stopped	|
|	file_version	|	Version	|	string	|	sysmon version	|	7.01	|
|	sysmon_schema_version	|	SchemaVersion	|	string	|	sysmon config schema version	|	4	|