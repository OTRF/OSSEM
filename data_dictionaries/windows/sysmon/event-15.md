---
title: Event ID 15 - FileCreateStreamHash
description: This event logs when a named file stream is created.
log.type: sysmon
sysmon.version: 9.01
sysmon.rule: FileCreateStreamHash
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/26/2019
---

# Event ID 15: FileCreateStreamHash

## Description
This event logs when a named file stream is created, and it generates events that log the hash of the contents of the file to which the stream is assigned (the unnamed stream), as well as the contents of the named stream. There are malware variants that drop their executables or configuration settings via browser downloads, and this event is aimed at capturing that based on the browser attaching a Zone.Identifier “mark of the web” stream.[Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-15-filecreatestreamhash)

## Event Log Illustration

<img src="https://github.com/Cyb3rWard0g/OSSEM/blob/master/resources/images/event-15.png" alt="Event 15 illustration" width="625" height="625">

## Event XML

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385f-c22a-43e0-bf4c-06f5698ffbd9}" /> 
    <EventID>15</EventID> 
    <Version>2</Version> 
    <Level>4</Level> 
    <Task>15</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2019-04-27T00:56:56.489937100Z" /> 
    <EventRecordID>3625973</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="1432" ThreadID="6344" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>WARDOG.RIVENDELL.local</Computer> 
    <Security UserID="S-1-5-18" /> 
  </System>
  <EventData>
    <Data Name="RuleName" /> 
    <Data Name="UtcTime">2019-04-27 00:56:56.485</Data> 
    <Data Name="ProcessGuid">{1c9fdc81-9f43-5cc3-0000-001049783700}</Data> 
    <Data Name="ProcessId">5220</Data> 
    <Data Name="Image">C:\WINDOWS\system32\browser_broker.exe</Data> 
    <Data Name="TargetFilename">C:\Users\cbrown\MicrosoftEdgeBackups\backups\MicrosoftEdgeBackup20190426\MicrosoftEdgeCookiesBackup.dat</Data> 
    <Data Name="CreationUtcTime">2019-04-27 00:56:56.481</Data> 
    <Data Name="Hash">SHA1=DA39A3EE5E6B4B0D3255BFEF95601890AFD80709,MD5=D41D8CD98F00B204E9800998ECF8427E,SHA256=E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855,IMPHASH=00000000000000000000000000000000</Data> 
  </EventData>
</Event>
```

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
| tag	|	RuleName |	string	| custom tag mapped to event. i.e ATT&CK technique ID	|	T1114 |
|	event_date_creation	|	UtcTime	|	date	|	Time in UTC when event was created	|	4/11/18 5:25	|
|	process_guid	|	ProcessGuid	|	string	|	Process Guid of the process that created the named file stream	|	{A98268C1-A8A0-5ACD-0000-001087DEBF00}	|
|	process_id	|	ProcessId	|	integer	|	Process ID used by the os to identify the process that created the named file stream	|	6972	|
|	process_name	|	Image	|	string	|	File name of the process that created the named file stream	|	chrome.exe	|
|	process_path	|	Image	|	string	|	File path of the process that created the named file stream	|	C:\Program Files (x86)\Google\Chrome\Application\chrome.exe	|
|	file_name	|	TargetFilename	|	string	|	Name of the file	|	C:\Users\wardog\Downloads\a0fa35bc5badf505f803921f0fe40971-4cf6bad280c7b66e21bb8e96ffe2f968ca460e0d.zip:Zone.Identifier	|
|	file_creation_time	|	CreationUtcTime	|	date	|	File download time	|	4/11/18 6:18	|
|	hash	|	Hash	|	string	|	hash is a full hash of the file with the algorithms in the HashType field	|	SHA1=F897DA14CF93C872CE821F549C34B848E345C8AC, MD5=697C69E7BB023075F14BC0BE25B875D8, SHA256=3157F3E7A854A13A40FFC79472C319E5B7C744B50D869D6E45F40CD4218539C5, IMPHASH=00000000000000000000000000000000	|
