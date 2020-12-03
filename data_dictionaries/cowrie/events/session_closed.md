# Cowrie session closed
###### Version: 0

## Description
This dictionary details the fields for the session closed event of the Cowrie honeypot.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|event_timestamp|timestamp|string|Timestamp when the data was discovered in ISO 8601 format|`2020-10-06T06:45:02.021156`|
|src_ip_addr|src_ip|string|The originating/source IP address of the SSH connection|`192.168.1.4`|
|event_message|message|string|The message contained in the event|`SSH client hassh fingerprint: aaaabbbbcccc11112222`|
|dvc_hostname|sensor|string|The name of the device that generated the event|`hk-lab1`|
|network_session_id|session|string|A unique identifier for a cowrie SSH session|`aaacde98ab17`|
|network_duration|duration|float|The duration (in second) of a cowrie session|`120.00089073181152`|

## References
* [Cowrie SSH transport code](https://github.com/cowrie/cowrie/blob/master/src/cowrie/ssh/transport.py#L225)
* [Cowrie telnet transport code](https://github.com/cowrie/cowrie/blob/master/src/cowrie/telnet/transport.py#L66)
