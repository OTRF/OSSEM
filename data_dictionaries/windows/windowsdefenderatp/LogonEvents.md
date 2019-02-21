---
title: LogonEvents
description: Login and other authentication events.
log.type: Windows Defender ATP
author: Jared Atkinson (@jaredcatkinson)
date: 02/21/2019
---

|	Standard Name	|	Field Name	|	Type	|	Description	|	Sample Value	|
|	-------------	|	----------	|	----	|	-----------	|	------------	|
|	event_date_creation	|	EventTime	|	date	|	Date and time when the event was recorded	|		|
|		|	MachineId	|	string	|	Unique identifier for the machine in the service	|		|
|		|	ComputerName	|	string	|	Fully qualified domain name (FQDN) of the machine	|		|
|		|	ActionType	|	string	|	Type of activity that triggered the event	|		|
|	user_domain	|	AccountDomain	|	string	|	Domain of the account	|		|
|	user_name	|	AccountName	|	string	|	User name of the account	|		|
|	user_sid	|	AccountSid	|	string	|	Security Identifier (SID) of the account	|		|
|		|	LogonType	|	string	|	Type of logon session	|		|
|		|	LogonId	|	string	|	Identifier for a logon session. This identifier is unique on the same machine only between restarts.	|		|
|	dst_host_name	|	RemoteComputerName	|	string	|	Name of the machine that performed a remote operation on the affected machine. Depending on the event being reported, this name could be a fully-qualified domain name (FQDN), a NetBIOS name, or a host name without domain information.	|		|
|	dst_ip	|	RemoteIP	|	string	|	IP address that was being connected to	|		|
|		|	RemoteIPType	|	string	|	Type of IP address, for example Public, Private, Reserved, Loopback, Teredo, FourToSixMapping, and Broadcast	|		|
|	dst_port	|	RemotePort	|	int	|	TCP port on the remote device that was being connected to	|		|
|		|	AdditionalFields	|	string	|	Additional information about the event in JSON array format	|		|
|	process_user_domain	|	InitiatingProcessAccountDomain	|	string	|	Domain of the account that ran the process responsible for the event	|		|
|	process_user_name	|	InitiatingProcessAccountName	|	string	|	User name of the account that ran the process responsible for the event	|		|
|	process_user_sid	|	InitiatingProcessAccountSid	|	string	|	Security Identifier (SID) of the account that ran the process responsible for the event	|		|
|	process_integrity_level	|	InitiatingProcessIntegrityLevel	|	string	|	Integrity level of the process that initiated the event. Windows assigns integrity levels to processes based on certain characteristics, such as if they were launched from an internet download. These integrity levels influence permissions to resources.	|		|
|	process_token_elevation	|	InitiatingProcessTokenElevation	|	string	|	Token type indicating the presence or absence of User Access Control (UAC) privilege elevation applied to the process that initiated the event	|		|
|	process_hash_sha1	|	InitiatingProcessSHA1	|	string	|	SHA-1 of the process (image file) that initiated the event	|		|
|	process_hash_md5	|	InitiatingProcessMD5	|	string	|	MD5 hash of the process (image file) that initiated the event	|		|
|	process_name	|	InitiatingProcessFileName	|	string	|	Name of the process that initiated the event	|		|
|	process_id	|	InitiatingProcessId	|	int	|	Process ID (PID) of the process that initiated the event	|		|
|	process_command_line	|	InitiatingProcessCommandLine	|	string	|	Command line used to run the process that initiated the event	|		|
|	process_creation_time	|	InitiatingProcessCreationTime	|	date	|	Date and time when the process that initiated the event was started	|		|
|	process_path	|	InitiatingProcessFolderPath	|	string	|	Folder containing the process (image file) that initiated the event	|		|
|	process_parent_id	|	InitiatingProcessParentId	|	int	|	Process ID (PID) of the parent process that spawned the process responsible for the event	|		|
|	process_parent_name	|	InitiatingProcessParentFileName	|	string	|	Name of the parent process that spawned the process responsible for the event	|		|
|	process_parent_creation_time	|	InitiatingProcessParentCreationTime	|	date	|	Date and time when the parent of the process responsible for the event was started	|		|
|		|	ReportId	|	long	|	Event identifier based on a repeating counter. To identify unique events, this column must be used in conjunction with the ComputerName and EventTime columns.	|		|
|		|	AppGuardContainerId	|	string	|	Identifier for the virtualized container used by Application Guard to isolate browser activity	|		|