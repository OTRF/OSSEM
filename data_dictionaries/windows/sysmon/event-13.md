---
title: Event ID 13 - RegistryEvent (Value Set)
description: This Registry event type identifies Registry value modifications.
log.type: sysmon
sysmon.version: 9.01
sysmon.rule: RegistryEvent
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/26/2019
---

# Event ID 13: RegistryEvent (Value Set)

## Description
This Registry event type identifies Registry value modifications. The event records the value written for Registry values of type DWORD and QWORD.[Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-13-registryevent-value-set)

## Event Log Illustration

<img src="https://github.com/Cyb3rWard0g/OSSEM/blob/master/resources/images/event-13.png" alt="Event 13 illustration" width="625" height="625">

## Event XML

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385f-c22a-43e0-bf4c-06f5698ffbd9}" /> 
    <EventID>13</EventID> 
    <Version>2</Version> 
    <Level>4</Level> 
    <Task>13</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2019-04-27T00:11:20.698542300Z" /> 
    <EventRecordID>3610086</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="2332" ThreadID="3784" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>WARDOG.RIVENDELL.local</Computer> 
    <Security UserID="S-1-5-18" /> 
  </System>
  <EventData>
    <Data Name="RuleName" /> 
    <Data Name="EventType">SetValue</Data> 
    <Data Name="UtcTime">2019-04-27 00:11:20.292</Data> 
    <Data Name="ProcessGuid">{1c9fdc81-9e27-5cc3-0000-0010116d0600}</Data> 
    <Data Name="ProcessId">3832</Data> 
    <Data Name="Image">C:\WINDOWS\system32\WerFault.exe</Data> 
    <Data Name="TargetObject">\REGISTRY\A\{417d6f3b-d84a-b9e2-2491-4db6453a55c9}\Root\InventoryApplicationFile\WritePermissionsCheck</Data> 
    <Data Name="Details">DWORD (0x00000001)</Data> 
  </EventData>
</Event>
```

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	event_type	|	EventType	|	string	|	registry event. Registry values modifications	|	SetValue	|
|	event_date_creation	|	UtcTime	|	date	|	Time in UTC when event was created	|	4/11/18 6:04	|
|	process_guid	|	ProcessGuid	|	string	|	Process Guid of the process that modified a registry value	|	{A98268C1-95F9-5ACD-0000-001025861000}	|
|	process_id	|	ProcessId	|	integer	|	Process ID used by the os to identify the process that that modified a registry value	|	4624	|
|	process_name	|	Image	|	string	|	File path of the process that that modified a registry value	|	C:\WINDOWS\Explorer.EXE	|
|	registry_key_path	|	TargetObject	|	string	|	complete path of the registry key	|	HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Notifications\Data\418A073AA3BC3475	|
|	registry_key_details	|	Details	|	string	|	Details added to the registry key	|	Binary Data	|