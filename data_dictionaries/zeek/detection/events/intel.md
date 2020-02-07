# Intel Log

## Description
None

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|@timestamp|ts|TBD|date_time|Timestamp when the data was discovered in epoch format|1300475167.096535|
|src_ip_addr|id.orig_h|TBD|ip|The originating/source IP address|10.1.1.1|
|src_port|id.orig_p|TBD|integer|The originating/source port|37682|
|dst_ip_addr|id.resp_h|TBD|ip|The responding/destination IP address|10.2.2.2|
|dst_port|id.resp_p|TBD|integer|The responding/destination port|80|
|event_uid|uid|TBD|string|If a connection was associated with this intelligence hit, this is the uid for the connection|``|
|TBD|fuid|TBD|string|present if base/frameworks/intel/files.bro is loaded If a file was associated with this intelligence hit, this is the uid for the file.|``|
|TBD|file_mime_type|TBD|string|present if base/frameworks/intel/files.bro is loaded A mime type if the intelligence hit is related to a file. If the $f field is provided this will be automatically filled out.|``|
|TBD|file_desc|TBD|string|present if base/frameworks/intel/files.bro is loaded Frequently files can be "described" to give a bit more context. If the $f field is provided this field will be automatically filled out.|``|
|TBD|matched|TBD|string|Which indicator types matched|``|
|TBD|seen_|TBD|n/a|Where the data was seen|``|
|TBD|seen.|TBD|n/a|Where the data was seen|``|
|TBD|indicator|TBD|string|The string if the data is about a string|``|
|TBD|indicator_type|TBD|string|The type of data that the indicator represents|``|
|TBD|host|TBD|ip|If the indicator type was Intel::ADDR, then this field will be present|``|
|TBD|node|TBD|string|The name of the node where the match was discovered|``|
|TBD|where|TBD|string|Where the data was discovered|``|
|TBD|sources|TBD|array_string|Sources which supplied data that resulted in this match.|Conn::IN_RESP|
