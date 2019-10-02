---
title: Event ID 22 - DNSEvent (DNS query)
description: This event generates when a process executes a DNS query.
log.type: sysmon
sysmon.version: 10.0
sysmon.rule: DnsQuery
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 06/11/2019
---

# Event ID 22: DNSEvent (DNS query)

## Description

This event generates when a process executes a DNS query, whether the result is successful or fails, cached or not.[Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-22-dnsevent-dns-query)

## Event Log Illustration

<img src="https://github.com/Cyb3rWard0g/OSSEM/blob/master/resources/images/event-22.png" alt="Event 22 illustration" width="625" height="625">

## Event XML

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385F-C22A-43E0-BF4C-06F5698FFBD9}" /> 
    <EventID>22</EventID> 
    <Version>5</Version> 
    <Level>4</Level> 
    <Task>22</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2019-06-12T00:57:56.373798200Z" /> 
    <EventRecordID>6612437</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="2312" ThreadID="3252" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>DESKTOP-WARDOG.RIVENDELL.local</Computer> 
    <Security UserID="S-1-5-18" /> 
  </System>
  <EventData>
    <Data Name="RuleName" /> 
    <Data Name="UtcTime">2019-06-12 00:57:55.254</Data> 
    <Data Name="ProcessGuid">{A98268C1-4DDF-5D00-0000-00102D794100}</Data> 
    <Data Name="ProcessId">416</Data> 
    <Data Name="QueryName">chrome.google.com</Data> 
    <Data Name="QueryStatus">0</Data> 
    <Data Name="QueryResults">type: 5 www3.l.google.com;172.217.7.206;</Data> 
    <Data Name="Image">C:\Program Files (x86)\Google\Chrome\Application\chrome.exe</Data> 
  </EventData>
</Event>
```

## Data Dictionary

| Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
| ----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
| tag	|	RuleName |	string	| custom tag mapped to event. i.e ATT&CK technique ID	|	T1114 |
| event_date_creation |	UtcTime	| date | Time in UTC when event was created	| 2019-06-12 00:57:55.254 |
| process_guid	|	ProcessGuid	|	string	|	Process Guid of the process that executed the DNS query	|{A98268C1-4DDF-5D00-0000-00102D794100} |
| process_id	|	ProcessId	|	string	|	Process id of the process that executed the DNS query	| 416 |
| dst_host_name	|	QueryName	|	string	|	DNS query name	| chrome.google.com |
| dns_query_status	|	QueryStatus	|	string	|	DNS query status	| 0 |
| dns_query_results | QueryResults | string | DNS query results | type: 5 www3.l.google.com;172.217.7.206; |
| process_path | Image | string	| The full path related to the process that executed the DNS query | C:\Program Files (x86)\Google\Chrome\Application\chrome.exe |
