---
title: Event ID 6 - Driver loaded
description: The driver loaded events provides information about a driver being loaded on the system.
log.type: sysmon
sysmon.version: 7.01
sysmon.rule: DriverLoad
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/11/2018
---

# Event ID 6: Driver loaded

## Description
The driver loaded events provides information about a driver being loaded on the system. The configured hashes are provided as well as signature information. The signature is created asynchronously for performance reasons and indicates if the file was removed after loading.[Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-6-driver-loaded)

## Event Log Illustration

<img src="https://github.com/Cyb3rWard0g/OSSEM/blob/master/resources/images/event-6.png" alt="Event 6 illustration" width="625" height="625">

## Event XML:

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385F-C22A-43E0-BF4C-06F5698FFBD9}" /> 
    <EventID>6</EventID> 
    <Version>3</Version> 
    <Level>4</Level> 
    <Task>6</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2018-04-11T05:21:34.704903800Z" /> 
    <EventRecordID>11744642</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="2152" ThreadID="3408" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>DESKTOP-WARDOG</Computer> 
    <Security UserID="S-1-5-18" /> 
  </System>
  <EventData>
    <Data Name="UtcTime">2018-04-11 05:21:34.650</Data> 
    <Data Name="ImageLoaded">C:\ProgramData\Microsoft\Windows Defender\Definition Updates\{741285CC-BF49-492C-90BE-E84BD6CADD73}\MpKsl4d223a5a.sys</Data> 
    <Data Name="Hashes">SHA1=38310AD6805DC31D5AA61BE182689D63060ACE94,MD5=BF2513029E231BE96D82F7C3ABFF87F4,SHA256=F6DB64112CC50EEE495E2D7C61B8BDBE757A31B03144B0396615FD38C312824E,IMPHASH=06D4A412CF7F5363C49E629BF34446B3</Data> 
    <Data Name="Signed">true</Data> 
    <Data Name="Signature">Microsoft Corporation</Data> 
    <Data Name="SignatureStatus">Valid</Data> 
  </EventData>
</Event>
```