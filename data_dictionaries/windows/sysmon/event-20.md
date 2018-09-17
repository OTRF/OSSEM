---
title: Event ID 20 - WmiEvent (WmiEventConsumer activity detected)
description: This event logs the registration of WMI consumers, recording the consumer name, log, and destination.
log.type: sysmon
sysmon.version: 8.08
sysmon.rule: WmiEvent
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 09/12/2018
---

# Event ID 19: WmiEvent (WmiEventFilter activity detected)

## Description
This event logs the registration of WMI consumers, recording the consumer name, log, and destination.[Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-20-wmievent-wmieventconsumer-activity-detected)

## Event Log Illustration

<img src="https://github.com/Cyb3rWard0g/OSSEM/blob/master/resources/images/event-20.png" alt="Event 20 illustration" width="625" height="625">

## Event XML

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385F-C22A-43E0-BF4C-06F5698FFBD9}" /> 
    <EventID>20</EventID> 
    <Version>3</Version> 
    <Level>4</Level> 
    <Task>20</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2018-09-12T00:41:00.762457400Z" /> 
    <EventRecordID>480410</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="2204" ThreadID="5784" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>DESKTOP-LFD11QP</Computer> 
    <Security UserID="S-1-5-18" /> 
  </System>
  <EventData>
    <Data Name="RuleName" /> 
    <Data Name="EventType">WmiConsumerEvent</Data> 
    <Data Name="UtcTime">2018-09-12 00:41:00.760</Data> 
    <Data Name="Operation">Created</Data> 
    <Data Name="User">DESKTOP-LFD11QP\pedro</Data> 
    <Data Name="Name">"Updater"</Data> 
    <Data Name="Type">Command Line</Data> 
    <Data Name="Destination">"C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\powershell.exe -nop -exec bypass -win hidden -noni -enc bm90ZXBhZC5leGU="</Data> 
  </EventData>
</Event>
```

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	tag	|	RuleName |	string	|	custom tag mapped to event. i.e ATT&CK technique ID	|	T1114 |
|	event_type	|	EventType	|	string	|	wmievent type 	|	WmiConsumerEvent	|
|	event_creation_time	|	UtcTime	|	date	|	Time in UTC when event was created	|	2018-09-11 23:12:46.606	|
|	wmi_operation	|	Operation	|	string	|	wmievent filter operation	|	Created |
|	user_name	|	User	|	string	|	user that created the wmi  consumer	|	DESKTOP-LFD11QP\pedro	|
|	wmi_consumer_name	|	Name	|	string	|	name of the consumer created	|	Updater	|
|	wmi_consumer_type	|	Type |	string	|	Type of wmi consumer	|	Command Line	|
| wmi_consumer_destination | Destination | string | command of consumer | C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\powershell.exe -nop -exec bypass -win hidden -noni -enc bm90ZXBhZC5leGU= |