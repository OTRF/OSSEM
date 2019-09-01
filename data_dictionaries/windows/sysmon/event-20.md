---
title: Event ID 20 - WmiEvent (WmiEventConsumer activity detected)
description: This event logs the registration of WMI consumers, recording the consumer name, log, and destination.
log.type: sysmon
sysmon.version: 9.01
sysmon.rule: WmiEvent
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/26/2019
---

# Event ID 20: WmiEvent (WmiEventConsumer activity detected)

## Description
This event logs the registration of WMI consumers, recording the consumer name, log, and destination.[Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-20-wmievent-wmieventconsumer-activity-detected)

## Event Log Illustration

<img src="https://github.com/Cyb3rWard0g/OSSEM/blob/master/resources/images/event-20.png" alt="Event 20 illustration" width="625" height="625">

## Event XML

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385f-c22a-43e0-bf4c-06f5698ffbd9}" /> 
    <EventID>20</EventID> 
    <Version>3</Version> 
    <Level>4</Level> 
    <Task>20</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2019-04-27T01:04:02.164205800Z" /> 
    <EventRecordID>3631726</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="1432" ThreadID="5672" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>WARDOG.RIVENDELL.local</Computer> 
    <Security UserID="S-1-5-18" /> 
  </System>
  <EventData>
    <Data Name="RuleName" /> 
    <Data Name="EventType">WmiConsumerEvent</Data> 
    <Data Name="UtcTime">2019-04-27 01:04:02.164</Data> 
    <Data Name="Operation">Created</Data> 
    <Data Name="User">RIVENDELL\cbrown</Data> 
    <Data Name="Name">"Updater"</Data> 
    <Data Name="Type">Command Line</Data> 
    <Data Name="Destination">"C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\powershell.exe -NonInteractive"</Data> 
  </EventData>
</Event>
```

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	tag	|	RuleName |	string	|	custom tag mapped to event. i.e ATT&CK technique ID	|	T1114 |
|	event_type	|	EventType	|	string	|	wmievent type 	|	WmiConsumerEvent	|
|	event_date_creation	|	UtcTime	|	date	|	Time in UTC when event was created	|	2018-09-11 23:12:46.606	|
|	wmi_operation	|	Operation	|	string	|	wmievent filter operation	|	Created |
|	user_name	|	User	|	string	|	user that created the wmi  consumer	|	DESKTOP-LFD11QP\pedro	|
|	wmi_consumer_name	|	Name	|	string	|	name of the consumer created	|	Updater	|
|	wmi_consumer_type	|	Type |	string	|	Type of wmi consumer	|	Command Line	|
| wmi_consumer_destination | Destination | string | command of consumer | C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\powershell.exe -nop -exec bypass -win hidden -noni -enc bm90ZXBhZC5leGU= |
