# DCE-RPC Log

## Description
None

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|@timestamp|ts|TBD|date_time|Timestamp of the beginning of the event in epoch format|1300475167.096535|
|src_ip_addr|id.orig_h|TBD|ip|The originating/source IP address|10.1.1.1|
|src_port|id.orig_p|TBD|integer|The originating/source port|37682|
|dst_ip_addr|id.resp_h|TBD|ip|The responding/destination IP address|10.2.2.2|
|dst_port|id.resp_p|TBD|integer|The responding/destination port|135|
|event_uid|uid|TBD|string|Unique ID for the connection.|CHhAvVGS1DHFjwGM9|
|TBD|endpoint|TBD|string|Endpoint name looked up from the uuid.|exchange_mapi|
|TBD|named_pipe|TBD|string|Remote pipe name.|\\pipe\spoolss|
|TBD|operation|TBD|string|Operation seen in the call.|BaseRegEnumValue|
|event_duration|rtt|TBD|float|Round trip time from the request to the response. If either the request or response was not seen, this will be null.|0.025|
