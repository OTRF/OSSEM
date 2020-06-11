# Process_file_events Table

## Description
A File Integrity Monitor implementation using the audit service.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|operation|TEXT|Operation type|`TBD`|
|TBD|pid|BIGINT|Process ID|`TBD`|
|TBD|ppid|BIGINT|Parent process ID|`TBD`|
|TBD|time|BIGINT|Time of execution in UNIX time|`TBD`|
|TBD|executable|TEXT|The executable path|`TBD`|
|TBD|partial|TEXT|True if this is a partial event (i.e.: this process existed before we started osquery)|`TBD`|
|TBD|cwd|TEXT|The current working directory of the process|`TBD`|
|TBD|path|TEXT|The path associated with the event|`TBD`|
|TBD|dest_path|TEXT|The canonical path associated with the event|`TBD`|
|TBD|uid|TEXT|The uid of the process performing the action|`TBD`|
|TBD|gid|TEXT|The gid of the process performing the action|`TBD`|
|TBD|euid|TEXT|Effective user ID of the process using the file|`TBD`|
|TBD|egid|TEXT|Effective group ID of the process using the file|`TBD`|
|TBD|uptime|BIGINT|Time of execution in system uptime|`TBD`|
|TBD|eid|TEXT|Event ID|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#process_file_events)

## Tags
* version_4.4.2