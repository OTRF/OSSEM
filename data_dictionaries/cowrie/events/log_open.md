# Cowrie log open
###### Version: 0

## Description
This dictionary details the fields for the log open event of the Cowrie honeypot. This does not seem to trigger anymore.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|event_timestamp|timestamp|string|Timestamp when the data was discovered in ISO 8601 format|`2020-10-06T06:45:02.021156`|
|src_ip_addr|src_ip|string|The originating/source IP address of the SSH connection|`192.168.1.4`|
|event_message|message|string|The message contained in the event|`SSH client hassh fingerprint: aaaabbbbcccc11112222`|
|dvc_hostname|sensor|string|The name of the device that generated the event|`hk-lab1`|
|network_session_id|session|string|A unique identifier for a cowrie SSH session|`aaacde98ab17`|
|TBD|ttylog|string|The path to the tty log file|`log/tty/20170123-092633-None-0i.log`|

## References
* [Old version of cowrie terminal emulation code](https://github.com/cowrie/cowrie/blob/b9fb147d982f9c76351b1275217c1b7ad2abee64/src/cowrie/insults/insults.py#L77)
* [Commit that removed it](https://github.com/cowrie/cowrie/commit/85035a419c9bb75dd7086340cc99bce07ce77f96#)
