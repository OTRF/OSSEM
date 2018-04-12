---
title: Event ID 13 - RegistryEvent (Value Set)
description: This Registry event type identifies Registry value modifications.
log.type: sysmon
sysmon.version: 7.01
sysmon.rule: RegistryEvent
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/11/2018
---

# Event ID 13: RegistryEvent (Value Set)

## Description
This Registry event type identifies Registry value modifications. The event records the value written for Registry values of type DWORD and QWORD.[Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-13-registryevent-value-set)

## Event Log Illustration

<img src="https://github.com/Cyb3rWard0g/OSSEM/blob/master/resources/images/event-13.png" alt="Event 13 illustration" width="625" height="625">

## Event XML

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385F-C22A-43E0-BF4C-06F5698FFBD9}" /> 
    <EventID>13</EventID> 
    <Version>2</Version> 
    <Level>4</Level> 
    <Task>13</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2018-04-11T06:04:04.556170700Z" /> 
    <EventRecordID>11761526</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="6028" ThreadID="4132" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>DESKTOP-WARDOG</Computer> 
    <Security UserID="S-1-5-18" /> 
  </System>
  <EventData>
    <Data Name="EventType">SetValue</Data> 
    <Data Name="UtcTime">2018-04-11 06:04:04.552</Data> 
    <Data Name="ProcessGuid">{A98268C1-95F9-5ACD-0000-001025861000}</Data> 
    <Data Name="ProcessId">4624</Data> 
    <Data Name="Image">C:\WINDOWS\Explorer.EXE</Data> 
    <Data Name="TargetObject">HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Notifications\Data\418A073AA3BC3475</Data> 
    <Data Name="Details">Binary Data</Data> 
  </EventData>
</Event>
```

## Data Dictionary

| Field Name | Type | Description | Sample Value |
|--------|---------|-------|---------|
| EventType | string | registry event. Registry values modifications | SetValue |
| UtcTime | date | Time in UTC when event was created |	2018-04-11 06:04:04.552 |
| ProcessGuid | string | Process Guid of the process that modified a registry value | {A98268C1-95F9-5ACD-0000-001025861000} |
| ProcessId | integer | Process ID used by the os to identify the process that that modified a registry value | 4624 |
| Image | string | File path of the process that that modified a registry value | C:\WINDOWS\Explorer.EXE |
| TargetObject | string | complete path of the registry key | HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Notifications\Data\418A073AA3BC3475 |
| Details | string | Value added to the registry key | Binary Data |