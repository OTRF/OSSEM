# Windows_crashes Table
###### Version: 4.4.2

## Description
Extracted information from Windows crash logs (Minidumps).

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|datetime|TEXT|Timestamp (log format) of the crash|`TBD`|
|TBD|module|TEXT|Path of the crashed module within the process|`TBD`|
|TBD|path|TEXT|Path of the executable file for the crashed process|`TBD`|
|TBD|pid|BIGINT|Process ID of the crashed process|`TBD`|
|TBD|tid|BIGINT|Thread ID of the crashed thread|`TBD`|
|TBD|version|TEXT|File version info of the crashed process|`TBD`|
|TBD|process_uptime|BIGINT|Uptime of the process in seconds|`TBD`|
|TBD|stack_trace|TEXT|Multiple stack frames from the stack trace|`TBD`|
|TBD|exception_code|TEXT|The Windows exception code|`TBD`|
|TBD|exception_message|TEXT|The NTSTATUS error message associated with the exception code|`TBD`|
|TBD|exception_address|TEXT|Address (in hex) where the exception occurred|`TBD`|
|TBD|registers|TEXT|The values of the system registers|`TBD`|
|TBD|command_line|TEXT|Command-line string passed to the crashed process|`TBD`|
|TBD|current_directory|TEXT|Current working directory of the crashed process|`TBD`|
|TBD|username|TEXT|Username of the user who ran the crashed process|`TBD`|
|TBD|machine_name|TEXT|Name of the machine where the crash happened|`TBD`|
|TBD|major_version|INTEGER|Windows major version of the machine|`TBD`|
|TBD|minor_version|INTEGER|Windows minor version of the machine|`TBD`|
|TBD|build_number|INTEGER|Windows build number of the crashing machine|`TBD`|
|TBD|type|TEXT|Type of crash log|`TBD`|
|TBD|crash_path|TEXT|Path of the log file|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#windows_crashes)
