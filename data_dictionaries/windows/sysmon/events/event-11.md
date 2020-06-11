---
title: Event ID 11 - FileCreate
description: File create operations are logged when a file is created or overwritten.
log.type: sysmon
sysmon.version: 9.01
sysmon.rule: FileCreate
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/26/2019
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
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385f-c22a-43e0-bf4c-06f5698ffbd9}" /> 
    <EventID>11</EventID> 
    <Version>2</Version> 
    <Level>4</Level> 
    <Task>11</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2019-04-27T00:11:22.786128800Z" /> 
    <EventRecordID>3611638</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="2332" ThreadID="3784" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>WARDOG.RIVENDELL.local</Computer> 
    <Security UserID="S-1-5-18" /> 
  </System>
  <EventData>
    <Data Name="RuleName" /> 
    <Data Name="UtcTime">2019-04-27 00:11:22.756</Data> 
    <Data Name="ProcessGuid">{1c9fdc81-9e27-5cc3-0000-0010116d0600}</Data> 
    <Data Name="ProcessId">3832</Data> 
    <Data Name="Image">C:\WINDOWS\system32\WerFault.exe</Data> 
    <Data Name="TargetFilename">C:\ProgramData\Microsoft\Windows\WER\ReportArchive\AppCrash_Sysmon.exe_16b56163a540d67bfc0dd95fd4d37fd83fe58dd_e290769b_0ef86f73\Report.wer</Data> 
    <Data Name="CreationUtcTime">2019-04-27 00:11:22.756</Data> 
  </EventData>
</Event>
```

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
| tag                | RuleName        | string  | custom tag mapped to event. i.e ATT&CK technique ID                             | T1114                                       |
| @timestamp         | UtcTime         | date    | Time in UTC when event was created                                              | 2020-04-01 09:01:01.576                     |
| process_guid       | ProcessGuid     | string  | Process Guid of the process that created the file                               | {A98268C1-958A-5ACD-0000-0010C62F0100}      |
| process_id         | ProcessId       | integer | Process ID used by the os to identify the process that created the file (child) | 1044                                        |
| process_name       | Image           | string  | File name of the process that created the file                                  | svchost.exe                                 |
| process_path       | Image           | string  | File path of the process that created the file                                  | C:\WINDOWS\System32\svchost.exe             |
| file_name          | TargetFilename  | string  | Name of the file                                                                | C:\Windows\Prefetch\CONHOST.EXE-1F3E9D7E.pf |
| file_creation_time | CreationUtcTime | date    | File creation time                                                              | 12/4/17 17:38                               |
