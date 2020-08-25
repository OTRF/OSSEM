# Process_events Table
###### Version: 4.4.2

## Description
Track time/action process executions.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|pid|BIGINT|Process (or thread) ID|`TBD`|
|TBD|path|TEXT|Path of executed file|`TBD`|
|TBD|mode|TEXT|File mode permissions|`TBD`|
|TBD|cmdline|TEXT|Command line arguments (argv)|`TBD`|
|TBD|cmdline_size|BIGINT|Actual size (bytes) of command line arguments|`TBD`|
|TBD|env|TEXT|Environment variables delimited by spaces|`TBD`|
|TBD|env_count|BIGINT|Number of environment variables|`TBD`|
|TBD|env_size|BIGINT|Actual size (bytes) of environment list|`TBD`|
|TBD|cwd|TEXT|The process current working directory|`TBD`|
|TBD|auid|BIGINT|Audit User ID at process start|`TBD`|
|TBD|uid|BIGINT|User ID at process start|`TBD`|
|TBD|euid|BIGINT|Effective user ID at process start|`TBD`|
|TBD|gid|BIGINT|Group ID at process start|`TBD`|
|TBD|egid|BIGINT|Effective group ID at process start|`TBD`|
|TBD|owner_uid|BIGINT|File owner user ID|`TBD`|
|TBD|owner_gid|BIGINT|File owner group ID|`TBD`|
|TBD|atime|BIGINT|File last access in UNIX time|`TBD`|
|TBD|mtime|BIGINT|File modification in UNIX time|`TBD`|
|TBD|ctime|BIGINT|File last metadata change in UNIX time|`TBD`|
|TBD|btime|BIGINT|File creation in UNIX time|`TBD`|
|TBD|overflows|TEXT|List of structures that overflowed|`TBD`|
|TBD|parent|BIGINT|Process parent's PID, or -1 if cannot be determined.|`TBD`|
|TBD|time|BIGINT|Time of execution in UNIX time|`TBD`|
|TBD|uptime|BIGINT|Time of execution in system uptime|`TBD`|
|TBD|eid|TEXT|Event ID|`TBD`|
|TBD|status|BIGINT|OpenBSM Attribute: Status of the process [DARWIN]|`TBD`|
|TBD|syscall|TEXT|Syscall name: fork, vfork, clone, execve, execveat [LINUX]|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#process_events)
