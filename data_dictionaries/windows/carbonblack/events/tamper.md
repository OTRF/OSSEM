# ingress.event.tamper (Cb Response Tamper)

## Description
A process tampered with a critical Carbon Black userspace process or kernel driver.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|cb_server|cb_server|TBD|TEXT|Used to distinguish between multiple Cb Response servers. Set this in the "server_name" option of cb-event-forwarder.ini.|cbserver|
|host_name|computer_name|TBD|TEXT|hostname of the sensor|JASON-WIN81-VM|
|event_type|event_type|TBD|TEXT|The type of event|tamper|
|sensor_id|sensor_id|TBD|INTEGER|Sensor ID of associated sensor|1|
|tamper_type|tamper_type|TBD|TEXT|The activity which triggered this tamper event: CoreDriverUnloaded, NetworkDriverUnloaded, CbServiceStopped, CbProcessTerminated, or CbCodeInjection|CbProcessTerminated|
|event_date_creation|timestamp|TBD|INTEGER|Endpoint timestamp of this event since epoch|1450470603|
|event_type_detailed|type|TBD|TEXT|The full type of event|ingress.event.tamper|

## Resources
* [Carbon Black Developer Docs](https://developer.carbonblack.com/reference/enterprise-response/event-forwarder/event-schema/#ingress-event-tamper-cb-response-tamper)
