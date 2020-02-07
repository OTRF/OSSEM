# Radius Log

## Description
None

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|@timestamp|ts|TBD|date_time|Timestamp of the beginning of the event in epoch format|1300475167.096535|
|src_ip_addr|id.orig_h|TBD|ip|The originating/source IP address|10.1.1.1|
|src_port|id.orig_p|TBD|integer|The originating/source port|37682|
|dst_ip_addr|id.resp_h|TBD|ip|The responding/destination IP address|10.2.2.2|
|dst_port|id.resp_p|TBD|integer|The responding/destination port|1812|
|event_uid|uid|TBD|string|Unique ID for the connection.|CHhAvVGS1DHFjwGM9|
|TBD|username|TBD|string|The username, if present.|host/somecomputername.domain.local|
|TBD|ttl|TBD|float|The duration between the first request and either the "Access-Accept" message or an error. If the field is empty, it means that either the request or response was not seen|``|
|TBD|result|TBD|boolean|Successful or failed authentication.|failed|
|TBD|mac|TBD|string|MAC address, if present|``|
|TBD|connect_info|TBD|string|Connect info, if present|``|
|TBD|framed_addr|TBD|ip|The address given to the network access server, if present. This is only a hint from the RADIUS server and the network access server is not required to honor the address|``|
|TBD|reply_msg|TBD|string|Reply message from the server challenge. This is frequently shown to the user authenticating|``|
|TBD|tunnel_client|TBD|string|Address (IPv4, IPv6, or FQDN) of the initiator end of the tunnel, if present. This is collected from the Tunnel-Client-Endpoint attribute|``|
