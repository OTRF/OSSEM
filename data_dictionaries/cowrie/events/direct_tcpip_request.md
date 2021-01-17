# Cowrie direct-tcpip request
###### Version: 0

## Description
This dictionary details the fields for the direct tcp-ip request event of the Cowrie honeypot, which triggers when someone tries to use the honeypot to forward data. This event does not contain the data forwarded.

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
|src_port|src_port|integer|The port from which the forwarding attempt was executed|`37380`|

## References
* [Cowrie forwarding code](https://github.com/cowrie/cowrie/blob/master/src/cowrie/ssh/forwarding.py#L23)
