---
title: Event ID 1 - Process creation
description: The process creation event provides extended information about a newly created process.
log.type: sysmon
sysmon.version: 10.0
sysmon.rule: ProcessCreate
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 06/11/2019
---

# Event ID 1: Process creation

## Description
The process creation event provides extended information about a newly created process. The full command line provides context on the process execution. The ProcessGUID field is a unique value for this process across a domain to make event correlation easier. The hash is a full hash of the file with the algorithms in the HashType field.[Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-1-process-creation)

## Event Log Illustration

<img src="https://github.com/Cyb3rWard0g/OSSEM/blob/master/resources/images/event-1.png" alt="Event 1 illustration" width="575" height="620">

## Event XML

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385F-C22A-43E0-BF4C-06F5698FFBD9}" /> 
    <EventID>1</EventID> 
    <Version>5</Version> 
    <Level>4</Level> 
    <Task>1</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2019-06-12T00:48:53.300422700Z" /> 
    <EventRecordID>6526518</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="2312" ThreadID="3800" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>DESKTOP-WARDOG.RIVENDELL.local</Computer> 
    <Security UserID="S-1-5-18" /> 
  </System>
  <EventData>
    <Data Name="RuleName" /> 
    <Data Name="UtcTime">2019-06-12 00:48:53.295</Data> 
    <Data Name="ProcessGuid">{A98268C1-4BF5-5D00-0000-00102A7B2B00}</Data> 
    <Data Name="ProcessId">6364</Data> 
    <Data Name="Image">C:\Windows\System32\wuauclt.exe</Data> 
    <Data Name="FileVersion">10.0.17134.1 (WinBuild.160101.0800)</Data> 
    <Data Name="Description">Windows Update</Data> 
    <Data Name="Product">Microsoft® Windows® Operating System</Data> 
    <Data Name="Company">Microsoft Corporation</Data> 
    <Data Name="OriginalFileName">wuauclt.exe</Data> 
    <Data Name="CommandLine">"C:\WINDOWS\system32\wuauclt.exe" /RunHandlerComServer</Data> 
    <Data Name="CurrentDirectory">C:\WINDOWS\system32\</Data> 
    <Data Name="User">NT AUTHORITY\SYSTEM</Data> 
    <Data Name="LogonGuid">{A98268C1-48F4-5D00-0000-0020E7030000}</Data> 
    <Data Name="LogonId">0x3e7</Data> 
    <Data Name="TerminalSessionId">0</Data> 
    <Data Name="IntegrityLevel">System</Data> 
    <Data Name="Hashes">SHA1=E82AC9345FBEFC100FF16D66536877502AB2C017,MD5=C8F7FA1A3A3B23DF12A2BCF4B500DEE1,SHA256=E666AC2934A9BA6C65531E4E258C9BEBD7C311C6A378A6ACCEFFDF7F9741B4A8,IMPHASH=E799C2BD8BC66603D6DDC95F2DB31A18</Data> 
    <Data Name="ParentProcessGuid">{A98268C1-48F5-5D00-0000-00103C410100}</Data> 
    <Data Name="ParentProcessId">1040</Data> 
    <Data Name="ParentImage">C:\Windows\System32\svchost.exe</Data> 
    <Data Name="ParentCommandLine">C:\WINDOWS\system32\svchost.exe -k netsvcs -p</Data> 
  </EventData>
