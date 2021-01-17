# Cowrie client size event
###### Version: 0

## Description
This dictionary details the fields for the client size event of the Cowrie honeypot, which gives information about the size of the client terminal. It might not trigger.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|event_timestamp|timestamp|string|Timestamp when the data was discovered in ISO 8601 format|`2020-10-06T06:45:02.021156`|
|src_ip_addr|src_ip|string|The originating/source IP address of the SSH connection|`192.168.1.4`|
|event_message|message|string|The message contained in the event|`SSH client hassh fingerprint: aaaabbbbcccc11112222`|
|dvc_hostname|sensor|string|The name of the device that generated the event|`hk-lab1`|
|network_session_id|session|string|A unique identifier for a cowrie SSH session|`aaacde98ab17`|
|TBD|width|TBD|The width of the terminal|`80`|
|TBD|height|TBD|The height of the terminal|`60`|

## References
* [Cowrie code](https://github.com/cowrie/cowrie/blob/master/src/cowrie/shell/session.py#L58)
