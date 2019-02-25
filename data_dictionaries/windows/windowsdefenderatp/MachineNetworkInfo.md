---
title: MachineNetworkInfo
description: Network properties of machines, including adapters, IP and MAC addresses, as well as connected networks and domains.
log.type: Windows Defender ATP
author: Jared Atkinson (@jaredcatkinson)
date: 02/21/2019
---

# MachineNetworkInfo

## Description
Network properties of machines, including adapters, IP and MAC addresses, as well as connected networks and domains

## Event Log Illustration & Event XML

## Data Dictionary
|	Standard Name	|	Field Name	|	Type	|	Description	|	Sample Value	|
|	-------------	|	----------	|	----	|	-----------	|	------------	|
|	event_date_creation	|	EventTime	|	date	|	Date and time when the event was recorded	|		|
|		|	MachineId	|	string	|	Unique identifier for the machine in the service	|		|
|		|	ComputerName	|	string	|	Fully qualified domain name (FQDN) of the machine	|		|
|		|	ReportId	|	long	|	Event identifier based on a repeating counter. To identify unique events, this column must be used in conjunction with the ComputerName and EventTime columns.	|		|
|		|	NetworkAdapterName	|	string	|	Name of the network adapter	|		|
|		|	MacAddress	|		|	string	|	MAC address of the network adapter	|
|		|	NetworkAdapterType	|	string	|	Network adapter type	|		|
|		|	NetworkAdapterStatus	|	string	|	Operational status of the network adapter	|		|
|		|	TunnelType	|	string	|	Tunneling protocol, if the interface is used for this purpose, for example 6to4, Teredo, ISATAP, PPTP, SSTP, and SSH	|		|
|		|	ConnectedNetwork	|	string	|	Networks that the adapter is connected to. Each JSON array contains the network name, category (public, private or domain), a description, and a flag indicating if it’s connected publicly to the internet.	|		|
|		|	DnsAddress	|	string	|	DNS server addresses in JSON array format	|		|
|		|	IPv4Dhcp	|	string	|	IPv4 address of DHCP server	|		|
|		|	IPv6Dhcp	|	string	|	IPv6 address of DHCP server	|		|
|		|	DefaultGateways	|	string	|	Default gateway addresses in JSON array format	|		|
|		|	IPAddresses	|	string	|	JSON array containing all the IP addresses assigned to the adapter, along with their respective subnet prefix and IP address space, such as public, private, or link-local	|		|