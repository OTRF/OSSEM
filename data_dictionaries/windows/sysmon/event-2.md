---
title: Event ID 2 - A process changed a file creation time
description: The change file creation time event is registered when a file creation time is explicitly modified by a process.
log.type: sysmon
sysmon.version: 9.01
sysmon.rule: FileCreateTime
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/26/2019
---

# Event ID 2: A process changed a file creation time

## Description
The change file creation time event is registered when a file creation time is explicitly modified by a process. This event helps tracking the real creation time of a file. Attackers may change the file creation time of a backdoor to make it look like it was installed with the operating system. Note that many processes legitimately change the creation time of a file; it does not necessarily indicate malicious activity.[Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-2-a-process-changed-a-file-creation-time)

## Event Log Illustration

<img src="https://github.com/Cyb3rWard0g/OSSEM/blob/master/resources/images/event-2.png" alt="Event 2 illustration" width="625" height="625">

## Event XML:

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385f-c22a-43e0-bf4c-06f5698ffbd9}" /> 
    <EventID>2</EventID> 
    <Version>4</Version> 
    <Level>4</Level> 
    <Task>2</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2019-04-27T00:10:30.035445300Z" /> 
    <EventRecordID>3605382</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="2336" ThreadID="3652" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>DESKTOP-LFD11QP.RIVENDELL.local</Computer> 
    <Security UserID="S-1-5-18" /> 
  </System>
  <EventData>
    <Data Name="RuleName" /> 
    <Data Name="UtcTime">2019-04-27 00:10:30.008</Data> 
    <Data Name="ProcessGuid">{1c9fdc81-9dc6-5cc3-0000-0010604f1300}</Data> 
    <Data Name="ProcessId">6944</Data> 
    <Data Name="Image">C:\Users\cbrown\AppData\Local\Microsoft\OneDrive\OneDrive.exe</Data> 
    <Data Name="TargetFilename">C:\Users\cbrown\AppData\Local\Microsoft\OneDrive\settings\Personal\global.temp.ini</Data> 
    <Data Name="CreationUtcTime">2018-10-21 00:54:18.030</Data> 
    <Data Name="PreviousCreationUtcTime">2018-10-21 00:54:18.030</Data> 
  </EventData>
</Event>
```

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
| @timestamp                  | UtcTime                 | date    | Time in UTC when event was created                                                | 2020-04-01 09:01:01.576                                                                               |
| process_guid                | ProcessGuid             | string  | Process Guid of the process that changed the file creation time                   | {A98268C1-975A-5ACD-0000-0010DB073A00}                                                                |
| process_id                  | ProcessId               | integer | Process ID used by the os to identify the process changing the file creation time | 1252                                                                                                  |
| process_name                | Image                   | string  | File name of the process that changed the file creation time                      | powershell.exe                                                                                        |
| process_path                | Image                   | string  | File path of the process that changed the file creation time                      | C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe                                             |
| file_name                   | TargetFilename          | string  | full path name of the file                                                        | C:\Users\wardog\AppData\Roaming\Microsoft\Windows\Recent\CustomDestinations\7G23PHTPHSQ3S2RVKKPS.temp |
| file_creation_time          | CreationUtcTime         | date    | new creation time of the file                                                     | 11/13/17 16:57                                                                                        |
| file_previous_creation_time | PreviousCreationUtcTime | date    | previous creation time of the file                                                | 4/11/18 5:04                                                                                          |
