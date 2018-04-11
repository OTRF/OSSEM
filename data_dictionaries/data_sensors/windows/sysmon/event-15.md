---
title: Event ID 15 - FileCreateStreamHash
description: This event logs when a named file stream is created.
log.type: sysmon
sysmon.version: 7.01
sysmon.rule: FileCreateStreamHash
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/11/2018
---

# Event ID 14: RegistryEvent (Key and Value Rename)

## Description
This event logs when a named file stream is created, and it generates events that log the hash of the contents of the file to which the stream is assigned (the unnamed stream), as well as the contents of the named stream. There are malware variants that drop their executables or configuration settings via browser downloads, and this event is aimed at capturing that based on the browser attaching a Zone.Identifier “mark of the web” stream.[Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-15-filecreatestreamhash)

## Event Log Illustration

![alt text](/resources/images/event-15.png "Event 15 illustration")

## Event XML

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385F-C22A-43E0-BF4C-06F5698FFBD9}" /> 
    <EventID>15</EventID> 
    <Version>2</Version> 
    <Level>4</Level> 
    <Task>15</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2018-04-11T06:18:33.145878300Z" /> 
    <EventRecordID>11768076</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="6028" ThreadID="4132" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>DESKTOP-WARDOG</Computer> 
    <Security UserID="S-1-5-18" /> 
  </System>
  <EventData>
    <Data Name="UtcTime">2018-04-11 06:18:33.143</Data> 
    <Data Name="ProcessGuid">{A98268C1-A8A0-5ACD-0000-001087DEBF00}</Data> 
    <Data Name="ProcessId">6972</Data> 
    <Data Name="Image">C:\Program Files (x86)\Google\Chrome\Application\chrome.exe</Data> 
    <Data Name="TargetFilename">C:\Users\wardog\Downloads\a0fa35bc5badf505f803921f0fe40971-4cf6bad280c7b66e21bb8e96ffe2f968ca460e0d.zip:Zone.Identifier</Data> 
    <Data Name="CreationUtcTime">2018-04-11 06:18:30.960</Data> 
    <Data Name="Hash">SHA1=F897DA14CF93C872CE821F549C34B848E345C8AC,MD5=697C69E7BB023075F14BC0BE25B875D8,SHA256=3157F3E7A854A13A40FFC79472C319E5B7C744B50D869D6E45F40CD4218539C5,IMPHASH=00000000000000000000000000000000</Data> 
  </EventData>
</Event>
```