---
title: Event ID 4103 - Module Logging
description: Detailed logging of all PowerShell command input and output.
log.type: Windows PowerShell
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 05/16/2018
---

# Event ID 4103: Module Logging 

## Description

Beginning in Windows PowerShell 3.0, you can record execution events for the cmdlets and functions in Windows PowerShell modules. This feature can provide detailed logging of all PowerShell command input and output, [Investigating PowerShell Attacks - Mandiant](https://www.defcon.org/images/defcon-22/dc-22-presentations/Kazanciyan-Hastings/DEFCON-22-Ryan-Kazanciyan-Matt-Hastings-Investigating-Powershell-Attacks.pdf)

Module logging records pipeline execution details as PowerShell executes, including variable initialization and command invocations. Module logging will record portions of scripts, some de-obfuscated code, and some data formatted for output. [FireEye](https://www.fireeye.com/blog/threat-research/2016/02/greater_visibilityt.html)

## Event Log Illustration

<img src="https://github.com/Cyb3rWard0g/OSSEM/blob/master/resources/images/event-4103.png" alt="Event 2 illustration" width="625" height="625">

## Event XML

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-PowerShell" Guid="{A0C1853B-5C40-4B15-8766-3CF1C58F985A}" /> 
    <EventID>4103</EventID> 
    <Version>1</Version> 
    <Level>4</Level> 
    <Task>106</Task> 
    <Opcode>20</Opcode> 
    <Keywords>0x0</Keywords> 
    <TimeCreated SystemTime="2018-05-16T21:08:50.767712300Z" /> 
    <EventRecordID>4272</EventRecordID> 
    <Correlation ActivityID="{240DF4D6-ED59-0000-3626-0E2459EDD301}" /> 
    <Execution ProcessID="6616" ThreadID="5112" /> 
    <Channel>Microsoft-windows-PowerShell/Operational</Channel> 
    <Computer>DESKTOP-WARDOG</Computer> 
    <Security UserID="S-1-5-21-3825400013-1856045589-1834093677-1001" /> 
  </System>
  <EventData>
    <Data Name="ContextInfo">Severity = Informational Host Name = ConsoleHost Host Version = 5.1.16299.431 Host ID = 312b26a7-53d3-45db-8b45-b79cae3afba9 Host Application = C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe Engine Version = 5.1.16299.431 Runspace ID = 0252cd51-52b5-4825-8029-a4f81a93cef6 Pipeline ID = 35 Command Name = Get-ChildItem Command Type = Cmdlet Script Name = Command Path = Sequence Number = 88 User = DESKTOP-WARDOG\wardog Connected User = Shell ID = Microsoft.PowerShell</Data> 
    <Data Name="UserData" /> 
    <Data Name="Payload">CommandInvocation(Get-ChildItem): "Get-ChildItem" ParameterBinding(Get-ChildItem): name="Filter"; value="*.yml" ParameterBinding(Get-ChildItem): name="Recurse"; value="True" ParameterBinding(Get-ChildItem): name="Path"; value="C:\Program Files\winlogbeat\" CommandInvocation(Select-String): "Select-String" ParameterBinding(Select-String): name="Pattern"; value="powershell" ParameterBinding(Select-String): name="InputObject"; value="fields.yml" ParameterBinding(Select-String): name="InputObject"; value="winlogbeat.reference.yml" ParameterBinding(Select-String): name="InputObject"; value="winlogbeat.yml" ParameterBinding(Select-String): name="InputObject"; value=".winlogbeat.yml"</Data> 
  </EventData>
</Event>
```

## Data Dictionary

| Standard Name | Field Name | Type | Description | Sample Value |
| ---------------- | ---------------- | ---------------- | ---------------- | ---------------- |
| powershell_command_invocation | CommandInvocation | string | | Get-ChildItem |
| powershell_parameter_binding | ParameterBinding | string | | Filter |
| powershell_severity | Severity | string | | Informational |
| powershell_host_name | HostName | string | | ConsoleHost |
| powershell_host_version | HostVersion | string | | 5.1.16299.431 |
| powershell_host_id | HostId | string | | 312b26a7-53d3-45db-8b45-b79cae3afba9 |
| powershell_host_application | HostApplication | string | | C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe |
| powershell_engine_version | EngineVersion | string | | 5.1.16299.431 |
| powershell_runspace_id | RunspaceId | string | | 0252cd51-52b5-4825-8029-a4f81a93cef6 |
| powershell_pipeline_id | PipelineId | integer | | 35 |
| powershell_command_name | CommandName | string | | Get-ChildItem |
| powershell_command_type | CommandType | string | | Cmdlet |
| powershell_script_name | ScriptName | string | | |
| powershell_command_path | CommandPath | string | | |
| powershell_sequence_number | Sequence Number | string | | 88 |
| user_name | User | string | | wardog |
| user_domain | User | string | | DESKTOP-WARDOG |
| powershell_connected_user | Connected User | string | | |
| powershell_shell_id | Shell ID | string | | Microsoft.PowerShell |
