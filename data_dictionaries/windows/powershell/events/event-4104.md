---
title: Event ID 4104 - Script Block Logging
description: It records blocks of code as they are executed by the PowerShell engine.
log.type: Windows PowerShell
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 05/16/2018
---

# Event ID 4104: Script Block Logging 

## Description

Script block logging records blocks of code as they are executed by the PowerShell engine, thereby capturing the full contents of code executed by an attacker, including scripts and commands. Due to the nature of script block logging, it also records de-obfuscated code as it is executed. For example, in addition to recording the original obfuscated code, script block logging records the decoded commands passed with PowerShell’s -EncodedCommand argument, as well as those obfuscated with XOR, Base64, ROT13, encryption, etc., in addition to the original obfuscated code. Script block logging will not record output from the executed code. [FireEye](https://www.fireeye.com/blog/threat-research/2016/02/greater_visibilityt.html)

## Event Log Illustration

<img src="https://github.com/Cyb3rWard0g/OSSEM/blob/master/resources/images/event-4104.png" alt="Event 2 illustration" width="625" height="625">

## Event XML

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-PowerShell" Guid="{A0C1853B-5C40-4B15-8766-3CF1C58F985A}" /> 
    <EventID>4104</EventID> 
    <Version>1</Version> 
    <Level>3</Level> 
    <Task>2</Task> 
    <Opcode>15</Opcode> 
    <Keywords>0x0</Keywords> 
    <TimeCreated SystemTime="2018-04-27T14:58:52.933359400Z" /> 
    <EventRecordID>4169</EventRecordID> 
    <Correlation ActivityID="{35AA0A3A-DCCA-0000-21BF-AA35CADCD301}" /> 
    <Execution ProcessID="6612" ThreadID="3444" /> 
    <Channel>Microsoft-windows-PowerShell/Operational</Channel> 
    <Computer>DESKTOP-WARDOG</Computer> 
    <Security UserID="S-1-5-21-3825400013-1856045589-1834093677-1001" /> 
  </System>
  <EventData>
    <Data Name="MessageNumber">1</Data> 
    <Data Name="MessageTotal">7</Data> 
    <Data Name="ScriptBlockText">function Invoke-ATTACKAPI { <# .SYNOPSIS A PS script to interact with the MITRE ATT&CK Framework via its own API .DESCRIPTION Use this script to interact with the MITRE ATT&CK Framework via its API and gather information about techniques, tactics, groups, software and references provided by the MITRE ATT&CK Team @MITREattack Almost all data in ATT&CK can be accessed using the Semantic MediaWiki Ask API. URLs targeting the API are constructed in the following pattern /api.php?action=ask&format=<format specifier>&query=<insert query statement> where <format specifier> is a specific output format (usually json or jsonfm) and <insert query statement> refers to a query that specifies the data that will be retrieved. Queries are structured as if they are targeting the Semantic MediaWiki #ask parser function. Queries are constructed by combining one or more page selectors with a set of display parameters. A simple selector for all techniques is [[Category:Technique]] and a simple display parameter is ?Has display name which maps to the name of the ATT&CK Technique. To construct the query, the selector is combined with the display parameter by placing a | symbol in between. So the combined query is [[Category:Technique]]|?Has display name. This query will retrieve all ATT&CK techniques along with their display name. To run this we just have to URL encode the combined query and place it in the URL. The final query is: https://attack.mitre.org/api.php?action=ask&format=jsonfm&query=%5B%5BCategory%3ATechnique%5D%5D%7C%3FHas%20display%20name .PARAMETER Sync Connects to the MITRE ATT&CK framework and dumps all its data to an object. The output of this is needed before running any other parameters. .PARAMETER Matrix Switch that you can use to display an up to date ATT&CK Matrix for Enterprise .PARAMETER Category Page selector switch. .PARAMETER </Data> 
    <Data Name="ScriptBlockId">1c97482f-51a2-4cf9-8abd-df9769b6e373</Data> 
    <Data Name="Path">C:\Tools\Invoke-ATTACKAPI-master\Invoke-ATTACKAPI.ps1</Data> 
  </EventData>
</Event>
```

## Data Dictionary

| Standard Name | Field Name | Type | Description | Sample Value |
| ---------------- | ---------------- | ---------------- | ---------------- | ---------------- |
| powershell_message_number | MessageNumber | integer | | 1 |
| powershell_parameter_binding | MessageTotal | integer | | 1 |
| powershell_scriptblock_text | ScriptBlockText | string | function Invoke-ATTACKAPI.. |  |
| powershell_scriptblock_id | ScriptBlockId | string | | 1c97482f-51a2-4cf9-8abd-df9769b6e373 |
| powershell_Path | Path | string | | C:\Tools\Invoke-ATTACKAPI-master\Invoke-ATTACKAPI.ps1 |
