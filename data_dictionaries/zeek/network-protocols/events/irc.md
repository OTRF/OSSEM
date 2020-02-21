# IRC Log

## Description
None

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|@timestamp|ts|date_time|Timestamp of the beginning of the event in epoch format|`1300475167.096535`|
|src_ip_addr|id.orig_h|ip|The originating/source IP address|`10.1.1.1`|
|src_port|id.orig_p|integer|The originating/source port|`37682`|
|dst_ip_addr|id.resp_h|ip|The responding/destination IP address|`10.2.2.2`|
|dst_port|id.resp_p|integer|The responding/destination port|`6660`|
|TBD|fuid|string|present if base/protocols/irc/files.bro is loaded File unique ID.|````|
|event_uid|uid|string|Unique ID for the connection.|`CHhAvVGS1DHFjwGM9`|
|TBD|addl|string|Any additional data for the command|````|
|TBD|dcc_file_name|string|present if base/protocols/irc/dcc-send.bro is loaded DCC filename requested.|````|
|TBD|dcc_file_size|integer|present if base/protocols/irc/dcc-send.bro is loaded Size of the DCC transfer as indicated by the sender.|````|
|TBD|dcc_mime_type|string|present if base/protocols/irc/dcc-send.bro is loaded Sniffed mime type of the file.|````|
|TBD|command|string|Command given by the client.|`USER`|
|TBD|nick|string|Nickname given for the connection.|`t9__Wkwc`|
|TBD|user|string|Username given for the connection|````|
|TBD|value|string|Value for the command given by the client|````|
