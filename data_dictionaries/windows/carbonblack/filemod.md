# File Modification Table

## Description

A file on the filesystem has been created, deleted, or modified on an endpoint monitored by Carbon Black.

[Carbon Black Developer Docs](https://developer.carbonblack.com/reference/enterprise-response/event-forwarder/event-schema/#ingress-event-filemod-file-modification)

## Event Log Illustration & Event XML
```
{
    "action": "create",
    "actiontype": 1,
    "cb_server": "cbserver",
    "computer_name": "JASON-WIN81-VM",
    "event_type": "filemod",
    "filetype": 0,
    "filetype_name": "Unknown",
    "link_process": "https://cbtests/#analyze/00000001-0000-0c70-01d1-1e951aae7e2f/1",
    "link_sensor": "https://cbtests/#/host/1",
    "md5": "7A2870C2A8283B3630BF7670D0362B94",
    "path": "c:\\users\\admin\\appdata\\local\\google\\chrome\\user data\\b5e2.tmp",
    "pid": 3184,
    "process_guid": "00000001-0000-0c70-01d1-1e951aae7e2f",
    "sensor_id": 1,
    "timestamp": 1447696804,
    "type": "ingress.event.filemod"
}
```

## Data Dictionary

|	Standard Name	|	Field Name	|	Type	|	Description	|	Sample Value	|
|	-------------	|	----------	|	----	|	-----------	|	------------	|
|		|	action	|	TEXT	|	Type of file modification: create, write, delete, lastwrite	|	create	|
|		|	actiontype	|	INTEGER	|	Enum value of the file modification: 1=create, 2=write, 4=delete, 8=lastwrite	|	1	|
|		|	cb_server	|	TEXT	|	Used to distinguish between multiple Cb Response servers. Set this in the “server_name” option of cb-event-forwarder.ini.	|	cbserver	|
|		|	computer_name	|	TEXT	|	hostname of the sensor	|	JASON-WIN81-VM	|
|		|	event_type	|	TEXT	|	The type of event	|	filemod	|
|		|	filetype	|	INTEGER	|	Enum value of the detected file type of this file. Only valid for “lastwrite” actions. See the CbFileType protobuf definition for the available values.	|	0	|
|		|	filetype_name	|	TEXT	|		The detected file type of this file. Only valid for “lastwrite” actions. Currently supported file types: PE, ELF, UniversalBin, Eicar, OfficeLegacy, OfficeOpenXml, PDF, PKZIP, LZH, LZW, RAR, TAR, and 7zip.	|	Unknown	|
|		|	link_process	|	TEXT	|	Deep link to Cb Response UI for process	|	https://cbtests/#analyze/00000001-0000-0c70-01d1-1e951aae7e2f/1	|
|		|	link_sensor	|	TEXT	|	Deep link to Cb Response UI for sensor	|	https://cbtests/#/host/1	|
|		|	md5	|	TEXT	|	md5 of process executable	|	7A2870C2A8283B3630BF7670D0362B94	|
|		|	path	|	TEXT	|	Full file path	|	c:\\users\\admin\\appdata\\local\\google\\chrome\\user data\\b5e2.tmp	|
|		|	pid	|	INTEGER	|	Endpoint OS Process id of process	|	3184	|
|		|	process_guid	|	TEXT	|	Cb Process GUID of process	|	00000001-0000-0c70-01d1-1e951aae7e2f	|
|		|	sensor_id	|	INTEGER	|	sensor ID of associated sensor	|	1	|
|		|	timestamp	|	INTEGER	|	Endpoint timestamp of this event since epoch	|	1447696804	|
|		|	type	|	TEXT	|		The full type of event	|	ingress.event.filemod	|