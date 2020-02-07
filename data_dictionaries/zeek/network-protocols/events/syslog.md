# Syslog Log

## Description
None

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|ts|TBD|date_time||1300475167.096535|
|TBD|id.orig_h|TBD|ip|The originating/source IP address|10.1.1.1|
|TBD|id.orig_p|TBD|integer|The originating/source port|37682|
|network_protocol|proto|TBD|string|Protocol over which the message was seen. Typically UDP but can definitely (and should) be TCP in some scenarios|udp|
|TBD|id.resp_h|TBD|ip|The responding/destination IP address|10.2.2.2|
|TBD|id.resp_p|TBD|integer|The responding/destination port|514|
|event_uid|uid|TBD|string|Unique ID for the connection.|CHhAvVGS1DHFjwGM9|
|TBD|facility|TBD|string|Syslog facility for the message|``|
|TBD|severity|TBD|string|Syslog severity for the message|``|
|TBD|message|TBD|string|The plain text message|``|
