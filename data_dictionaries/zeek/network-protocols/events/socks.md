# Socks Log

## Description
None

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|@timestamp|ts|TBD|date_time|Timestamp of the beginning of the event in epoch format|1300475167.096535|
|src_ip_addr|id.orig_h|TBD|ip|The originating/source IP address|10.1.1.1|
|src_port|id.orig_p|TBD|integer|The originating/source port|37682|
|dst_ip_addr|id.resp_h|TBD|ip|The responding/destination IP address|10.2.2.2|
|dst_port|id.resp_p|TBD|integer|The responding/destination port|1080|
|event_uid|uid|TBD|string|Unique ID for the tunnel - may correspond to connection uid or be non-existent|``|
|TBD|user|TBD|string|Username used to request a login to the proxy|``|
|TBD|password|TBD|string|Password used to request a login to the proxy|``|
|TBD|bound_host|TBD|ip|Server bound ip|``|
|TBD|bound_name|TBD|string|Server bound name.|i)'ÐÐ#"";""8ÐÐö|
|TBD|bound_p|TBD|integer|Server bound port.|19973|
|TBD|request_host|TBD|ip|Client requested SOCKS ip|``|
|TBD|request_name|TBD|string|Client requested SOCKS name|``|
|TBD|request_p|TBD|integer|Client requested port|``|
|TBD|status|TBD|string|Server status for the attempt at using the proxy.|succeeded|
|TBD|version|TBD|integer|Protocol version of SOCKS.|4|
|TBD|bound_|TBD|json_object|Server bound address. Could be an address, a name or both|``|
|TBD|request_|TBD|json_object|Client requested SOCKS address. Could be an address, a name or both|``|
