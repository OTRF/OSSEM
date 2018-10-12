# ingress.event.regmod (Registry Modification)

## Description

A registry key has been created, deleted, or modified on an endpoint monitored by Carbon Black.

[Carbon Black Developer Docs](https://developer.carbonblack.com/reference/enterprise-response/event-forwarder/event-schema/#ingress-event-regmod-registry-modification)

## Event Log Illustration & Event XML
```
{
    "action": "writeval",
    "actiontype": 2,
    "cb_server": "cbserver",
    "computer_name": "JASON-WIN81-VM",
    "event_type": "regmod",
    "link_process": "https://cbtests/#analyze/00000001-0000-0484-01d1-1e951b7c000b/1",
    "link_sensor": "https://cbtests/#/host/1",
    "md5": "0E7196981EDE614F1F54FFF2C3843ADF",
    "path": "\\registry\\user\\s-1-5-21-2709706146-4189370754-997381202-1001\\software\\microsoft\\vscommon\\12.0\\sqm\\pids\\1156\\stillalive",
    "pid": 1156,
    "process_guid": "00000001-0000-0484-01d1-1e951b7c000b",
    "sensor_id": 1,
    "timestamp": 1447696798,
    "type": "ingress.event.regmod"
}
```

## Data Dictionary

|	Standard Name	|	Field Name	|	Type	|	Description	|	Sample Value	|
|	-------------	|	----------	|	----	|	-----------	|	------------	|
|		|	action	|	TEXT	|	Type of registry modification. This can be one of: createkey, writeval, delkey, or delval	|	writeval	|
|		|	actiontype	|	INTEGER	|	Enum value of the registry modification: 1=createkey, 2=writeval, 4=delkey, 8=delval	|	2	|
|		|	cb_server	|	TEXT	|	Used to distinguish between multiple Cb Response servers. Set this in the “server_name” option of cb-event-forwarder.ini.	|	cbserver	|
|		|	computer_name	|	TEXT	|	hostname of the sensor	|	JASON-WIN81-VM	|
|		|	event_type	|	TEXT	|	The type of event	|	regmod	|
|		|	link_process	|	TEXT	|	Deep link to Cb Response UI for process	|	https://cbtests/#analyze/00000001-0000-0484-01d1-1e951b7c000b/1	|
|		|	link_sensor	|	TEXT	|	Deep link to Cb Response UI for sensor	|	https://cbtests/#/host/1	|
|		|	md5	|	TEXT	|	md5 of process executable	|	0E7196981EDE614F1F54FFF2C3843ADF	|
|		|	path	|	TEXT	|	Full registry path	|	\\registry\\user\\s-1-5-21-2709706146-4189370754-997381202-1001\\software\\microsoft\\vscommon\\12.0\\sqm\\pids\\1156\\stillalive	|
|		|	pid	|	INTEGER	|	Endpoint OS Process id of process	|	1156	|
|		|	process_guid	|	TEXT	|	Cb Process GUID of process	|	00000001-0000-0484-01d1-1e951b7c000b	|
|		|	sensor_id	|	INTEGER	|	Sensor ID of associated sensor	|	1	|
|		|	timestamp	|	BIGINT	|	Endpoint timestamp of this event since epoch	| 1447696798 |
|		|	type	|	TEXT	|	The full type of event	| ingress.event.regmod |