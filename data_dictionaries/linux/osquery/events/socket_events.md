# Socket_events Table
###### Version: 4.4.2

## Description
Track network socket opens and closes.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|action|TEXT|The socket action (bind, listen, close)|`TBD`|
|TBD|pid|BIGINT|Process (or thread) ID|`TBD`|
|TBD|path|TEXT|Path of executed file|`TBD`|
|TBD|fd|TEXT|The file description for the process socket|`TBD`|
|TBD|auid|BIGINT|Audit User ID|`TBD`|
|TBD|success|INTEGER|The socket open attempt status|`TBD`|
|TBD|family|INTEGER|The Internet protocol family ID|`TBD`|
|TBD|protocol|INTEGER|The network protocol ID|`TBD`|
|TBD|local_address|TEXT|Local address associated with socket|`TBD`|
|TBD|remote_address|TEXT|Remote address associated with socket|`TBD`|
|TBD|local_port|INTEGER|Local network protocol port number|`TBD`|
|TBD|remote_port|INTEGER|Remote network protocol port number|`TBD`|
|TBD|socket|TEXT|The local path (UNIX domain socket only)|`TBD`|
|TBD|time|BIGINT|Time of execution in UNIX time|`TBD`|
|TBD|uptime|BIGINT|Time of execution in system uptime|`TBD`|
|TBD|eid|TEXT|Event ID|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#socket_events)
