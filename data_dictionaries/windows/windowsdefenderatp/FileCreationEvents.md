---
title: FileCreationEvents
description: File creation, modification, and other file system events.
log.type: Windows Defender ATP
author: Jared Atkinson (@jaredcatkinson)
date: 02/21/2019
---

# FileCreationEvents

## Description
File creation, modification, and other file system events

## Event Log Illustration & Event XML

## Data Dictionary
|	Standard Name	|	Field Name	|	Type	|	Description	|	Sample Value	|
|	-------------	|	----------	|	----	|	-----------	|	------------	|
|	@timestamp	|	EventTime	|	date	|	Date and time when the event was recorded	|		|
|	machine_id	|	MachineId	|	string	|	Unique identifier for the machine in the service	|		|
|	computer_name	|	ComputerName	|	string	|	Fully qualified domain name (FQDN) of the machine	|		|
|	action_type	|	ActionType	|	string	|	Type of activity that triggered the event	|		|
|	file_name	|	FileName	|	string	|	Name of the file that the recorded action was applied to	|		|
|	file_path	|	FolderPath	|	string	|	Folder containing the file that the recorded action was applied to	|		|
|	hash_sha1	|	SHA1	|	string	|	SHA-1 of the file that the recorded action was applied to	|		|
|	hash_sha256	|	SHA256	|	string	|	SHA-256 of the file that the recorded action was applied to. This field is usually not populated—use the SHA1 column when available.	|		|
|	hash_md5	|	MD5	|	string	|	MD5 hash of the file that the recorded action was applied to	|		|
|	file_origin_url	|	FileOriginUrl	|	string	|	URL where the file was downloaded from	|		|
|	file_origin_reference_url	|	FileOriginReferenceUrl	|	string	|	URL of the web page that links to the downloaded file	|		|
|	file_origin_ip	|	FileOriginIP	|	string	|	IP address where the file was downloaded from	|		|
|	user_domain	|	InitiatingProcessAccountDomain	|	string	|	Domain of the account that ran the process responsible for the event	|		|
|	user_name	|	InitiatingProcessAccountName	|	string	|	User name of the account that ran the process responsible for the event	|		|
|	user_sid	|	InitiatingProcessAccountSid	|	string	|	Security Identifier (SID) of the account that ran the process responsible for the event	|		|
|	md5_hash	|	InitiatingProcessMD5	|	string	|	MD5 hash of the process (image file) that initiated the event	|		|
|	sha1_hash	|	InitiatingProcessSHA1	|	string	|	SHA-1 of the process (image file) that initiated the event	|		|
|	process_path	|	InitiatingProcessFolderPath	|	string	|	Folder containing the process (image file) that initiated the event	|		|
|	process_name	|	InitiatingProcessFileName	|	string	|	Name of the process that initiated the event	|		|
|	process_id	|	InitiatingProcessId	|	int	|	Process ID (PID) of the process that initiated the event	|		|
|	process_command_line	|	InitiatingProcessCommandLine	|	string	|	Command line used to run the process that initiated the event	|		|
|	process_creation_time	|	InitiatingProcessCreationTime	|	date	|	Date and time when the process that initiated the event was started	|		|
|	process_integrity_level	|	InitiatingProcessIntegrityLevel	|	string	|	Integrity level of the process that initiated the event. Windows assigns integrity levels to processes based on certain characteristics, such as if they were launched from an internet download. These integrity levels influence permissions to resources.	|		|
|	process_token_elevation	|	InitiatingProcessTokenElevation	|	string	|	Token type indicating the presence or absence of User Access Control (UAC) privilege elevation applied to the process that initiated the event	|		|
|	process_parent_id	|	InitiatingProcessParentId	|	int	|	Process ID (PID) of the parent process that spawned the process responsible for the event	|		|
|	process_parent_name	|	InitiatingProcessParentFileName	|	string	|	Name of the parent process that spawned the process responsible for the event	|		|
|	process_parent_creation_time	|	InitiatingProcessParentCreationTime	|	date	|	Date and time when the parent of the process responsible for the event was started	|		|
|	report_id	|	ReportId	|	long	|	Event identifier based on a repeating counter. To identify unique events, this column must be used in conjunction with the ComputerName and EventTime columns.	|		|
|	app_guard_container_id	|	AppGuardContainerId	|	string	|	Identifier for the virtualized container used by Application Guard to isolate browser activity	|		|
|	sensitivity_label	|	SensitivityLabel	|		|		|		|
|	sensitivity_sublabel	|	SensitivitySubLabel	|		|		|		|
|	is_windows_infor_protection_applied	|	IsWindowsInfoProtectionApplied	|		|		|		|
|	is_azure_info_protection_applied	|	IsAzureInfoProtectionApplied	|		|		|		|
