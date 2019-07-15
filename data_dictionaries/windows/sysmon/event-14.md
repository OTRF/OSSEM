---
title: Event ID 14 - RegistryEvent (Key and Value Rename)
description: Registry key and value rename operations map to this event type.
log.type: sysmon
sysmon.version: 9.01
sysmon.rule: RegistryEvent
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/26/2019
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
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385f-c22a-43e0-bf4c-06f5698ffbd9}" /> 
    <EventID>14</EventID> 
    <Version>2</Version> 
    <Level>4</Level> 
    <Task>14</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2019-04-27T00:55:25.938142200Z" /> 
    <EventRecordID>3623832</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="1432" ThreadID="6344" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>WARDOG.RIVENDELL.local</Computer> 
    <Security UserID="S-1-5-18" /> 
  </System>
  <EventData>
    <Data Name="RuleName" /> 
    <Data Name="EventType">RenameKey</Data> 
    <Data Name="UtcTime">2019-04-27 00:55:25.926</Data> 
    <Data Name="ProcessGuid">{1c9fdc81-a79f-5cc3-0000-001084f96100}</Data> 
    <Data Name="ProcessId">2904</Data> 
    <Data Name="Image">C:\WINDOWS\regedit.exe</Data> 
    <Data Name="TargetObject">HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce\New Key #1</Data> 
    <Data Name="NewName">HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce\wardog</Data> 
  </EventData>
</Event>
```

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
| tag	|	RuleName |	string	| custom tag mapped to event. i.e ATT&CK technique ID	|	T1114 |
|	event_type	|	EventType	|	string	|	registry event. Registry key and value renamed	|	RenameKey	|
|	event_date_creation	|	UtcTime	|	date	|	Time in UTC when event was created	|	4/11/18 6:04	|
|	process_guid	|	ProcessGuid	|	string	|	Process Guid of the process that renamed a registry value and key	|	{A98268C1-95F9-5ACD-0000-001025861000}	|
|	process_id	|	ProcessId	|	integer	|	Process ID used by the os to identify the process that renamed a registry value and key	|	4624	|
|	process_name	|	Image	|	string	|	File name of the process that renamed a registry value and key	|	Explorer.EXE	|
|	process_path	|	Image	|	string	|	File path of the process that renamed a registry value and key	|	C:\WINDOWS\Explorer.EXE	|
|	registry_key_path	|	TargetObject	|	string	|	complete path of the registry key	|	HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\New Key #1	|
|	registry_key_new_name	|	NewName	|	string	|	new name of the registry key	|	\REGISTRY\MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\hello	|