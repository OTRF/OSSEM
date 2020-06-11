# ingress.event.tamper (Cb Response Tamper)

## Description

A process tampered with a critical Carbon Black userspace process or kernel driver.

[Carbon Black Developer Docs](https://developer.carbonblack.com/reference/enterprise-response/event-forwarder/event-schema/#ingress-event-tamper-cb-response-tamper)

## Event Log Illustration & Event XML
```
{
    "cb_server": "cbserver",
    "computer_name": "JASON-WIN81-VM",
    "event_type": "tamper",
    "sensor_id": 1,
    "tamper_type": "CbProcessTerminated",
    "timestamp": 1450470455,
    "type": "ingress.event.tamper"
}
```

## Data Dictionary

|	Standard Name	|	Field Name	|	Type	|	Description	|	Sample Value	|
|	-------------	|	----------	|	----	|	-----------	|	------------	|
|	cb_server	|	cb_server	|	TEXT	|	Used to distinguish between multiple Cb Response servers. Set this in the “server_name” option of cb-event-forwarder.ini.	|	cbserver	|
|	host_name	|	computer_name	|	TEXT	|	hostname of the sensor	|	JASON-WIN81-VM	|
|	event_type	|	event_type	|	TEXT	|	The type of event	|	tamper	|
|	sensor_id	|	sensor_id	|	INTEGER	|	Sensor ID of associated sensor	|	1	|
|	tamper_type	|	tamper_type	|	TEXT	|	The activity which triggered this tamper event: CoreDriverUnloaded, NetworkDriverUnloaded, CbServiceStopped, CbProcessTerminated, or CbCodeInjection	| CbProcessTerminated |
|	@timestamp	|	timestamp	|	INTEGER	|	Endpoint timestamp of this event since epoch	| 1450470603 |
|	event_type_detailed	|	type	|	TEXT	|	The full type of event	| ingress.event.tamper |
