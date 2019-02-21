---
title: ProcessCreationEvents
description: Process creation and related events.
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
|	process_name	|	FileName	|	string	|	Name of the file that the recorded action was applied to	|		|
|	process_path	|	FolderPath	|	string	|	Folder containing the file that the recorded action was applied to	|		|
|	sha1_hash	|	SHA1	|	string	|	SHA-1 of the file that the recorded action was applied to	|		|
|	md5_hash	|	MD5	|	string	|	MD5 hash of the file that the recorded action was applied to	|		|
|	process_id	|	ProcessId	|	int	|	Process ID (PID) of the newly created process	|		|
|	process_command_line	|	ProcessCommandLine	|	string	|	Command line used to create the new process	|		|
|	process_integrity_level	|	ProcessIntegrityLevel	|	string	|	Integrity level of the newly created process. Windows assigns integrity levels to processes based on certain characteristics, such as if they were launched from an internet downloaded. These integrity levels influence permissions to resources.	|		|
|	process_token_elevation	|	ProcessTokenElevation	|	string	|	Token type indicating the presence or absence of User Access Control (UAC) privilege elevation applied to the newly created process	|		|
|	process_creation_time	|	ProcessCreationTime	|	date	|	Date and time the process was created	|		|
|	user_domain	|	AccountDomain	|	string	|	Domain of the account	|		|
|	user_name	|	AccountName	|	string	|	User name of the account	|		|
|	user_sid	|	AccountSid	|	string	|	Security Identifier (SID) of the account	|		|
|	user_logon_id	|	LogonId	|	string	|	Identifier for a logon session. This identifier is unique on the same machine only between restarts.	|		|
|	process_parent_user_domain	|	InitiatingProcessAccountDomain	|	string	|	Domain of the account that ran the process responsible for the event	|		|
|	process_parent_user_name	|	InitiatingProcessAccountName	|	string	|	User name of the account that ran the process responsible for the event	|		|
|	process_parent_user_sid	|	InitiatingProcessAccountSid	|	string	|	Security Identifier (SID) of the account that ran the process responsible for the event	|		|
|	process_parent_user_logon_id	|	InitiatingProcessLogonId	|	string	|	Identifier for a logon session of the process that initiated the event. This identifier is unique on the same machine only between restarts.	|		|
|	process_parent_integrity_level	|	InitiatingProcessIntegrityLevel	|	string	|	Integrity level of the process that initiated the event. Windows assigns integrity levels to processes based on certain characteristics, such as if they were launched from an internet download. These integrity levels influence permissions to resources.	|		|
|	process_parent_token_elevation	|	InitiatingProcessTokenElevation	|	string	|	Token type indicating the presence or absence of User Access Control (UAC) privilege elevation applied to the process that initiated the event	|		|
|	process_parent_sha1_hash	|	InitiatingProcessSHA1	|	string	|	SHA-1 of the process (image file) that initiated the event	|		|
|	process_parent_md5_hash	|	InitiatingProcessMD5	|	string	|	MD5 hash of the process (image file) that initiated the event	|		|
|	process_parent_file_name	|	InitiatingProcessFileName	|	string	|	Name of the process that initiated the event	|		|
|	process_parent_id	|	InitiatingProcessId	|	int	|	Process ID (PID) of the process that initiated the event	|		|
|	process_parent_command_line	|	InitiatingProcessCommandLine	|	string	|	Command line used to run the process that initiated the event	|		|
|	process_parent_creation_time	|	InitiatingProcessCreationTime	|	date	|	Date and time when the process that initiated the event was started	|		|
|	process_parent_path	|	InitiatingProcessFolderPath	|	string	|	Folder containing the process (image file) that initiated the event	|		|
|		|	InitiatingProcessParentId	|	int	|	Process ID (PID) of the parent process that spawned the process responsible for the event	|		|
|		|	InitiatingProcessParentFileName	|	string	|	Name of the parent process that spawned the process responsible for the event	|		|
|		|	InitiatingProcessParentCreationTime	|	date	|	Date and time when the parent of the process responsible for the event was started	|		|
|		|	ReportId	|	long	|	Event identifier based on a repeating counter. To identify unique events, this column must be used in conjunction with the ComputerName and EventTime columns.	|		|
|		|	AppGuardContainerId	|	string	|	Identifier for the virtualized container used by Application Guard to isolate browser activity	|		|
|	hash_sha256	|	SHA256	|	string	|	SHA-256 of the file that the recorded action was applied to. This field is usually not populated—use the SHA1 column when available.	|		|
|	process_parent_sha256_hash	|	InitiatingProcessSHA256	|	string	|	SHA-256 of the process (image file) that initiated the event. This field is usually not populated—use the SHA1 column when available.	|		|