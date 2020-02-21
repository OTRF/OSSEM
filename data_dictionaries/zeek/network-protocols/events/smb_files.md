# SMB Files Log

## Description
None

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|@timestamp|ts|date_time|Timestamp of the beginning of the event in epoch format|`1581064352.153314`|
|src_ip_addr|id.orig_h|ip|The originating/source IP address|`10.1.1.1`|
|src_port|id.orig_p|integer|The originating/source port|`49247`|
|dst_ip_addr|id.resp_h|ip|The responding/destination IP address|`10.2.2.2`|
|dst_port|id.resp_p|integer|The responding/destination port|`445`|
|event_uid|uid|string|Unique ID of the connection the file was sent over|`CVCEfC2Vej9sjr5ARe`|
|TBD|fuid|string|Unique ID of the file, if the file was extracted|````|
|file_accessed_time|times_accessed|date_time|The time, in epoch, attribute for when the file was last accessed|`1505160917.765625`|
|file_creation_time|times_created|date_time|The time attribute for when the file was created|`1505160917.765625`|
|file_changed_time|times_changed|date_time|The time attribute for when the file was last modified|`1505416680.062500`|
|file_modified_time|times_modified|date_time|The time attribute for when data was last written to the file|`1505416680.062500`|
|share_relative_target_name|name|string|The path/name relative to tree's path that was accessed|`adtest.local\\Policies\\{4132D0FE-8293-4D5A-BB3D-2164535CA3B2}\\ Machine\\Preferences\\ScheduledTasks\\ScheduledTasks.xml`|
|share_name|path|string|Path pulled from the tree this file was transferred to or from.|`\\dc001.adtest.local\SysVol`|
|file_size|size|integer|Total size of the file.|`5639`|
|TBD|action|string|Action this log record represents.|`SMB::FILE_OPEN`|
|file_previous_name|prev_name|string|If the rename action was seen, this will be the file's previous name.|`CX$\Johnbillingson\Payroll Documents\Pay\ROLL\Master Slides\Master Payroll Members.pptx`|
