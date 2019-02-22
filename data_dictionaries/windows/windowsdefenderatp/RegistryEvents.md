---
title: RegistryEvents
description: Creation and modification of registry entries.
log.type: Windows Defender ATP
author: Jared Atkinson (@jaredcatkinson)
date: 02/21/2019
---

# RegistryEvents

## Description
Creation and modification of registry entries

## Event Log Illustration & Event XML

## Data Dictionary
|	Standard Name	|	Field Name	|	Type	|	Description	|	Sample Value	|
|	-------------	|	----------	|	----	|	-----------	|	------------	|
|	event_date_creation	|	EventTime	|	date	|	Date and time when the event was recorded	|		|
|		|	MachineId	|	string	|	Unique identifier for the machine in the service	|		|
|		|	ComputerName	|	string	|	Fully qualified domain name (FQDN) of the machine	|		|
|		|	ActionType	|	string	|	Type of activity that triggered the event	|		|
|	registry_key_path	|	RegistryKey	|	string	|	Registry key that the recorded action was applied to	|		|
|		|	RegistryValueType	|	string	|	Data type, such as binary or string, of the registry value that the recorded action was applied to	|		|
|		|	RegistryValueName	|	string	|	Name of the registry value that the recorded action was applied to	|		|
|		|	RegistryValueData	|	string	|		Data of the registry value that the recorded action was applied to	|		|
|		|	PreviousRegistryValueName	|	string	|	Original name of the registry value before it was modified	|		|
|		|	PreviousRegistryValueData	|	string	|	Original data of the registry value before it was modified	|		|
|	user_domain	|	InitiatingProcessAccountDomain	|	string	|	Domain of the account that ran the process responsible for the event	|		|
|	user_name	|	InitiatingProcessAccountName	|	string	|	User name of the account that ran the process responsible for the event	|		|
|	user_sid	|	InitiatingProcessAccountSid	|	string	|	Security Identifier (SID) of the account that ran the process responsible for the event	|		|
|	hash_sha1	|	InitiatingProcessSHA1	|	string	|	SHA-1 of the process (image file) that initiated the event	|		|
|	hash_md5	|	InitiatingProcessMD5	|	string	|	MD5 hash of the process (image file) that initiated the event	|		|
|	process_name	|	InitiatingProcessFileName	|	string	|	Name of the process that initiated the event	|		|
|	process_id	|	InitiatingProcessId	|	int	|	Process ID (PID) of the process that initiated the event	|		|
|	process_command_line	|	InitiatingProcessCommandLine	|	string	|	Command line used to run the process that initiated the event	|		|
|	process_creation_time	|	InitiatingProcessCreationTime	|	date	|	Date and time when the process that initiated the event was started	|		|
|	process_path	|	InitiatingProcessFolderPath	|	string	|	Folder containing the process (image file) that initiated the event	|		|
|	process_parent_id	|	InitiatingProcessParentId	|	int	|	Process ID (PID) of the parent process that spawned the process responsible for the event	|		|
|	process_parent_name	|	InitiatingProcessParentFileName	|	string	|	Name of the parent process that spawned the process responsible for the event	|		|
|	process_parent_creation_time	|	InitiatingProcessParentCreationTime	|	date	|	Date and time when the parent of the process responsible for the event was started	|		|
|	process_integrity_level	|	InitiatingProcessIntegrityLevel	|	string	|	Integrity level of the process that initiated the event. Windows assigns integrity levels to processes based on certain characteristics, such as if they were launched from an internet download. These integrity levels influence permissions to resources.	|		|
|	process_token_elevation	|	InitiatingProcessTokenElevation	|	string	|	Token type indicating the presence or absence of User Access Control (UAC) privilege elevation applied to the process that initiated the event	|		|
|		|	ReportId	|	long	|	Event identifier based on a repeating counter. To identify unique events, this column must be used in conjunction with the ComputerName and EventTime columns.	|		|
|		|	AppGuardContainerId	|	string	|	Identifier for the virtualized container used by Application Guard to isolate browser activity	|		|