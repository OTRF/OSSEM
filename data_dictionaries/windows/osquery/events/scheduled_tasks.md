# Scheduled_tasks Table

## Description
Lists all of the tasks in the Windows task scheduler.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|name|TEXT|Name of the scheduled task|`TBD`|
|TBD|action|TEXT|Actions executed by the scheduled task|`TBD`|
|TBD|path|TEXT|Path to the executable to be run|`TBD`|
|TBD|enabled|INTEGER|Whether or not the scheduled task is enabled|`TBD`|
|TBD|state|TEXT|State of the scheduled task|`TBD`|
|TBD|hidden|INTEGER|Whether or not the task is visible in the UI|`TBD`|
|TBD|last_run_time|INTEGER|Timestamp the task last ran|`TBD`|
|TBD|next_run_time|INTEGER|Timestamp the task is scheduled to run next|`TBD`|
|TBD|last_run_message|TEXT|Exit status message of the last task run|`TBD`|
|TBD|last_run_code|TEXT|Exit status code of the last task run|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#scheduled_tasks)

## Tags
* version_4.4.2