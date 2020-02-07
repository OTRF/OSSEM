# SMB Mapping Log

## Description
None

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|@timestamp|ts|TBD|date_time|Timestamp of the beginning of the event in epoch format|1300475167.096535|
|src_ip_addr|id.orig_h|TBD|ip|The originating/source IP address|10.1.1.1|
|src_port|id.orig_p|TBD|integer|The originating/source port|37682|
|dst_ip_addr|id.resp_h|TBD|ip|The responding/destination IP address|10.2.2.2|
|dst_port|id.resp_p|TBD|integer|The responding/destination port|445|
|event_uid|uid|TBD|string|Unique ID of the connection the tree was mapped over|``|
|TBD|native_file_system|TBD|string|File system of the tree.|NTFS|
|TBD|path|TBD|string|Name of the tree path.|\\SOMENAME\$IPC|
|TBD|share_type|TBD|string|If this is SMB2, a share type will be included. For SMB1, the type of share will be deduced and included as well.|PRINT|
|TBD|service|TBD|string|The type of resource of the tree (disk share, printer share, named pipe, etc.).|C:|
