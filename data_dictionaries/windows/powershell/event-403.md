---
title: Event ID 403 - Engine Lifecycle
description: Information about PowerShell engine state. Engine state is changed from Available to Stopped
log.type: Windows PowerShell
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 05/16/2018
---

# Event ID 403: Engine Lifecycle

## Description

Logs the start and stop of PowerShell. Each time that PowerShell executes – either upon the execution of a single command, the start of a local session, or the start of a remoting session – this log records an Event ID (EID) 400 message: “Engine state is changed from None to Available.” At the completion of the session, the log records an EID 403 event: “Engine state is changed from Available to Stopped”.
The message details for both EID 400 and EID 403 events include a HostName field. If executed locally, this field will be logged as HostName=ConsoleHost. If PowerShell remoting is in use, the accessed system will record these events with HostName=ServerRemoteHost.”[Investigating PowerShell Attacks - Mandiant](https://www.blackhat.com/docs/us-14/materials/us-14-Kazanciyan-Investigating-Powershell-Attacks-WP.pdf)

## Event Log Illustration

<img src="https://github.com/Cyb3rWard0g/OSSEM/blob/master/resources/images/event-403.png" alt="Event 2 illustration" width="625" height="625">

## Event XML

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="PowerShell" /> 
    <EventID Qualifiers="0">403</EventID> 
    <Level>4</Level> 
    <Task>4</Task> 
    <Keywords>0x80000000000000</Keywords> 
    <TimeCreated SystemTime="2017-12-04T20:15:14.047446300Z" /> 
    <EventRecordID>15</EventRecordID> 
    <Channel>Windows PowerShell</Channel> 
    <Computer>DESKTOP-29DJI4T</Computer> 
    <Security /> 
  </System>
  <EventData>
    <Data>Stopped</Data> 
    <Data>Available</Data> 
    <Data>NewEngineState=Stopped PreviousEngineState=Available SequenceNumber=15 HostName=Windows PowerShell ISE Host HostVersion=5.1.16299.64 HostId=26572281-9dcd-4297-ae4b-d6bb52bdaff6 HostApplication=C:\WINDOWS\system32\WindowsPowerShell\v1.0\PowerShell_ISE.exe EngineVersion=5.1.16299.64 RunspaceId=aba09534-39f7-4ec3-aa46-8c709c39cf5a PipelineId= CommandName= CommandType= ScriptName= CommandPath= CommandLine=</Data> 
  </EventData>
</Event>
```

## Data Dictionary

| Standard Name | Field Name | Type | Description | Sample Value |
| ---------------- | ---------------- | ---------------- | ---------------- | ---------------- |
| powershell_new_engine_state | NewEngineState | string | | Stopped |
| powershell_previous_engine_state | PreviousEngineState | string | | Available |
| powershell_sequence_number | SequenceNumber | integer | | 13 |
| powershell_host_name | HostName | string | | Windows PowerShell ISE |
| powershell_host_version | HostVersion | string | | 5.1.16299.64 |
| powershell_host_id | HostId | string | | 26572281-9dcd-4297-ae4b-d6bb52bdaff6 |
| powershell_host_application | HostApplication | string | | C:\WINDOWS\system32\WindowsPowerShell\v1.0\PowerShell_ISE.exe |
| powershell_engine_version | EngineVersion | string | | 5.1.16299.64 |
| powershell_runspace_id | RunspaceId | string | | aba09534-39f7-4ec3-aa46-8c709c39cf5a |
| powershell_pipeline_id | PipelineId | string | | |
| powershell_command_name | CommandName | string | | |
| powershell_command_type | CommandType | string | | |
| powershell_script_name | ScriptName | string | | |
| powershell_command_path | CommandPath | string | | |
| powershell_command_line | CommandLine | string | | |
