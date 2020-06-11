---
title: Event ID 255 - Error Report
description:
log.type: sysmon
sysmon.version: 9.01
sysmon.rule: WmiEvent
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/26/2019
---
# Event ID 255: Error Report

## Description


## Event Log Illustration

<img src="https://github.com/Cyb3rWard0g/OSSEM/blob/master/resources/images/event-255.png" alt="Event 255 illustration" width="625" height="625">

## Event XML

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385f-c22a-43e0-bf4c-06f5698ffbd9}" />
    <EventID>255</EventID>
    <Version>3</Version>
    <Level>2</Level>
    <Task>255</Task>
    <Opcode>0</Opcode>
    <Keywords>0x8000000000000000</Keywords>
    <TimeCreated SystemTime="2019-04-27T00:10:34.262645100Z" />
    <EventRecordID>3606985</EventRecordID>
    <Correlation />
    <Execution ProcessID="2336" ThreadID="3124" />
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel>
    <Computer>WARDOG.RIVENDELL.local</Computer>
    <Security UserID="S-1-5-18" />
  </System>
  <EventData>
    <Data Name="UtcTime">2019-04-27 00:10:34.254</Data>
    <Data Name="ID">GetConfigurationOptions</Data>
    <Data Name="Description">Failed to open service configuration with error 19</Data>
  </EventData>
</Event>
```