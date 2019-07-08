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
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385F-C22A-43E0-BF4C-06F5698FFBD9}" /> 
    <EventID>7</EventID> 
    <Version>3</Version> 
    <Level>4</Level> 
    <Task>7</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2019-06-12T00:53:09.437770100Z" /> 
    <EventRecordID>6562598</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="2312" ThreadID="3808" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>DESKTOP-WARDOG.RIVENDELL.local</Computer> 
    <Security UserID="S-1-5-18" /> 
    </System>
  <EventData>
    <Data Name="RuleName" /> 
    <Data Name="UtcTime">2019-06-12 00:53:09.400</Data> 
    <Data Name="ProcessGuid">{A98268C1-4902-5D00-0000-0010B06C0300}</Data> 
    <Data Name="ProcessId">3336</Data> 
    <Data Name="Image">C:\Windows\System32\wbem\WmiPrvSE.exe</Data> 
    <Data Name="ImageLoaded">C:\Windows\Microsoft.NET\Framework64\v2.0.50727\mscorwks.dll</Data> 
    <Data Name="FileVersion">2.0.50727.8941 (WinRelRS4.050727-8900)</Data> 
    <Data Name="Description">Microsoft .NET Runtime Common Language Runtime - WorkStation</Data> 
    <Data Name="Product">Microsoft® .NET Framework</Data> 
    <Data Name="Company">Microsoft Corporation</Data> 
    <Data Name="OriginalFileName">?</Data> 
    <Data Name="Hashes">SHA1=7E409FF7E28EC847E08DC329AD39609CA8198726,MD5=0485F3060BC9B591D7934214854D6062,SHA256=89E265B3339C6D159A9E8D58B2C6B289739C08C872CBD1361D3ECE2E35BE4285,IMPHASH=935807DE361D1D4C00670D8AAF7F807F</Data> 
    <Data Name="Signed">true</Data> 
    <Data Name="Signature">Microsoft Corporation</Data> 
    <Data Name="SignatureStatus">Valid</Data> 
  </EventData>
</Event>
```

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
| tag	|	RuleName |	string	| custom tag mapped to event. i.e ATT&CK technique ID	|	T1114 |
|	event_date_creation	|	UtcTime	|	date	|	Time in UTC when event was created	|	4/11/18 5:46	|
|	process_guid	|	ProcessGuid	|	string	|	Process Guid of the process that loaded the image	|	{A98268C1-A12A-5ACD-0000-0010E4C8B300}	|
|	process_id	|	ProcessId	|	integer	|	Process ID used by the os to identify the process that loaded the image	|	3532	|
|	process_name	|	Image	|	string	|	File path of the process that loaded the image	|	C:\Windows\System32\cmd.exe	|
|	module_loaded	|	ImageLoaded	|	string	|	full path of the image loaded	|	C:\Windows\System32\msvcrt.dll	|
|	file_version	|	FileVersion	|	string	|	Version of the image loaded	|	7.0.16299.125 (WinBuild.160101.0800)	|
|	file_description	|	Description	|	string	|	Description of the image loaded	|	Windows NT CRT DLL	|
|	file_product	|	Product	|	string	|	Product name the image loaded belongs to	|	Microsoft® Windows® Operating System	|
|	file_company	|	Company	|	string	|	Company name the image loaded belongs to	|	Microsoft Corporation	|
| file_name_original | OriginalFileName | string | original file name | ? |
|	hash	|	Hashes	|	string	|	hash is a full hash of the file with the algorithms in the HashType field	|	SHA1=AEB9839D02C99A3E7EED1F12671C3F827221EDF8, MD5=68195105C7D9A2B5DF5BB82ECA521092, SHA256=556FF2B03495E2117223E5697B54253F30BD10ED3C67468947D79945168A624A, IMPHASH=C16CC99941EF5E18707133A2532B7D0C	|
|	module_is_signed	|	Signed	|	boolean	|	is the image loaded signed	|	TRUE	|
|	module_signature	|	Signature	|	string	|	The signer	|	Microsoft Corporation	|
|	module_signature_status	|	SignatureStatus	|	string	|	status of the signature (i.e valid)	|	Valid	|