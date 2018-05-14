---
title: Event ID 14 - RegistryEvent (Key and Value Rename)
description: Registry key and value rename operations map to this event type.
log.type: sysmon
sysmon.version: 7.01
sysmon.rule: RegistryEvent
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/11/2018
---

# Event ID 14: RegistryEvent (Key and Value Rename)

## Description
Registry key and value rename operations map to this event type, recording the new name of the key or value that was renamed.[Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-14-registryevent-key-and-value-rename)

## Event Log Illustration

<img src="https://github.com/Cyb3rWard0g/OSSEM/blob/master/resources/images/event-14.png" alt="Event 14 illustration" width="625" height="625">

## Event XML

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385F-C22A-43E0-BF4C-06F5698FFBD9}" /> 
    <EventID>14</EventID> 
    <Version>2</Version> 
    <Level>4</Level> 
    <Task>14</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2018-04-11T06:14:57.050339700Z" /> 
    <EventRecordID>11765950</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="6028" ThreadID="4132" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>DESKTOP-WARDOG</Computer> 
    <Security UserID="S-1-5-18" /> 
  </System>
  <EventData>
    <Data Name="EventType">RenameKey</Data> 
    <Data Name="UtcTime">2018-04-11 06:14:57.040</Data> 
    <Data Name="ProcessGuid">{A98268C1-A7BF-5ACD-0000-00106B2EBE00}</Data> 
    <Data Name="ProcessId">2676</Data> 
    <Data Name="Image">C:\Windows\regedit.exe</Data> 
    <Data Name="TargetObject">HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\New Key #1</Data> 
    <Data Name="NewName">\REGISTRY\MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\hello</Data> 
  </EventData>
</Event>
```

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	event_type	|	EventType	|	string	|	registry event. Registry key and value renamed	|	RenameKey	|
|	event_creation_time	|	UtcTime	|	date	|	Time in UTC when event was created	|	4/11/18 6:04	|
|	process_guid	|	ProcessGuid	|	string	|	Process Guid of the process that renamed a registry value and key	|	{A98268C1-95F9-5ACD-0000-001025861000}	|
|	process_id	|	ProcessId	|	integer	|	Process ID used by the os to identify the process that renamed a registry value and key	|	4624	|
|	process_name	|	Image	|	string	|	File path of the process that renamed a registry value and key	|	C:\WINDOWS\Explorer.EXE	|
|	registry_key_path	|	TargetObject	|	string	|	complete path of the registry key	|	HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\New Key #1	|
|	registry_key_new_name	|	NewName	|	string	|	new name of the registry key	|	\REGISTRY\MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\hello	|