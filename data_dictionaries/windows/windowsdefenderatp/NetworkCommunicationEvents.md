---
title: NetworkCommunicationEvents
description: Network connection and related events.
log.type: Windows Defender ATP
author: Jared Atkinson (@jaredcatkinson)
date: 02/21/2019
---

# NetworkCommunicationEvents

## Description
Network connection and related events

## Event Log Illustration & Event XML

## Data Dictionary
|	Standard Name	|	Field Name	|	Type	|	Description	|	Sample Value	|
|	-------------	|	----------	|	----	|	-----------	|	------------	|
|	event_date_creation	|	EventTime	|	date	|	Date and time when the event was recorded	|		|
|		|	MachineId	|	string	|	Unique identifier for the machine in the service	|		|
|		|	ComputerName	|	string	|	Fully qualified domain name (FQDN) of the machine	|		|
|		|	ActionType	|	string	|	Type of activity that triggered the event	|		|
|	dst_ip	|	RemoteIP	|	string	|	IP address that was being connected to	|		|
|	dst_port	|	RemotePort	|	int	|	TCP port on the remote device that was being connected to	|		|
|	dst_host_name	|	RemoteUrl	|	string	|	URL or fully qualified domain name (FQDN) that was being connected to	|		|
|	src_ip	|	LocalIP	|	string	|	IP address assigned to the local machine used during communication	|		|
|	src_port	|	LocalPort	|	int	|	TCP port on the local machine used during communication	|		|
|	network_protocol	|	Protocol	|	string	|	IP protocol used, whether TCP or UDP	|		|
|	src_ip_type	|	LocalIPType	|	string	|		Type of IP address, for example Public, Private, Reserved, Loopback, Teredo, FourToSixMapping, and Broadcast	|		|
|	dst_ip_type	|	RemoteIPType	|	string	|	Type of IP address, for example Public, Private, Reserved, Loopback, Teredo, FourToSixMapping, and Broadcast	|		|
|	hash_sha1	|	InitiatingProcessSHA1	|	string	|	SHA-1 of the process (image file) that initiated the event	|		|
|	hash_md5	|	InitiatingProcessMD5	|	string	|	MD5 hash of the process (image file) that initiated the event	|		|
|	process_name	|	InitiatingProcessFileName	|	string	|	Name of the process that initiated the event	|		|
|	process_id	|	InitiatingProcessId	|	int	|	Process ID (PID) of the process that initiated the event	|		|
|	process_command_line	|	InitiatingProcessCommandLine	|	string	|	Command line used to run the process that initiated the event	|		|
|	process_creation_time	|	InitiatingProcessCreationTime	|	date	|	Date and time when the process that initiated the event was started	|		|
|	process_path	|	InitiatingProcessFolderPath	|	string	|	Folder containing the process (image file) that initiated the event	|		|
|	process_parent_name	|	InitiatingProcessParentFileName	|	string	|	Name of the parent process that spawned the process responsible for the event	|		|
|	process_parent_id	|	InitiatingProcessParentId	|	int	|	Process ID (PID) of the parent process that spawned the process responsible for the event	|		|
|	process_parent_creation_time	|	InitiatingProcessParentCreationTime	|	date	|	Date and time when the parent of the process responsible for the event was started	|		|
|	user_domain	|	InitiatingProcessAccountDomain	|	string	|	Domain of the account that ran the process responsible for the event	|		|
|	user_name	|	InitiatingProcessAccountName	|	string	|	User name of the account that ran the process responsible for the event	|		|
|	user_sid	|	InitiatingProcessAccountSid	|	string	|	Security Identifier (SID) of the account that ran the process responsible for the event	|		|
|	process_integrity_level	|	InitiatingProcessIntegrityLevel	|	string	|	Integrity level of the process that initiated the event. Windows assigns integrity levels to processes based on certain characteristics, such as if they were launched from an internet download. These integrity levels influence permissions to resources.	|		|
|	process_token_elevation	|	InitiatingProcessTokenElevation	|	string	|	Token type indicating the presence or absence of User Access Control (UAC) privilege elevation applied to the process that initiated the event	|		|
|		|	ReportId	|	long	|	Event identifier based on a repeating counter. To identify unique events, this column must be used in conjunction with the ComputerName and EventTime columns.	|		|
|		|	AppGuardContainerId	|	string	|	Identifier for the virtualized container used by Application Guard to isolate browser activity	|		|