</Event>
```

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
| @timestamp                  | UtcTime           | date    | Time in UTC when event was created                                                                                                                            | `2020-04-01 09:01:01.576`                                                                                                                                                                                           |
| file_company                | Company           | string  | Company name the image associated with the main process (child) belongs to                                                                                    | `Microsoft Corporation`                                                                                                                                                                                  |
| file_description            | Description       | string  | Description of the image associated with the main process (child)                                                                                             | `Console Window Host`                                                                                                                                                                                    |
| file_product                | Product           | string  | Product name the image associated with the main process (child) belongs to                                                                                    | `Microsoft® Windows® Operating System`                                                                                                                                                                   |
| file_version                | FileVersion       | string  | Version of the image associated with the main process (child)                                                                                                 | `10.0.16299.15 (WinBuild.160101.0800)`                                                                                                                                                                   |
| hash                        | Hashes            | string  | Hashes captured by sysmon driver                                                                                                                              | `SHA1=B0BF5AC2E81BBF597FAD5F349FEEB32CAC449FA2, MD5=6A255BEBF3DBCD13585538ED47DBAFD7, SHA256=4668BB2223FFB983A5F1273B9E3D9FA2C5CE4A0F1FB18CA5C1B285762020073C, IMPHASH=2505BD03D7BD285E50CE89CEC02B333B` |
| process_command_line        | CommandLine       | string  | Arguments which were passed to the executable associated with the main process                                                                                | `??\C:\WINDOWS\system32\conhost.exe 0xffffffff -ForceV1`                                                                                                                                                 |
| process_current_directory   | CurrentDirectory  | string  | The path without the name of the image associated with the process                                                                                            | `C:\WINDOWS`                                                                                                                                                                                             |
| process_guid                | ProcessGuid       | string  | Process Guid of the process that got spawned/created (child)                                                                                                  | `{A98268C1-9C2E-5ACD-0000-0010396CAB00}`                                                                                                                                                                 |
| process_id                  | ProcessId         | integer | Process ID used by the os to identify the created process (child)                                                                                             | `4756`                                                                                                                                                                                                   |
| process_integrity_level     | IntegrityLevel    | string  | Integrity label assigned to a process                                                                                                                         | `Medium`                                                                                                                                                                                                 |
| process_name                | Image             | string  | The name of the executable without full path related to the process being spawned/created in the event. Considered also the child or source process           | `1`                                                                                                                                                                                                      |
| process_parent_command_line | ParentCommandLine | string  | Arguments which were passed to the executable associated with the parent process                                                                              | `C:\WINDOWS\system32\cmd.exe`                                                                                                                                                                            |
| process_parent_guid         | ParentProcessGuid | string  | ProcessGUID of the process that spawned/created the main process (child)                                                                                      | `{A98268C1-9C2E-5ACD-0000-00100266AB00}`                                                                                                                                                                 |
| process_parent_id           | ParentProcessId   | integer | Process ID of the process that spawned/created the main process (child)                                                                                       | `240`                                                                                                                                                                                                    |
| process_parent_name         | ParentImage       | string  | The name of the executable related to the target process                                                                                                      | `cmd.exe`                                                                                                                                                                                                |
| process_parent_path         | ParentImage       | string  | File path that spawned/created the main process                                                                                                               | `C:\Windows\System32\cmd.exe`                                                                                                                                                                            |
| process_path                | Image             | string  | File path of the process being spawned/created. Considered also the child or source process                                                                   | `1`                                                                                                                                                                                                      |
| user_logon_guid             | LogonGuid         | string  | Logon GUID of the user who created the new process. Value that can help you correlate this event with others that contain the same Logon GUID (Sysmon Events) | `{A98268C1-95F2-5ACD-0000-002019620F00}`                                                                                                                                                                 |
| user_logon_id               | LogonId           | integer | Login ID of the user who created the new process. Value that can help you correlate this event with others that contain the same Logon ID                     | `0xf6219`                                                                                                                                                                                                |
| user_name                   | User              | string  | Name of the account who created the process (child) . It usually contains domain name and user name (Parsed to show only username without the domain)         | `DESKTOP-WARDOG\wardog`                                                                                                                                                                                  |
| user_session_id             | TerminalSessionId | integer | ID of the session the user belongs to                                                                                                                         | `1`                                                                                                                                                                                                      |
| file_name_original          | OriginalFileName  | string  | original file name                                                                                                                                            | `wuauclt.exe`                                                                                                                                                                                            |
| tag                         | RuleName          | string  | custom tag mapped to event. i.e ATT&CK technique ID                                                                                                           | `T1114`                                                                                                                                                                                                  |
