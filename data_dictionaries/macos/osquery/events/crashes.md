# Crashes Table
###### Version: 4.4.2

## Description
Application, System, and Mobile App crash logs.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|type|TEXT|Type of crash log|`TBD`|
|TBD|pid|BIGINT|Process (or thread) ID of the crashed process|`TBD`|
|TBD|path|TEXT|Path to the crashed process|`TBD`|
|TBD|crash_path|TEXT|Location of log file|`TBD`|
|TBD|identifier|TEXT|Identifier of the crashed process|`TBD`|
|TBD|version|TEXT|Version info of the crashed process|`TBD`|
|TBD|parent|BIGINT|Parent PID of the crashed process|`TBD`|
|TBD|responsible|TEXT|Process responsible for the crashed process|`TBD`|
|TBD|uid|INTEGER|User ID of the crashed process|`TBD`|
|TBD|datetime|TEXT|Date/Time at which the crash occurred|`TBD`|
|TBD|crashed_thread|BIGINT|Thread ID which crashed|`TBD`|
|TBD|stack_trace|TEXT|Most recent frame from the stack trace|`TBD`|
|TBD|exception_type|TEXT|Exception type of the crash|`TBD`|
|TBD|exception_codes|TEXT|Exception codes from the crash|`TBD`|
|TBD|exception_notes|TEXT|Exception notes from the crash|`TBD`|
|TBD|registers|TEXT|The value of the system registers|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#crashes)
