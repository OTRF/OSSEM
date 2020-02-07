# MySQL Log

## Description
None

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|@timestamp|ts|TBD|date_time|Timestamp of the beginning of the event in epoch format|1300475167.096535|
|src_ip_addr|id.orig_h|TBD|ip|The originating/source IP address|192.168.0.254|
|src_port|id.orig_p|TBD|integer|The originating/source port|37682|
|dst_ip_addr|id.resp_h|TBD|ip|The responding/destination IP address|192.168.0.254|
|dst_port|id.resp_p|TBD|integer|The responding/destination port|3306|
|event_uid|uid|TBD|string|Unique ID for the connection.|CzwW5j3qyZtuKCIt0f|
|TBD|arg|TBD|string|The argument issued to the command.|insert into foo (animal, name) values (\"cat\", \"Garfield\")|
|TBD|cmd|TBD|string|The command that was issued.|query|
|TBD|response|TBD|string|Server message, if any.|CHhAvVGS1DHFjwGM9|
|TBD|rows|TBD|integer|The number of affected rows, if any.|1|
|TBD|uid|TBD|boolean|Did the server tell us that the command succeeded.|true|
