---
title: Event ID 12 - RegistryEvent (Object create and delete)
description: Registry key and value create and delete operations map to this event type.
log.type: sysmon
sysmon.version: 9.01
sysmon.rule: RegistryEvent
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/26/2019
---

# Event ID 12: RegistryEvent (Object create and delete)

## Description
Registry key and value create and delete operations map to this event type, which can be useful for monitoring for changes to Registry autostart locations, or specific malware registry modifications.[Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-12-registryevent-object-create-and-delete)

## Event Log Illustration

<img src="https://github.com/Cyb3rWard0g/OSSEM/blob/master/resources/images/event-12.png" alt="Event 12 illustration" width="625" height="625">

## Event XML

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385f-c22a-43e0-bf4c-06f5698ffbd9}" /> 
    <EventID>12</EventID> 
    <Version>2</Version> 
    <Level>4</Level> 
    <Task>12</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2019-04-27T00:11:22.786058200Z" /> 
    <EventRecordID>3611636</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="2332" ThreadID="3784" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>WARDOG.RIVENDELL.local</Computer> 
    <Security UserID="S-1-5-18" /> 
  </System>
  <EventData>
    <Data Name="RuleName" /> 
    <Data Name="EventType">CreateKey</Data> 
    <Data Name="UtcTime">2019-04-27 00:11:22.753</Data> 
    <Data Name="ProcessGuid">{1c9fdc81-9e27-5cc3-0000-0010116d0600}</Data> 
    <Data Name="ProcessId">3832</Data> 
    <Data Name="Image">C:\WINDOWS\system32\WerFault.exe</Data> 
    <Data Name="TargetObject">HKLM\System\CurrentControlSet\Control\Hvsi</Data> 
  </EventData>
</Event>
```

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	event_type	|	EventType	|	string	|	registry event. Either Create or Delete	|	CreateKey	|
|	event_date_creation	|	UtcTime	|	date	|	Time in UTC when event was created	|	4/11/18 5:25	|
|	process_guid	|	ProcessGuid	|	string	|	Process Guid of the process that created or deleted a registry key	|	{A98268C1-9595-5ACD-0000-0010C2380200}	|
|	process_id	|	ProcessId	|	integer	|	Process ID used by the os to identify the process that created or deleted a registry key	|	2052	|
|	process_name	|	Image	|	string	|	File path of the process that created or deleted a registry key	|	C:\Program Files\Common Files\Microsoft Shared\ClickToRun\OfficeClickToRun.exe	|
|	registry_key_path	|	TargetObject	|	string	|	complete path of the registry key	|	HKU.DEFAULT\Software\Microsoft\Office\16.0\Common	|