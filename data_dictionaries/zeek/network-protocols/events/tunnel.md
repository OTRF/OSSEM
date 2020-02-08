# Tunnel Log

## Description
None

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|@timestamp|ts|date_time|Timestamp of the beginning of the event in epoch format|`1300475167.096535`|
|src_ip_addr|id.orig_h|ip|The originating/source IP address|`10.1.1.1`|
|src_port|id.orig_p|integer|The originating/source port|`37682`|
|dst_ip_addr|id.resp_h|ip|The responding/destination IP address|`10.2.2.2`|
|dst_port|id.resp_p|integer|The responding/destination port|`3544`|
|event_uid|uid|string|The unique identifier for the tunnel, which may correspond to a connection's uid field for non-IP-in-IP tunnels. This is optional because there could be numerous connections for payload proxies like SOCKS but we should treat it as a single tunnel|````|
|TBD|action|string|The type of activity that occurred.|`Tunnel::TEREDO`|
|TBD|tunnel_type|string|The type of tunnel.|`Tunnel::DISCOVER`|
