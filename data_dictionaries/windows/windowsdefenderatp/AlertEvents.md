---
title: AlertEvents
description: Alerts on Windows Defender Security Center.
log.type: Windows Defender ATP
author: Jared Atkinson (@jaredcatkinson)
date: 02/21/2019
---


|	Standard Name	|	Field Name	|	Type	|	Description	|	Sample Value	|
|	-------------	|	----------	|	----	|	-----------	|	------------	|
|		|	AlertId	|	string	|	Unique identifier for the alert	|		|
|	event_date_creation	|	EventTime	|	date	|	Date and time when the event was recorded	|		|
|		|	MachineId	|	string	|	Unique identifier for the machine in the service	|		|
|		|	ComputerName	|	string	|	Fully qualified domain name (FQDN) of the machine	|		|
|		|	Severity	|		|		|		|
|		|	Category	|		|		|		|
|		|	Title	|		|		|		|
|		|	FileName	|	string	|	Name of the file that the recorded action was applied to	|		|
|	hash_sha1	|	SHA1	|	string	|ß	SHA-1 of the file that the recorded action was applied to	|		|
|		|	RemoteUrl	|	string	|	URL or fully qualified domain name (FQDN) that was being connected to	|		|
|		|	RemoteIP	|	string	|	IP address that was being connected to	|		|
|		|	ReportId	|	long	|	Event identifier based on a repeating counter. To identify unique events, this column must be used in conjunction with the ComputerName and EventTime columns.	|		|
|		|	Table	|	string	|	Table that contains the details of the event	|		|