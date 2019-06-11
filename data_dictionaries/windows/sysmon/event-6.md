---
title: Event ID 6 - Driver loaded
description: The driver loaded events provides information about a driver being loaded on the system.
log.type: sysmon
sysmon.version: 9.01
sysmon.rule: DriverLoad
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/26/2019
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
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385f-c22a-43e0-bf4c-06f5698ffbd9}" /> 
    <EventID>6</EventID> 
    <Version>3</Version> 
    <Level>4</Level> 
    <Task>6</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2019-04-27T00:11:22.407923200Z" /> 
    <EventRecordID>3611351</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="2332" ThreadID="3796" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>WARDOG.RIVENDELL.local</Computer> 
    <Security UserID="S-1-5-18" /> 
  </System>
  <EventData>
    <Data Name="RuleName" /> 
    <Data Name="UtcTime">2019-04-27 00:11:01.735</Data> 
    <Data Name="ImageLoaded">C:\Windows\System32\drivers\vmusbmouse.sys</Data> 
    <Data Name="Hashes">SHA1=651C73ABD8BE1B2A9C97FBBD7912A9050B4D555E,MD5=1F211FD46A2C49D0A2D3CF7160726292,SHA256=7AC0FE224B03EA3568A9A6F74A8BC30064DBF1A73A22C4AC89120C669537B31E,IMPHASH=0AC7A1ED563A3C7C6706B591B9D8E120</Data> 
    <Data Name="Signed">true</Data> 
    <Data Name="Signature">VMware, Inc.</Data> 
    <Data Name="SignatureStatus">Valid</Data> 
  </EventData>
</Event>
```

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	event_date_creation	|	UtcTime	|	date	|	Time in UTC when event was created	|	4/11/18 5:21	|
|	driver_loaded	|	ImageLoaded	|	string	|	full path of the driver loaded	|	C:\ProgramData\Microsoft\Windows Defender\Definition Updates{741285CC-BF49-492C-90BE-E84BD6CADD73}\MpKsl4d223a5a.sys	|
|	hash	|	Hashes	|	string	|	Hashes captured by sysmon driver	|	SHA1=38310AD6805DC31D5AA61BE182689D63060ACE94, MD5=BF2513029E231BE96D82F7C3ABFF87F4, SHA256=F6DB64112CC50EEE495E2D7C61B8BDBE757A31B03144B0396615FD38C312824E, IMPHASH=06D4A412CF7F5363C49E629BF34446B3	|
|	driver_is_signed	|	Signed	|	boolean	|	is the driver loaded signed	|	TRUE	|
|	driver_signature	|	Signature	|	string	|	The signer	|	Microsoft Corporation	|
|	driver_signature_status	|	SignatureStatus	|	string	|	status of the signature (i.e valid)	|	Valid	|