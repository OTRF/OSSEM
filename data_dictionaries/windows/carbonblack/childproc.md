# ingress.event.childproc (Child Process)

## Description

A process has spawned another process on an endpoint monitored by Carbon Black.

[Carbon Black Developer Docs](https://developer.carbonblack.com/reference/enterprise-response/event-forwarder/event-schema/#ingress-event-childproc-child-process)

## Event Log Illustration & Event XML
```
{
    "cb_server": "cbserver",
    "child_process_guid": "00000001-0000-07b4-01d1-209a100bc217",
    "computer_name": "JASON-WIN81-VM",
    "created": true,
    "event_type": "childproc",
    "link_child": "https://cbtests/#analyze/00000001-0000-07b4-01d1-209a100bc217/1",
    "link_process": "https://cbtests/#analyze/00000001-0000-0af4-01d1-1e444bf4c3dd/1",
    "link_sensor": "https://cbtests/#/host/1",
    "md5": "D6021013D7C4E248AEB8BED12D3DCC88",
    "pid": 2804,
    "process_guid": "00000001-0000-0af4-01d1-1e444bf4c3dd",
    "sensor_id": 1,
    "timestamp": 1447697423,
    "type": "ingress.event.childproc"
}
```

## Data Dictionary

|	Standard Name	|	Field Name	|	Type	|	Description	|	Sample Value	|
|	-------------	|	----------	|	----	|	-----------	|	------------	|
|		|	cb_server	|	TEXT	|	Used to distinguish between multiple Cb Response servers. Set this in the “server_name” option of cb-event-forwarder.ini.	|	cbserver	|
|		|	child_process_guid	|	TEXT	|	process guid of the child process	|	00000001-0000-07b4-01d1-209a100bc217	|
|		|	computer_name	|	TEXT	|	hostname of the sensor	|	JASON-WIN81-VM	|
|		|	created	|	BOOLEAN	|	Specifies whether this process_guid is the child or the parent	|	true	|
|		|	event_type	|	TEXT	|	The type of event	|	childproc	|
|		|	link_child	|	TEXT	|	Deep link to Cb Response UI for child process	|	https://cbtests/#analyze/00000001-0000-07b4-01d1-209a100bc217/1	|
|		|	link_process	|	TEXT	|	Deep link to Cb Response UI for parent process	|	https://cbtests/#analyze/00000001-0000-0af4-01d1-1e444bf4c3dd/1	|
|		|	link_sensor	|	TEXT	|	Deep link to Cb Response UI for sensor	|	https://cbtests/#/host/1	|
|		|	md5	|	TEXT	|	md5 of the module	|	D6021013D7C4E248AEB8BED12D3DCC88	|
|		|	pid	|	INTEGER	|	Endpoint OS Process id of process	|	2804	|
|		|	process_guid	|	TEXT	|	Cb Process GUID of parent process	|	00000001-0000-0af4-01d1-1e444bf4c3dd	|
|		|	sensor_id	|	INTEGER	|	sensor ID of associated sensor	|	1	|
|		|	timestamp	|	INTEGER	|	Endpoint timestamp of this event since epoch	|	1447697423	|
|		|	type	|	TEXT	|		The full type of event	|	ingress.event.childproc	|