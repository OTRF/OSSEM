# SSH Log

## Description
None

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|@timestamp|ts|TBD|date_time|Timestamp of the beginning of the event in epoch format|1300475167.096535|
|src_ip_addr|id.orig_h|TBD|ip|The originating/source IP address|10.1.1.1|
|src_port|id.orig_p|TBD|integer|The originating/source port|37682|
|dst_ip_addr|id.resp_h|TBD|ip|The responding/destination IP address|10.2.2.2|
|dst_port|id.resp_p|TBD|integer|The responding/destination port|22|
|event_uid|uid|TBD|string|Unique ID for the connection.|CHhAvVGS1DHFjwGM9|
|TBD|direction|TBD|string|Direction of the connection. If the client was a local host logging into an external host, this would be OUTBOUND. INBOUND would be set for the opposite situation|``|
|TBD|auth_attempts|TBD|integer|The number of authentication attemps we observed. There's always at least one, since some servers might support no authentication at all. It's important to note that not all of these are failures, since some servers require two-factor auth (e.g. password AND pubkey)|``|
|TBD|auth_success|TBD|boolean|Authentication result (T=success, F=failure, unset=unknown)|true|
|TBD|cipher_alg|TBD|string|The encryption algorithm in use|aes256-cbc|
|TBD|client|TBD|string|The client's version string|SSH-2.0-1.82 sshlib|
|TBD|compression_alg|TBD|string|The compression algorithm in use|zlib|
|TBD|cshka|TBD|array_string|present if https://github.com/salesforce/hassh is loaded)|ssh-ed25519|
|TBD|hassh|TBD|string|present if https://github.com/salesforce/hassh is loaded|``|
|TBD|hasshAlgorithms|TBD|array_string|present if https://github.com/salesforce/hassh is loaded|curve25519-sha256@libssh.org|
|TBD|hasshServer|TBD|string|present if https://github.com/salesforce/hassh is loaded|``|
|TBD|hasshServerAlgorithms|TBD|array_string|present if https://github.com/salesforce/hassh is loaded|[ "curve25519-sha256@libssh.org", "ecdh-sha2-nistp256" ]|
|TBD|hasshVersion|TBD|string|present if https://github.com/salesforce/hassh is loaded|1|
|TBD|host_key|TBD|string|The server's key fingerprint|dd:cc:3a:81:40:2a:fa:9b:eb:7e:24:3d:a2:44:7c:e3|
|TBD|host_key_alg|TBD|string|The server host key's algorithm|ssh-rsa|
|TBD|kex_alg|TBD|string|The key exchange algorithm in use|diffie-hellman-group-exchange-sha256|
|TBD|mac_alg|TBD|string|The signing (MAC) algorithm in use|hmac-sha2-512|
|TBD|server|TBD|string|The server's version string|SSH-2.0-OpenSSH_5.3|
|TBD|version|TBD|integer|SSH major version (1 or 2)|2|
|TBD|remote_location.country_code|TBD|string|The country code|``|
|TBD|remote_location.region|TBD|string|The region|``|
|TBD|remote_location.city|TBD|string|The city|``|
|TBD|remote_location.latitude|TBD|double|Latitude|``|
|TBD|remote_location.longitude|TBD|double|Longitude|``|
