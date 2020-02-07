# ingress.event.processblock (Process Block)

## Description
A process was blocked from executing on an endpoint monitored by Carbon Black because the process MD5 has been blacklisted.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|blocked_event|blocked_event|TBD|TEXT|The type of event that was blocked: either ProcessCreate (the process was terminated immediately upon execution) or RunningProcess (the process was already running on the endpoint when the block was applied).|ProcessCreate|
|blocked_reason|blocked_reason|TBD|TEXT|The reason for block action (Md5Hash is the only possible value)|Md5Hash|
|blocked_result|blocked_result|TBD|TEXT|The result of the blocked action: ProcessTerminated, NotTerminatedCBProcess, NotTerminatedSystemProcess, NotTerminatedCriticalSystemProcess, NotTerminatedWhitelistPath, NotTerminatedOpenProcessError, or NotTerminatedTerminateError.|ProcessTerminated|
|cb_server|cb_server|TBD|TEXT|Used to distinguish between multiple Cb Response servers. Set this in the "server_name" option of cb-event-forwarder.ini.|cbserver|
|process_command_line|command_line|TBD|TEXT|Command line associated with the blocked process|\"C:\Program Files\Microsoft Games\hearts\hearts.exe\"|
|host_name|computer_name|TBD|TEXT|hostname of the sensor|JASON-WIN81-VM|
|event_type|event_type|TBD|TEXT|The type of event|blocked_process|
|hash|md5|TBD|TEXT|md5 of process executable|A8524F6C3AFF774911BCA26AB8322602|
|file_path|path|TBD|TEXT|Path of the blocked executable on disk|c:\program files\microsoft games\hearts\hearts.exe|
|sensor_id|sensor_id|TBD|INTEGER|Sensor ID of associated sensor|1|
|event_date_creation|timestamp|TBD|BIGINT|Endpoint timestamp of this event since epoch|1450470603|
|event_type_detailed|type|TBD|TEXT|The full type of event|ingress.event.processblock|
|user_sid|uid|TBD|TEXT|Security Identifier of the username name used for process creation|S-1-5-21-3382350439-2970772701-2583938045-1000|
|user_name|username|TBD|TEXT|Username that initiated the process creation|DANWIN764\dan|

## Resources
* [Carbon Black Developer Docs](https://developer.carbonblack.com/reference/enterprise-response/event-forwarder/event-schema/#ingress-event-processblock-process-block)
