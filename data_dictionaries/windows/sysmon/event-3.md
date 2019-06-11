---
title: Event ID 3 - Network connection
description: The network connection event logs TCP/UDP connections on the machine.
log.type: sysmon
sysmon.version: 9.01
sysmon.rule: NetworkConnect
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/26/2019
---

# Event ID 3: Network connection

## Description
The network connection event logs TCP/UDP connections on the machine. It is disabled by default. Each connection is linked to a process through the ProcessId and ProcessGUID fields. The event also contains the source and destination host names IP addresses, port numbers and IPv6 status.[Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-3-network-connection)

## Event Log Illustration

<img src="https://github.com/Cyb3rWard0g/OSSEM/blob/master/resources/images/event-3.png" alt="Event 3 illustration" width="625" height="625">

## Event XML:

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385f-c22a-43e0-bf4c-06f5698ffbd9}" /> 
    <EventID>3</EventID> 
    <Version>5</Version> 
    <Level>4</Level> 
    <Task>3</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2019-04-27T00:10:32.964282300Z" /> 
    <EventRecordID>3606939</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="2336" ThreadID="3140" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>WARDOG.RIVENDELL.local</Computer> 
    <Security UserID="S-1-5-18" /> 
  </System>
  <EventData>
    <Data Name="RuleName" /> 
    <Data Name="UtcTime">2019-04-27 00:10:31.843</Data> 
    <Data Name="ProcessGuid">{1c9fdc81-9d71-5cc3-0000-001029c30000}</Data> 
    <Data Name="ProcessId">820</Data> 
    <Data Name="Image">C:\Windows\System32\lsass.exe</Data> 
    <Data Name="User">NT AUTHORITY\SYSTEM</Data> 
    <Data Name="Protocol">tcp</Data> 
    <Data Name="Initiated">true</Data> 
    <Data Name="SourceIsIpv6">false</Data> 
    <Data Name="SourceIp">192.168.64.137</Data> 
    <Data Name="SourceHostname">DESKTOP-LFD11QP.RIVENDELL.local</Data> 
    <Data Name="SourcePort">49767</Data> 
    <Data Name="SourcePortName" /> 
    <Data Name="DestinationIsIpv6">false</Data> 
    <Data Name="DestinationIp">192.168.64.178</Data> 
    <Data Name="DestinationHostname">DC-WD-001</Data> 
    <Data Name="DestinationPort">88</Data> 
    <Data Name="DestinationPortName">kerberos</Data> 
  </EventData>
</Event>
```

## Data Dictionary

|	Standard Name	| Field Name |	Type	|	Description	|	Sample Value	|
|	----------------	|	----------------	|	----------------	|	----------------	|	----------------	|
|	event_date_creation	|	UtcTime	|	date	|	Time in UTC when event was created	|	4/11/18 5:29	|
|	process_guid	|	ProcessGuid	|	string	|	Process Guid of the process that made the network connection	|	{A98268C1-957F-5ACD-0000-0010EB030000}	|
|	process_id	|	ProcessId	|	integer	|	Process ID used by the os to identify the process that made the network connection	|	4	|
|	process_name	|	Image	|	string	|	File path of the process that made the network connection	|	System	|
|	user_name	|	User	|	string	|	Name of the account who made the network connection. It usually containes domain name and user name	|	NT AUTHORITY\SYSTEM	|
|	network_protocol	|	Protocol	|	string	|	Protocol being used for the network connection	|	udp	|
|	network_connection_initiated	|	Initiated	|	boolean	|	Indicated process initiated tcp connection	|	FALSE	|
|	src_is_ipv6	|	SourceIsIpv6	|	boolean	|	is the source ip an Ipv6	|	FALSE	|
|	src_ip	|	SourceIp	|	ip	|	source ip address that made the network connection	|	192.168.64.255	|
|	src_host_name	|	SourceHostname	|	string	|	name of the host that made the network connection	|	computer_name or none for broadcast	|
|	src_port |	SourcePort	|	integer	|	source port number	|	138	|
|	src_port_name	|	SourcePortName	|	string	|	name of the source port being used (i.e. netbios-dgm)	|	netbios-dgm	|
|	dst_is_ipv6	|	DestinationIsIpv6	|	boolean	|	is the destination ip an Ipv6	|	C:\Windows\System32\cmd.exe	|
|	dst_ip	|	DestinationIp	|	ip	|	ip address destination	|	192.168.64.135	|
|	dst_port |	DestinationPort	|	integer	|	destination port number	|	138	|
|	dst_port_name	|	DestinationPortName	|	string	|	name of the destination port	|	netbios-dgm	|
