# ingress.event.regmod (Registry Modification)

## Description
A registry key has been created, deleted, or modified on an endpoint monitored by Carbon Black.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|action|action|TBD|TEXT|Type of registry modification. This can be one of: createkey, writeval, delkey, or delval|writeval|
|actiontype|actiontype|TBD|INTEGER|Enum value of the registry modification: 1=createkey, 2=writeval, 4=delkey, 8=delval|2|
|cb_server|cb_server|TBD|TEXT|Used to distinguish between multiple Cb Response servers. Set this in the "server_name" option of cb-event-forwarder.ini.|cbserver|
|host_name|computer_name|TBD|TEXT|hostname of the sensor|JASON-WIN81-VM|
|event_type|event_type|TBD|TEXT|The type of event|regmod|
|process_link|link_process|TBD|TEXT|Deep link to Cb Response UI for process|https://cbtests/#analyze/00000001-0000-0484-01d1-1e951b7c000b/1|
|sensor_link|link_sensor|TBD|TEXT|Deep link to Cb Response UI for sensor|https://cbtests/#/host/1|
|hash|md5|TBD|TEXT|md5 of process executable|0E7196981EDE614F1F54FFF2C3843ADF|
|process_path|path|TBD|TEXT|Full registry path|\registry\user\s-1-5-21-2709706146-4189370754-997381202-1001\software\microsoft\vscommon\12.0\sqm\pids\1156\stillalive|
|process_id|pid|TBD|INTEGER|Endpoint OS Process id of process|1156|
|process_guid|process_guid|TBD|TEXT|Cb Process GUID of process|00000001-0000-0484-01d1-1e951b7c000b|
|sensor_id|sensor_id|TBD|INTEGER|Sensor ID of associated sensor|1|
|event_date_creation|timestamp|TBD|BIGINT|Endpoint timestamp of this event since epoch|1447696798|
|event_type_detailed|type|TBD|TEXT|The full type of event|ingress.event.regmod|

## Resources
* [Carbon Black Developer Docs](https://developer.carbonblack.com/reference/enterprise-response/event-forwarder/event-schema/#ingress-event-regmod-registry-modification)
