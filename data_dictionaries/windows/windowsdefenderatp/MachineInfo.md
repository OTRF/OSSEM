---
title: MachineInfo
description: Machine information, including OS information.
log.type: Windows Defender ATP
author: Jared Atkinson (@jaredcatkinson)
date: 02/21/2019
---

# MachineInfo

## Description
Machine information, including OS information

## Event Log Illustration & Event XML

## Data Dictionary
|	Standard Name	|	Field Name	|	Type	|	Description	|	Sample Value	|
|	-------------	|	----------	|	----	|	-----------	|	------------	|
|	event_date_creation	|	EventTime	|	date	|	Date and time when the event was recorded	|		|
|		|	MachineId	|	string	|	Unique identifier for the machine in the service	|		|
|		|	ComputerName	|	string	|	Fully qualified domain name (FQDN) of the machine	|		|
|		|	ClientVersion	|		|		|		|
|		|	PublicIP	|	string	|	Public IP address used by the onboarded machine to connect to the Windows Defender ATP service. This could be the IP address of the machine itself, a NAT device, or a proxy.	|		|
|		|	OSArchitecture	|	string	|	Architecture of the operating system running on the machine	|		|
|		|	OSPlatform	|	string	|	Platform of the operating system running on the machine. This indicates specific operating systems, including variations within the same family, such as Windows 10 and Windows 7.	|		|
|		|	OSBuild	|	string	|	Build version of the operating system running on the machine	|		|
|		|	ISAzureADJoined	|	boolean	|	Boolean indicator of whether machine is joined to the Azure Active Directory	|		|
|		|	LoggedOnUsers	|	string	|	List of all users that are logged on the machine at the time of the event in JSON array format	|		|
|		|	MachineGroup	|	string	|	Machine group of the machine. This group is used by role-based access control to determine access to the machine.	|		|
|		|	ReportId	|	long	|	Event identifier based on a repeating counter. To identify unique events, this column must be used in conjunction with the ComputerName and EventTime columns.	|		|
|		|	OSVersion	|		|		|		|