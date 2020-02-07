# ingress.event.crossprocopen (Cross Process Open)

## Description
A process has attempted to open a handle into another process OR if a remote thread was created.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|cb_server|cb_server|TBD|TEXT|Used to distinguish between multiple Cb Response servers. Set this in the "server_name" option of cb-event-forwarder.ini.|cbserver|
|host_name|computer_name|TBD|TEXT|hostname of the sensor|JASON-WIN81-VM|
|cross_process_type|cross_process_type|TBD|TEXT|The type of cross process event: either open_process (opening a handle to another process) or open_thread|open_process|
|event_type|event_type|TBD|TEXT|type of event|cross_process|
|is_target|is_target|TBD|BOOLEAN|specifies whether process_guid is the target of the cross process event|false|
|target_process_link|link_target|TBD|TEXT|Deep link to Cb Response UI for target process|https://cbtests/#analyze/00000007-0000-02c4-01d1-20982cef85d3/1|
|process_link|link_process|TBD|TEXT|Deep link to Cb Response UI for this process|https://cbtests/#analyze/00000007-0000-0ccc-01d1-209ab5339f45/1|
|sensor_link|link_sensor|TBD|TEXT|Deep link to Cb Response UI for sensor|https://cbtests/#/host/7|
|hash|md5|TBD|TEXT|md5 of process_guid executable image|053EEEE1ABAE53F044F1E386E22AE525|
|process_id|pid|TBD|INTEGER|Endpoint OS Process id of process that generated the crossprocopen event|3276|
|process_guid|process_guid|TBD|TEXT|Process guid of child process|00000007-0000-0ccc-01d1-209ab5339f45|
|process_granted_access|requested_access|TBD|INTEGER|Windows bitfield representing the requested access for this process or thread handle (decimal)|5136|
|sensor_id|sensor_id|TBD|INTEGER|sensor ID of associated sensor|7|
|target_create_time|target_create_time|TBD|BIGINT|Target Process create time represented as a 64-bit Windows FILETIME|130921702131467731|
|target_process_hash|target_md5|TBD|TEXT|md5 of target process executable image|382100E75B6F4668AEAEF228C6CEFFAD|
|target_process_path|target_path|TBD|TEXT|Path of the target process' executable image|c:\windows\system32\lsass.exe|
|target_process_id|target_pid|TBD|INTEGER|Process ID of the target process|708|
|target_process_guid|target_process_guid|TBD|TEXT|process_guid of the target process|00000007-0000-02c4-01d1-20982cef85d3|
|event_date_creation|timestamp|TBD|INTEGER|Endpoint timestamp of this event since epoch|1447697702|
|event_type_detailed|type|TBD|TEXT|The full type of event|ingress.event.crossprocopen|

## Resources
* [Carbon Black Developer Docs](https://developer.carbonblack.com/reference/enterprise-response/event-forwarder/event-schema/#ingress-event-crossprocopen-cross-process-open)
