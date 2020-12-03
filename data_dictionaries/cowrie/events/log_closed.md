# Cowrie log closed
###### Version: 0

## Description
This dictionary details the fields for the log closed event of the Cowrie honeypot. Cowrie records a log of each terminal session that can then be replayed.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|event_timestamp|timestamp|string|Timestamp when the data was discovered in ISO 8601 format|`2020-10-06T06:45:02.021156`|
|src_ip_addr|src_ip|string|The originating/source IP address of the SSH connection|`192.168.1.4`|
|event_message|message|string|The message contained in the event|`SSH client hassh fingerprint: aaaabbbbcccc11112222`|
|dvc_hostname|sensor|string|The name of the device that generated the event|`hk-lab1`|
|network_session_id|session|string|A unique identifier for a cowrie SSH session|`aaacde98ab17`|
|TBD|ttylog|string|The path to the tty log file|`var/lib/cowrie/tty/2638f1c1c2018567a46a4cae049dd90db2d468e1538d60d328f2707d071f73c5`|
|TBD|size|integer|The size (in bytes) of the input data|`313`|
|TBD|shasum|string|SHA256 checksum of the data that was input to the terminal|`2638f1c1c2018567a46a4cae049dd90db2d468e1538d60d328f2707d071f73c5`|
|TBD|duplicate|boolean|A boolean indicating whether a tty log with the same name already exists|`False`|
|event_duration|duration|float|The duration of the terminal session, in seconds|`17.948433876037598`|

## References
* [Cowrie terminal emulation code](https://github.com/cowrie/cowrie/blob/master/src/cowrie/insults/insults.py#L194)
