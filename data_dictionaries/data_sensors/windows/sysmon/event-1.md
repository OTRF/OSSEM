---
title: Event ID 1 - Process creation
description: The process creation event provides extended information about a newly created process.
log.type: sysmon
sysmon.version: 7.01
sysmon.rule: ProcessCreate
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/11/2018
---

# Event ID 1: Process creation

## Description
The process creation event provides extended information about a newly created process. The full command line provides context on the process execution. The ProcessGUID field is a unique value for this process across a domain to make event correlation easier. The hash is a full hash of the file with the algorithms in the HashType field.[Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-1-process-creation)

## Event Log Illustration

![alt text](/OSSEM/resources/images/event-1.png "Event 1 illustration")

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
    <TimeCreated SystemTime="2018-04-11T05:25:02.959125700Z" /> 
    <EventRecordID>11748095</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="2152" ThreadID="3392" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>DESKTOP-WARDOG</Computer> 
    <Security UserID="S-1-5-18" /> 
  </System>
  <EventData>
    <Data Name="UtcTime">2018-04-11 05:25:02.955</Data> 
    <Data Name="ProcessGuid">{A98268C1-9C2E-5ACD-0000-0010396CAB00}</Data> 
    <Data Name="ProcessId">4756</Data> 
    <Data Name="Image">C:\Windows\System32\conhost.exe</Data> 
    <Data Name="FileVersion">10.0.16299.15 (WinBuild.160101.0800)</Data> 
    <Data Name="Description">Console Window Host</Data> 
    <Data Name="Product">Microsoft® Windows® Operating System</Data> 
    <Data Name="Company">Microsoft Corporation</Data> 
    <Data Name="CommandLine">\??\C:\WINDOWS\system32\conhost.exe 0xffffffff -ForceV1</Data> 
    <Data Name="CurrentDirectory">C:\WINDOWS</Data> 
    <Data Name="User">DESKTOP-WARDOG\wardog</Data> 
    <Data Name="LogonGuid">{A98268C1-95F2-5ACD-0000-002019620F00}</Data> 
    <Data Name="LogonId">0xf6219</Data> 
    <Data Name="TerminalSessionId">1</Data> 
    <Data Name="IntegrityLevel">Medium</Data> 
    <Data Name="Hashes">SHA1=B0BF5AC2E81BBF597FAD5F349FEEB32CAC449FA2,MD5=6A255BEBF3DBCD13585538ED47DBAFD7,SHA256=4668BB2223FFB983A5F1273B9E3D9FA2C5CE4A0F1FB18CA5C1B285762020073C,IMPHASH=2505BD03D7BD285E50CE89CEC02B333B</Data> 
    <Data Name="ParentProcessGuid">{A98268C1-9C2E-5ACD-0000-00100266AB00}</Data> 
    <Data Name="ParentProcessId">240</Data> 
    <Data Name="ParentImage">C:\Windows\System32\cmd.exe</Data> 
    <Data Name="ParentCommandLine">"C:\WINDOWS\system32\cmd.exe"</Data> 
  </EventData>
</Event>
```