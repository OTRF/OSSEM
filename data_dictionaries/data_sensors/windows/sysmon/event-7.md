---
title: Event ID 7 - Image loaded
description: The image loaded event logs when a module is loaded in a specific process.
log.type: sysmon
sysmon.version: 7.01
sysmon.rule: ImageLoad
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/11/2018
---

# Event ID 7: Image loaded

## Description
The image loaded event logs when a module is loaded in a specific process. This event is disabled by default and needs to be configured with the –l option. It indicates the process in which the module is loaded, hashes and signature information. The signature is created asynchronously for performance reasons and indicates if the file was removed after loading. This event should be configured carefully, as monitoring all image load events will generate a large number of events.[Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-7-image-loaded)

## Event Log Illustration

![alt text](/OSSEM/resources/images/event-7.png "Event 7 illustration")

## Event XML

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385F-C22A-43E0-BF4C-06F5698FFBD9}" /> 
    <EventID>7</EventID> 
    <Version>3</Version> 
    <Level>4</Level> 
    <Task>7</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2018-04-11T05:46:18.402515800Z" /> 
    <EventRecordID>11756509</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="6028" ThreadID="4132" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>DESKTOP-WARDOG</Computer> 
    <Security UserID="S-1-5-18" /> 
  </System>
  <EventData>
    <Data Name="UtcTime">2018-04-11 05:46:18.398</Data> 
    <Data Name="ProcessGuid">{A98268C1-A12A-5ACD-0000-0010E4C8B300}</Data> 
    <Data Name="ProcessId">3532</Data> 
    <Data Name="Image">C:\Windows\System32\cmd.exe</Data> 
    <Data Name="ImageLoaded">C:\Windows\System32\msvcrt.dll</Data> 
    <Data Name="FileVersion">7.0.16299.125 (WinBuild.160101.0800)</Data> 
    <Data Name="Description">Windows NT CRT DLL</Data> 
    <Data Name="Product">Microsoft® Windows® Operating System</Data> 
    <Data Name="Company">Microsoft Corporation</Data> 
    <Data Name="Hashes">SHA1=AEB9839D02C99A3E7EED1F12671C3F827221EDF8,MD5=68195105C7D9A2B5DF5BB82ECA521092,SHA256=556FF2B03495E2117223E5697B54253F30BD10ED3C67468947D79945168A624A,IMPHASH=C16CC99941EF5E18707133A2532B7D0C</Data> 
    <Data Name="Signed">true</Data> 
    <Data Name="Signature">Microsoft Windows</Data> 
    <Data Name="SignatureStatus">Valid</Data> 
  </EventData>
</Event>
```