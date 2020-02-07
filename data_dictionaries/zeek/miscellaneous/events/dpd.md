# DPD Log

## Description
Protocol/application detection failures

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|@timestamp|ts|TBD|date_time|Timestamp for when protocol analysis failed in epoch format|1300475167.096535|
|network_protocol|proto|TBD|string|Transport protocol for the violation|``|
|src_ip_addr|id.orig_h|TBD|ip|The originating/source IP address|10.1.1.1|
|src_port|id.orig_p|TBD|integer|The originating/source port|37682|
|dst_ip_addr|id.resp_h|TBD|ip|The responding/destination IP address|10.2.2.2|
|dst_port|id.resp_p|TBD|integer|The responding/destination port|80|
|event_uid|uid|TBD|string|Unique ID for the connection.|CHhAvVGS1DHFjwGM9|
|TBD|analyzer|TBD|string|The analyzer that generated the violation.|HTTP|
|TBD|failure_reason|TBD|string|The textual reason for the analysis failure.|not a http reply line|
|TBD|packet_segment|TBD|string|present if policy/frameworks/dpd/packet-segment-logging.bro is loaded A chunk of the payload that most likely resulted in the protocol violation.|``|
