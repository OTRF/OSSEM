# SNMP Log

## Description
None

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|@timestamp|ts|TBD|date_time|Timestamp of the beginning of the event in epoch format|1300475167.096535|
|src_ip_addr|id.orig_h|TBD|ip|The originating/source IP address|10.1.1.1|
|src_port|id.orig_p|TBD|integer|The originating/source port|37682|
|dst_ip_addr|id.resp_h|TBD|ip|The responding/destination IP address|10.2.2.2|
|dst_port|id.resp_p|TBD|integer|The responding/destination port|161|
|event_uid|uid|TBD|string|Unique ID for the connection.|CHhAvVGS1DHFjwGM9|
|TBD|duration|TBD|float|The amount of time between the first packet belonging to the SNMP session and the latest one seen|0.038019|
|TBD|community|TBD|string|The community string of the first SNMP packet associated with the session. This is used as part of SNMP's (v1 and v2c) administrative/security framework. See RFC 1157 or RFC 1901|public|
|TBD|display_string|TBD|string|A system description of the SNMP responder endpoint.|VMware ESXi 5.5.0 build-4722766 VMware, Inc. x86_64|
|TBD|get_bulk_requests|TBD|integer|The number of variable bindings in GetBulkRequest PDUs seen for the session|0|
|TBD|get_requests|TBD|integer|The number of variable bindings in GetRequest/GetNextRequest PDUs seen for the session|2|
|TBD|get_responses|TBD|integer|The number of variable bindings in GetResponse/Response PDUs seen for the session|2|
|TBD|set_requests|TBD|integer|The number of variable bindings in SetRequest PDUs seen for the session|1|
|TBD|up_since        date_time|TBD|The time at which the SNMP responder endpoint claims it's been up since|``||
|TBD|version|TBD|string|The version of SNMP being used.|1|
