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
|	@timestamp	|	EventTime	|	date	|	Date and time when the event was recorded	|		|
|	machine_id	|	MachineId	|	string	|	Unique identifier for the machine in the service	|		|
|	computer_name	|	ComputerName	|	string	|	Fully qualified domain name (FQDN) of the machine	|		|
|	client_version	|	ClientVersion	|		|		|		|
|	public_ip	|	PublicIP	|	string	|	Public IP address used by the onboarded machine to connect to the Windows Defender ATP service. This could be the IP address of the machine itself, a NAT device, or a proxy.	|		|
|	os_architecture	|	OSArchitecture	|	string	|	Architecture of the operating system running on the machine	|		|
|	os_platform	|	OSPlatform	|	string	|	Platform of the operating system running on the machine. This indicates specific operating systems, including variations within the same family, such as Windows 10 and Windows 7.	|		|
|	os_build	|	OSBuild	|	string	|	Build version of the operating system running on the machine	|		|
|	is_azure_ad_joined	|	ISAzureADJoined	|	boolean	|	Boolean indicator of whether machine is joined to the Azure Active Directory	|		|
|	logged_on_users	|	LoggedOnUsers	|	string	|	List of all users that are logged on the machine at the time of the event in JSON array format	|		|
|	machine_group	|	MachineGroup	|	string	|	Machine group of the machine. This group is used by role-based access control to determine access to the machine.	|		|
|	report_id	|	ReportId	|	long	|	Event identifier based on a repeating counter. To identify unique events, this column must be used in conjunction with the ComputerName and EventTime columns.	|		|
|	os_version	|	OSVersion	|		|		|		|
