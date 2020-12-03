# Cowrie file upload
###### Version: 0

## Description
This dictionary details the fields for the file upload event of the Cowrie honeypot, which triggers when a file is uploaded to the honeypot with scp or sftp.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|event_timestamp|timestamp|string|Timestamp when the data was discovered in ISO 8601 format|`2020-10-06T06:45:02.021156`|
|src_ip_addr|src_ip|string|The originating/source IP address of the SSH connection|`192.168.1.4`|
|event_message|message|string|The message contained in the event|`SSH client hassh fingerprint: aaaabbbbcccc11112222`|
|dvc_hostname|sensor|string|The name of the device that generated the event|`hk-lab1`|
|network_session_id|session|string|A unique identifier for a cowrie SSH session|`aaacde98ab17`|
|file_name|filename|string|The name of the file uploaded|`bad.exe`|
|file_path|outfile|string|The path where the file is stored on the file system (outside of the honeypot)|`var/lib/cowrie/downloads/2267ef2579a94a6c2b0ba83e56a52031d4c21e916e1c45b7dfd1e01c98d6c5d9`|
|file_hash_sha256|shasum|string|The SHA256 hash of the file|`2267ef2579a94a6c2b0ba83e56a52031d4c21e916e1c45b7dfd1e01c98d6c5d9`|

## References
* [Cowrie code](https://github.com/cowrie/cowrie/blob/master/src/cowrie/shell/fs.py#L412)
