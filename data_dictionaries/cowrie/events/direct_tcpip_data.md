# Cowrie direct-tcpip data
###### Version: 0

## Description
This dictionary details the fields for the direct tcp-ip data event of the Cowrie honeypot, which triggers when someone tries to use the honeypot to forward data. This event holds the data that is attempted to be forwarded.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|event_timestamp|timestamp|string|Timestamp when the data was discovered in ISO 8601 format|`2020-10-06T06:45:02.021156`|
|src_ip_addr|src_ip|string|The originating/source IP address of the SSH connection|`192.168.1.4`|
|event_message|message|string|The message contained in the event|`SSH client hassh fingerprint: aaaabbbbcccc11112222`|
|dvc_hostname|sensor|string|The name of the device that generated the event|`hk-lab1`|
|network_session_id|session|string|A unique identifier for a cowrie SSH session|`aaacde98ab17`|
|dst_ip_addr|dst_ip|string|The IP towards which the forwarding attempt was executed|`192.168.1.23`|
|dst_port|dst_port|integer|The port towards which the forwarding attempt was executed|`80`|
|TBD|data|binary string|The data contained in the request|`b'\GET / HTTP/1.1\\r\\nHost: localhost:80\\r\\nUser-Agent: Mozilla/5.0'`|
|TBD|id|integer|An id for the request, which gets incremented for each new request|`1`|

## References
* [Cowrie forwarding code](https://github.com/cowrie/cowrie/blob/master/src/cowrie/ssh/forwarding.py#L94)
