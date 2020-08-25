# Processes Table
###### Version: 4.4.2

## Description
All running processes on the host system.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|pid|BIGINT|Process (or thread) ID|`TBD`|
|TBD|name|TEXT|The process path or shorthand argv[0]|`TBD`|
|TBD|path|TEXT|Path to executed binary|`TBD`|
|TBD|cmdline|TEXT|Complete argv|`TBD`|
|TBD|state|TEXT|Process state|`TBD`|
|TBD|cwd|TEXT|Process current working directory|`TBD`|
|TBD|root|TEXT|Process virtual root directory|`TBD`|
|TBD|uid|BIGINT|Unsigned user ID|`TBD`|
|TBD|gid|BIGINT|Unsigned group ID|`TBD`|
|TBD|euid|BIGINT|Unsigned effective user ID|`TBD`|
|TBD|egid|BIGINT|Unsigned effective group ID|`TBD`|
|TBD|suid|BIGINT|Unsigned saved user ID|`TBD`|
|TBD|sgid|BIGINT|Unsigned saved group ID|`TBD`|
|TBD|wired_size|BIGINT|Bytes of unpagable memory used by process|`TBD`|
|TBD|resident_size|BIGINT|Bytes of private memory used by process|`TBD`|
|TBD|total_size|BIGINT|Total virtual memory size|`TBD`|
|TBD|user_time|BIGINT|CPU time in milliseconds spent in user space|`TBD`|
|TBD|system_time|BIGINT|CPU time in milliseconds spent in kernel space|`TBD`|
|TBD|disk_bytes_read|BIGINT|Bytes read from disk|`TBD`|
|TBD|disk_bytes_written|BIGINT|Bytes written to disk|`TBD`|
|TBD|start_time|BIGINT|Process start time in seconds since Epoch, in case of error -1|`TBD`|
|TBD|parent|BIGINT|Process parent's PID|`TBD`|
|TBD|pgroup|BIGINT|Process group|`TBD`|
|TBD|threads|INTEGER|Number of threads used by process|`TBD`|
|TBD|nice|INTEGER|Process nice level (-20 to 20, default 0)|`TBD`|
|TBD|is_elevated_token|INTEGER|Process uses elevated token yes=1, no=0 [WINDOWS]|`TBD`|
|TBD|elapsed_time|BIGINT|Elapsed time in seconds this process has been running. [WINDOWS]|`TBD`|
|TBD|handle_count|BIGINT|Total number of handles that the process has open. This number is the sum of the handles currently opened by each thread in the process. [WINDOWS]|`TBD`|
|TBD|percent_processor_time|BIGINT|Returns elapsed time that all of the threads of this process used the processor to execute instructions in 100 nanoseconds ticks. [WINDOWS]|`TBD`|
|TBD|upid|BIGINT|A 64bit pid that is never reused. Returns -1 if we couldn't gather them from the system. [DARWIN]|`TBD`|
|TBD|uppid|BIGINT|The 64bit parent pid that is never reused. Returns -1 if we couldn't gather them from the system. [DARWIN]|`TBD`|
|TBD|cpu_type|INTEGER|A 64bit pid that is never reused. Returns -1 if we couldn't gather them from the system. [DARWIN]|`TBD`|
|TBD|cpu_subtype|INTEGER|The 64bit parent pid that is never reused. Returns -1 if we couldn't gather them from the system. [DARWIN]|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#processes)
