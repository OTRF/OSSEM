---
title: Event ID 7 - Image loaded
description: The image loaded event logs when a module is loaded in a specific process.
log.type: sysmon
sysmon.version: 9.01
sysmon.rule: ImageLoad
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/26/2019
---

# Event ID 7: Image loaded

## Description
The image loaded event logs when a module is loaded in a specific process. This event is disabled by default and needs to be configured with the –l option. It indicates the process in which the module is loaded, hashes and signature information. The signature is created asynchronously for performance reasons and indicates if the file was removed after loading. This event should be configured carefully, as monitoring all image load events will generate a large number of events.[Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-7-image-loaded)

## Event Log Illustration

<img src="https://github.com/Cyb3rWard0g/OSSEM/blob/master/resources/images/event-7.png" alt="Event 7 illustration" width="625" height="625">

## Event XML

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385f-c22a-43e0-bf4c-06f5698ffbd9}" /> 
    <EventID>7</EventID> 
    <Version>3</Version> 
    <Level>4</Level> 
    <Task>7</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2019-04-27T00:11:22.874806200Z" /> 
    <EventRecordID>3611661</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="2332" ThreadID="3796" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>WARDOG.RIVENDELL.local</Computer> 
    <Security UserID="S-1-5-18" /> 
  </System>
  <EventData>
    <Data Name="RuleName" /> 
    <Data Name="UtcTime">2019-04-27 00:11:02.553</Data> 
    <Data Name="ProcessGuid">{1c9fdc81-9e16-5cc3-0000-001062ac0000}</Data> 
    <Data Name="ProcessId">608</Data> 
    <Data Name="Image">C:\Windows\System32\csrss.exe</Data> 
    <Data Name="ImageLoaded">C:\Windows\System32\sxssrv.dll</Data> 
    <Data Name="FileVersion">10.0.17763.437 (WinBuild.160101.0800)</Data> 
    <Data Name="Description">Windows SxS Server DLL</Data> 
    <Data Name="Product">Microsoft® Windows® Operating System</Data> 
    <Data Name="Company">Microsoft Corporation</Data> 
    <Data Name="Hashes">SHA1=96BAC143846FCA945A5535DD2F96E3DFA322322F,MD5=B08257DDEACDEFFFCF91A743795CBF11,SHA256=6935D53B5F05833E76F87CA3A2A5C5B5D0EE05DD7953487492C8EDCC9E5F6F8F,IMPHASH=4BF8E692F4BD33947C8B7B301408157E</Data> 
    <Data Name="Signed">true</Data> 
    <Data Name="Signature">Microsoft Windows</Data> 
    <Data Name="SignatureStatus">Valid</Data> 
  </EventData>
</Event>
```

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	event_creation_time	|	UtcTime	|	date	|	Time in UTC when event was created	|	4/11/18 5:46	|
|	process_guid	|	ProcessGuid	|	string	|	Process Guid of the process that loaded the image	|	{A98268C1-A12A-5ACD-0000-0010E4C8B300}	|
|	process_id	|	ProcessId	|	integer	|	Process ID used by the os to identify the process that loaded the image	|	3532	|
|	process_name	|	Image	|	string	|	File name of the process that loaded the image	|	cmd.exe	|
|	process_path	|	Image	|	string	|	File path of the process that loaded the image	|	C:\Windows\System32\cmd.exe	|
|	module_loaded	|	ImageLoaded	|	string	|	full path of the image loaded	|	C:\Windows\System32\msvcrt.dll	|
|	file_version	|	FileVersion	|	string	|	Version of the image loaded	|	7.0.16299.125 (WinBuild.160101.0800)	|
|	file_description	|	Description	|	string	|	Description of the image loaded	|	Windows NT CRT DLL	|
|	file_product	|	Product	|	string	|	Product name the image loaded belongs to	|	Microsoft® Windows® Operating System	|
|	file_company	|	Company	|	string	|	Company name the image loaded belongs to	|	Microsoft Corporation	|
|	hash	|	Hashes	|	string	|	hash is a full hash of the file with the algorithms in the HashType field	|	SHA1=AEB9839D02C99A3E7EED1F12671C3F827221EDF8, MD5=68195105C7D9A2B5DF5BB82ECA521092, SHA256=556FF2B03495E2117223E5697B54253F30BD10ED3C67468947D79945168A624A, IMPHASH=C16CC99941EF5E18707133A2532B7D0C	|
|	module_is_signed	|	Signed	|	boolean	|	is the image loaded signed	|	TRUE	|
|	module_signature	|	Signature	|	string	|	The signer	|	Microsoft Corporation	|
|	module_signature_status	|	SignatureStatus	|	string	|	status of the signature (i.e valid)	|	Valid	|