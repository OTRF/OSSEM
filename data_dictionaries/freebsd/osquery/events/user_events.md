# User_events Table

## Description
Track user events from the audit framework.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|uid|BIGINT|User ID|`TBD`|
|TBD|auid|BIGINT|Audit User ID|`TBD`|
|TBD|pid|BIGINT|Process (or thread) ID|`TBD`|
|TBD|message|TEXT|Message from the event|`TBD`|
|TBD|type|INTEGER|The file description for the process socket|`TBD`|
|TBD|path|TEXT|Supplied path from event|`TBD`|
|TBD|address|TEXT|The Internet protocol address or family ID|`TBD`|
|TBD|terminal|TEXT|The network protocol ID|`TBD`|
|TBD|time|BIGINT|Time of execution in UNIX time|`TBD`|
|TBD|uptime|BIGINT|Time of execution in system uptime|`TBD`|
|TBD|eid|TEXT|Event ID|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#user_events)

## Tags
* version_4.4.2