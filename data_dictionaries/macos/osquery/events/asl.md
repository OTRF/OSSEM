# Asl Table
###### Version: 4.4.2

## Description
Queries the Apple System Log data structure for system events.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|time|INTEGER|Unix timestamp.  Set automatically|`TBD`|
|TBD|time_nano_sec|INTEGER|Nanosecond time.|`TBD`|
|TBD|host|TEXT|Sender's address (set by the server).|`TBD`|
|TBD|sender|TEXT|Sender's identification string.  Default is process name.|`TBD`|
|TBD|facility|TEXT|Sender's facility.  Default is 'user'.|`TBD`|
|TBD|pid|INTEGER|Sending process ID encoded as a string.  Set automatically.|`TBD`|
|TBD|gid|BIGINT|GID that sent the log message (set by the server).|`TBD`|
|TBD|uid|BIGINT|UID that sent the log message (set by the server).|`TBD`|
|TBD|level|INTEGER|Log level number.  See levels in asl.h.|`TBD`|
|TBD|message|TEXT|Message text.|`TBD`|
|TBD|ref_pid|INTEGER|Reference PID for messages proxied by launchd|`TBD`|
|TBD|ref_proc|TEXT|Reference process for messages proxied by launchd|`TBD`|
|TBD|extra|TEXT|Extra columns, in JSON format. Queries against this column are performed entirely in SQLite, so do not benefit from efficient querying via asl.h.|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#asl)
