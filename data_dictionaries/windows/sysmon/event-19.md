---
title: Event ID 19 - WmiEvent (WmiEventFilter activity detected)
description: This event logs when a WMI event filter is registered, which is a method used by malware to execute
log.type: sysmon
sysmon.version: 9.01
sysmon.rule: WmiEvent
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/26/2019
---

# Event ID 19: WmiEvent (WmiEventFilter activity detected)

## Description
When a WMI event filter is registered, which is a method used by malware to execute, this event logs the WMI namespace, filter name and filter expression.[Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-19-wmievent-wmieventfilter-activity-detected)

## Event Log Illustration

<img src="https://github.com/Cyb3rWard0g/OSSEM/blob/master/resources/images/event-19.png" alt="Event 19 illustration" width="625" height="625">

## Event XML

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385f-c22a-43e0-bf4c-06f5698ffbd9}" /> 
    <EventID>19</EventID> 
    <Version>3</Version> 
    <Level>4</Level> 
    <Task>19</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2019-04-27T01:04:02.146396600Z" /> 
    <EventRecordID>3631722</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="1432" ThreadID="5672" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>WARDOG.RIVENDELL.local</Computer> 
    <Security UserID="S-1-5-18" /> 
  </System>
  <EventData>
    <Data Name="RuleName" /> 
    <Data Name="EventType">WmiFilterEvent</Data> 
    <Data Name="UtcTime">2019-04-27 01:04:02.146</Data> 
    <Data Name="Operation">Created</Data> 
    <Data Name="User">RIVENDELL\cbrown</Data> 
    <Data Name="EventNamespace">"root\\CimV2"</Data> 
    <Data Name="Name">"Updater"</Data> 
    <Data Name="Query">"SELECT * FROM __InstanceModificationEvent WITHIN 60 WHERE TargetInstance ISA 'Win32_PerfFormattedData_PerfOS_System' AND TargetInstance.SystemUpTime >= 240 AND TargetInstance.SystemUpTime < 325"</Data> 
  </EventData>
</Event>
```

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	tag	|	RuleName |	string	|	custom tag mapped to event. i.e ATT&CK technique ID	|	T1114 |
|	event_type	|	EventType	|	string	|	wmievent type 	|	WmiFilterEvent	|
|	event_date_creation	|	UtcTime	|	date	|	Time in UTC when event was created	|	2018-09-11 23:12:46.606	|
|	wmi_operation	|	Operation	|	string	|	wmievent filter operation	|	Created |
|	user_name	|	User	|	string	|	user that created the wmi filter	|	DESKTOP-LFD11QP\pedro	|
|	wmi_namespace	|	EventNamespace	|	string	|	event namespace where the wmi clas	|	root\\CimV2	|
|	wmi_filter_name	|	Name	|	string	|	Wmi filter name being created	|	Updater	|
| wmi_query | Query | string | wmi filter query | "SELECT * FROM __InstanceModificationEvent WITHIN 60 WHERE TargetInstance ISA 'Win32_PerfFormattedData_PerfOS_System' AND TargetInstance.SystemUpTime >= 240 AND TargetInstance.SystemUpTime < 325" |