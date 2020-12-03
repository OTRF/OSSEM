# Cowrie client key exchange
###### Version: 0

## Description
This dictionary details the fields for the key exchange event of the Cowrie honeypot.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|event_timestamp|timestamp|string|Timestamp when the data was discovered in ISO 8601 format|`2020-10-06T06:45:02.021156`|
|src_ip_addr|src_ip|string|The originating/source IP address of the SSH connection|`192.168.1.4`|
|event_message|message|string|The message contained in the event|`SSH client hassh fingerprint: aaaabbbbcccc11112222`|
|dvc_hostname|sensor|string|The name of the device that generated the event|`hk-lab1`|
|network_session_id|session|string|A unique identifier for a cowrie SSH session|`aaacde98ab17`|
|TBD|hassh|string|[Hassh](https://github.com/salesforce/hassh) fingerprinting of the client supported algorithms|`de30354b88bae4c2810426614e1b6976`|
|TBD|hasshAlgorithms|string|List of algorithms used for the hassh fingerprint|`diffie-hellman-group-exchange-sha256,diffie-hellman-group-exchange-sha1,diffie-hellman-group14-sha1,diffie-hellman-group1-sha1;aes128-ctr,aes192-ctr,aes256-ctr,aes256-cbc,rijndael-cbc@lysator.liu.se,aes192-cbc,aes128-cbc,blowfish-cbc,arcfour128,arcfour,cast128-cbc,3des-cbc;hmac-sha2-256,hmac-sha2-512,hmac-sha1,hmac-sha1-96,hmac-md5,hmac-md5-96,hmac-ripemd160,hmac-ripemd160@openssh.com;none`|
|TBD|kexAlgs|list|List of key exchange algorithms proposed|`['diffie-hellman-group-exchange-sha256', 'diffie-hellman-group-exchange-sha1', 'diffie-hellman-group14-sha1', 'diffie-hellman-group1-sha1']`|
|TBD|keyAlgs|list|Host key algorithms|`['ssh-rsa', 'ssh-dss']`|
|TBD|encCS|list|Encryption algorithms|`['aes128-ctr', 'aes192-ctr', 'aes256-ctr', 'aes256-cbc']`|
|TBD|macCS|list|MAC algorithms|`['hmac-sha2-256', 'hmac-sha2-512', 'hmac-sha1']`|
|TBD|compCS|list|Compression algorithms|`['none', 'zlib@openssh.com', 'zlib']`|
|TBD|langCS|list|TBD|`TBD`|

## References
* [Cowrie SSH key exchange code](https://github.com/cowrie/cowrie/blob/master/src/cowrie/ssh/transport.py#L181)
