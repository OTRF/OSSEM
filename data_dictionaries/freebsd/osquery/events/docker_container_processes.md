# Docker_container_processes Table
###### Version: 4.4.2

## Description
Docker container processes.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|id|TEXT|Container ID|`TBD`|
|TBD|pid|BIGINT|Process ID|`TBD`|
|TBD|name|TEXT|The process path or shorthand argv[0]|`TBD`|
|TBD|cmdline|TEXT|Complete argv|`TBD`|
|TBD|state|TEXT|Process state|`TBD`|
|TBD|uid|BIGINT|User ID|`TBD`|
|TBD|gid|BIGINT|Group ID|`TBD`|
|TBD|euid|BIGINT|Effective user ID|`TBD`|
|TBD|egid|BIGINT|Effective group ID|`TBD`|
|TBD|suid|BIGINT|Saved user ID|`TBD`|
|TBD|sgid|BIGINT|Saved group ID|`TBD`|
|TBD|wired_size|BIGINT|Bytes of unpagable memory used by process|`TBD`|
|TBD|resident_size|BIGINT|Bytes of private memory used by process|`TBD`|
|TBD|total_size|BIGINT|Total virtual memory size|`TBD`|
|TBD|parent|BIGINT|Process parent's PID|`TBD`|
|TBD|pgroup|BIGINT|Process group|`TBD`|
|TBD|threads|INTEGER|Number of threads used by process|`TBD`|
|TBD|nice|INTEGER|Process nice level (-20 to 20, default 0)|`TBD`|
|TBD|user|TEXT|User name|`TBD`|
|TBD|time|TEXT|Cumulative CPU time. [DD-]HH:MM:SS format|`TBD`|
|TBD|cpu|DOUBLE|CPU utilization as percentage|`TBD`|
|TBD|mem|DOUBLE|Memory utilization as percentage|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#docker_container_processes)
