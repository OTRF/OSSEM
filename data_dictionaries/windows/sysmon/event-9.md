---
title: Event ID 9 - RawAccessRead
description: The RawAccessRead event detects when a process conducts reading operations from the drive using the \\.\ denotation.
log.type: sysmon
sysmon.version: 9.01
sysmon.rule: RawAccessRead
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/26/2019
---

# Event ID 9: RawAccessRead

## Description
The RawAccessRead event detects when a process conducts reading operations from the drive using the \\.\ denotation. This technique is often used by malware for data exfiltration of files that are locked for reading, as well as to avoid file access auditing tools. The event indicates the source process and target device.[Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-9-rawaccessread)

## Event Log Illustration

<img src="https://github.com/Cyb3rWard0g/OSSEM/blob/master/resources/images/event-9.png" alt="Event 9 illustration" width="625" height="625">

## Event XML

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385f-c22a-43e0-bf4c-06f5698ffbd9}" /> 
    <EventID>9</EventID> 
    <Version>2</Version> 
    <Level>4</Level> 
    <Task>9</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2019-04-27T00:11:20.686207100Z" /> 
    <EventRecordID>3610045</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="2332" ThreadID="3784" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>WARDOG.RIVENDELL.local</Computer> 
    <Security UserID="S-1-5-18" /> 
  </System>
  <EventData>
    <Data Name="RuleName" /> 
    <Data Name="UtcTime">2019-04-27 00:11:19.430</Data> 
    <Data Name="ProcessGuid">{1c9fdc81-9e20-5cc3-0000-0010a3d60300}</Data> 
    <Data Name="ProcessId">2864</Data> 
    <Data Name="Image">C:\Windows\System32\wbem\WmiPrvSE.exe</Data> 
    <Data Name="Device">\Device\Harddisk0\DR0</Data> 
  </EventData>
</Event>
```

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	event_creation_time	|	UtcTime	|	date	|	Time in UTC when event was created	|	4/11/18 5:51	|
|	process_guid	|	ProcessGuid	|	string	|	Process Guid of the process that conducted reading operations from the drive	|	{A98268C1-959B-5ACD-0000-0010EFD50200}	|
|	process_id	|	ProcessId	|	integer	|	Process ID used by the os to identify the process that conducted reading operations from the drive	|	2708	|
|	process_name	|	Image	|	string	|	File name of the process that conducted reading operations from the drive	|	svchost.exe	|
|	process_path	|	Image	|	string	|	File path of the process that conducted reading operations from the drive	|	C:\Windows\System32\svchost.exe	|
|	target_device	|	Device	|	string	|	Target device	|	\Device\HarddiskVolume2	|