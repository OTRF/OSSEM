---
title: Event ID 3 - Network connection
description: The network connection event logs TCP/UDP connections on the machine.
log.type: sysmon
sysmon.version: 7.01
sysmon.rule: NetworkConnect
author: Roberto Rodriguez (@Cyb3rWard0g)
date: 04/11/2018
---

# Event ID 3: Network connection

## Description
The network connection event logs TCP/UDP connections on the machine. It is disabled by default. Each connection is linked to a process through the ProcessId and ProcessGUID fields. The event also contains the source and destination host names IP addresses, port numbers and IPv6 status.[Sysmon Source](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-3-network-connection)

## Event Log Illustration

![alt text](/OSSEM/resources/images/event-3.png "Event 3 illustration")

## Event XML:

```
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
  <System>
    <Provider Name="Microsoft-Windows-Sysmon" Guid="{5770385F-C22A-43E0-BF4C-06F5698FFBD9}" /> 
    <EventID>3</EventID> 
    <Version>5</Version> 
    <Level>4</Level> 
    <Task>3</Task> 
    <Opcode>0</Opcode> 
    <Keywords>0x8000000000000000</Keywords> 
    <TimeCreated SystemTime="2018-04-11T05:29:36.333863500Z" /> 
    <EventRecordID>11750109</EventRecordID> 
    <Correlation /> 
    <Execution ProcessID="2152" ThreadID="3236" /> 
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel> 
    <Computer>DESKTOP-WARDOG</Computer> 
    <Security UserID="S-1-5-18" /> 
  </System>
  <EventData>
    <Data Name="UtcTime">2018-04-11 05:29:35.394</Data> 
    <Data Name="ProcessGuid">{A98268C1-957F-5ACD-0000-0010EB030000}</Data> 
    <Data Name="ProcessId">4</Data> 
    <Data Name="Image">System</Data> 
    <Data Name="User">NT AUTHORITY\SYSTEM</Data> 
    <Data Name="Protocol">udp</Data> 
    <Data Name="Initiated">false</Data> 
    <Data Name="SourceIsIpv6">false</Data> 
    <Data Name="SourceIp">192.168.64.255</Data> 
    <Data Name="SourceHostname" /> 
    <Data Name="SourcePort">138</Data> 
    <Data Name="SourcePortName">netbios-dgm</Data> 
    <Data Name="DestinationIsIpv6">false</Data> 
    <Data Name="DestinationIp">192.168.64.135</Data> 
    <Data Name="DestinationHostname">DESKTOP-WARDOG.localdomain</Data> 
    <Data Name="DestinationPort">138</Data> 
    <Data Name="DestinationPortName">netbios-dgm</Data> 
  </EventData>
</Event>
```