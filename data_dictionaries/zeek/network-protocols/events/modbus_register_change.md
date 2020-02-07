# Modbus Register Change Log

## Description
None

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|@timestamp|ts|TBD|date_time|Timestamp of the beginning of the event in epoch format|1300475167.096535|
|network_protocol|proto|TBD|string|The transport layer network_protocolcol of the connection. Can be UDP but is usually TCP|tcp|
|src_ip_addr|id.orig_h|TBD|ip|The originating/source IP address|10.1.1.1|
|src_port|id.orig_p|TBD|integer|The originating/source port|37682|
|dst_ip_addr|id.resp_h|TBD|ip|The responding/destination IP address|10.2.2.2|
|dst_port|id.resp_p|TBD|integer|The responding/destination port|502|
|event_uid|uid|TBD|string|Unique ID for the connection.|CHhAvVGS1DHFjwGM9|
|TBD|delta|TBD|float|The time delta between when the old_val and new_val were seen. present if policy/protocols/modbus/track-memmap.bro is loaded.|``|
|TBD|new_val|TBD|integer|The new value stored in the register (present if policy/protocols/modbus/track-memmap.bro is loaded.|``|
|TBD|old_val|TBD|integer|The old value stored in the register. (present if policy/protocols/modbus/track-memmap.bro is loaded.|``|
|TBD|register|TBD|integer|The device memory offset. (present if policy/protocols/modbus/track-memmap.bro is loaded)"|``|
