# Cowrie session connection
###### Version: 0

## Description
This dictionary details the fields for the session connect event of the Cowrie honeypot.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|event_timestamp|timestamp|string|Timestamp when the data was discovered in ISO 8601 format|`2020-10-06T06:45:02.021156`|
|src_ip_addr|src_ip|string|The originating/source IP address of the SSH connection|`192.168.1.4`|
|event_message|message|string|The message contained in the event|`SSH client hassh fingerprint: aaaabbbbcccc11112222`|
|dvc_hostname|sensor|string|The name of the device that generated the event|`hk-lab1`|
|network_session_id|session|string|A unique identifier for a cowrie SSH session|`aaacde98ab17`|
|src_port|src_port|int|The port from which the SSH connection originated|`54973`|
|dst_ip_addr|dst_ip|string|Destination IP of the connection. Should be one of Cowrie's IP addresses|`192.168.1.22`|
|dst_port|dst_port|int|Destination port of the connection. Typically 22/2222/23/2223|`2222`|
|network_application_protocol|protocol|string|The protocol, SSH or telnet|`ssh`|

## References
* [Cowrie SSH transport code](https://github.com/cowrie/cowrie/blob/master/src/cowrie/ssh/transport.py#L56)
* [Cowrie telnet transport code](https://github.com/cowrie/cowrie/blob/master/src/cowrie/telnet/transport.py#L29)
