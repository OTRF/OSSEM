---
title: Event ID 2 - A process changed a file creation time
description: The change file creation time event is registered when a file creation time is explicitly modified by a process.
log.type: sysmon
sysmon.version: 7.01
sysmon.rule: FileCreateTime
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/11/2018
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
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385F-C22A-43E0-BF4C-06F5698FFBD9}" /> 
    <EventID>2</EventID> 
    <Version>4</Version> 
    <Level>4</Level> 
    <Task>2</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2018-04-11T05:04:27.222624200Z" /> 
    <EventRecordID>11469394</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="2152" ThreadID="3392" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>DESKTOP-WARDOG</Computer> 
    <Security UserID="S-1-5-18" /> 
    </System>
  <EventData>
    <Data Name="UtcTime">2018-04-11 05:04:27.211</Data> 
    <Data Name="ProcessGuid">{A98268C1-975A-5ACD-0000-0010DB073A00}</Data> 
    <Data Name="ProcessId">1252</Data> 
    <Data Name="Image">C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe</Data> 
    <Data Name="TargetFilename">C:\Users\wardog\AppData\Roaming\Microsoft\Windows\Recent\CustomDestinations\
    7G23PHTPHSQ3S2RVKKPS.temp</Data> 
    <Data Name="CreationUtcTime">2017-11-13 16:57:51.663</Data> 
    <Data Name="PreviousCreationUtcTime">2018-04-11 05:04:27.179</Data> 
  </EventData>
</Event>
```