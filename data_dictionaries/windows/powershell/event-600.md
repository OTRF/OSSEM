---
title: Event ID 600 - Provider Lifecycle
description: Logs the start and stop of PowerShell providers.
log.type: Windows PowerShell
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 05/16/2018
---

# Event ID 600: Provider Lifecycle 

## Description

Logs the start and stop of PowerShell providers. If the provider started is equal to **WSMan**, then it indicates the use rof PowerShell remoting [Investigating PowerShell Attacks - Mandiant](https://www.defcon.org/images/defcon-22/dc-22-presentations/Kazanciyan-Hastings/DEFCON-22-Ryan-Kazanciyan-Matt-Hastings-Investigating-Powershell-Attacks.pdf)

## Event Log Illustration

<img src="https://github.com/Cyb3rWard0g/OSSEM/blob/master/resources/images/event-600.png" alt="Event 2 illustration" width="625" height="625">

## Event XML

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="PowerShell" /> 
    <EventID Qualifiers="0">600</EventID> 
    <Level>4</Level> 
    <Task>6</Task> 
    <Keywords>0x80000000000000</Keywords> 
    <TimeCreated SystemTime="2018-05-07T05:46:02.808934700Z" /> 
    <EventRecordID>8047</EventRecordID> 
    <Channel>Windows PowerShell</Channel> 
    <Computer>DESKTOP-WARDOG</Computer> 
    <Security /> 
  </System>
  <EventData>
    <Data>Variable</Data> 
    <Data>Started</Data> 
    <Data>ProviderName=Variable NewProviderState=Started SequenceNumber=11 HostName=ConsoleHost HostVersion=5.1.16299.251 HostId=7839f0de-2e81-4a34-beb3-526dc9f11385 HostApplication=C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe EngineVersion= RunspaceId= PipelineId= CommandName= CommandType= ScriptName= CommandPath= CommandLine=</Data> 
  </EventData>
</Event>
```

## Data Dictionary

| Standard Name | Field Name | Type | Description | Sample Value |
| ---------------- | ---------------- | ---------------- | ---------------- | ---------------- |
| event_provider_name | ProviderName | string | | Variable |
| powershell_new_provider_state | NewProviderState | string | | Started |
| powershell_sequence_number | SequenceNumber | integer | | 11 |
| powershell_host_name | HostName | string | | ConsoleHost |
| powershell_host_version | HostVersion | string | | 5.1.16299.251 |
| powershell_host_id | HostId | string | | 7839f0de-2e81-4a34-beb3-526dc9f11385 |
| powershell_host_application | HostApplication | string | | C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe |
| powershell_engine_version | EngineVersion | string | |  |
| powershell_runspace_id | RunspaceId | string | | |
| powershell_pipeline_id | PipelineId | string | | |
| powershell_command_name | CommandName | string | | |
| powershell_command_type | CommandType | string | | |
| powershell_script_name | ScriptName | string | | |
| powershell_command_path | CommandPath | string | | |
| powershell_command_line | CommandLine | string | | |
