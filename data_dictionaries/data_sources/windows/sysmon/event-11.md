---
title: Event ID 11 - FileCreate
description: File create operations are logged when a file is created or overwritten.
log.type: sysmon
sysmon.version: 7.01
sysmon.rule: FileCreate
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/11/2018
---

# Event ID 11: FileCreate

## Description
File create operations are logged when a file is created or overwritten. This event is useful for monitoring autostart locations, like the Startup folder, as well as temporary and download directories, which are common places malware drops during initial infection.[Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-11-filecreate)

## Event Log Illustration

<img src="https://github.com/Cyb3rWard0g/OSSEM/blob/master/resources/images/event-11.png" alt="Event 11 illustration" width="625" height="625">

## Event XML

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385F-C22A-43E0-BF4C-06F5698FFBD9}" /> 
    <EventID>11</EventID> 
    <Version>2</Version> 
    <Level>4</Level> 
    <Task>11</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2018-04-11T06:01:23.107069400Z" /> 
    <EventRecordID>11760994</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="6028" ThreadID="4132" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>DESKTOP-WARDOG</Computer> 
    <Security UserID="S-1-5-18" /> 
  </System>
  <EventData>
    <Data Name="UtcTime">2018-04-11 06:01:23.106</Data> 
    <Data Name="ProcessGuid">{A98268C1-958A-5ACD-0000-0010C62F0100}</Data> 
    <Data Name="ProcessId">1044</Data> 
    <Data Name="Image">C:\WINDOWS\System32\svchost.exe</Data> 
    <Data Name="TargetFilename">C:\Windows\Prefetch\CONHOST.EXE-1F3E9D7E.pf</Data> 
    <Data Name="CreationUtcTime">2017-12-04 17:38:32.040</Data> 
  </EventData>
</Event>
```

## Data Dictionary

| Field Name | Type | Description | Sample Value |
|--------|---------|-------|---------|
| UtcTime | date | Time in UTC when event was created |	2018-04-11 06:01:23.106 |
| ProcessGuid | string | Process Guid of the process that created the file | {A98268C1-958A-5ACD-0000-0010C62F0100} |
| ProcessId | integer | Process ID used by the os to identify the process that created the file (child) | 1044 |
| Image | string | File path of the process that created the file | C:\WINDOWS\System32\svchost.exe |
| TargetFilename | string | Name of the file | C:\Windows\Prefetch\CONHOST.EXE-1F3E9D7E.pf |
| CreationUtcTime | date | File creation time | 2017-12-04 17:38:32.040 |