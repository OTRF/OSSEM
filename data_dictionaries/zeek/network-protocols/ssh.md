# SSH Log

## Description

## Event JSON

```json
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|#TODO:NewFieldName|@stream|string||
|#TODO:NewFieldName|ts|date_time||
|#TODO:NewFieldName|id.orig_h|ip||
|#TODO:NewFieldName|id.orig_p|integer||
|#TODO:NewFieldName|id.resp_h|ip||
|#TODO:NewFieldName|id.resp_p|integer||
|#TODO:NewFieldName|uid|string|Unique ID for the connection.|
|#TODO:NewFieldName|direction|string|Direction of the connection. If the client was a local host logging into an external host, this would be OUTBOUND. INBOUND would be set for the opposite situation.|
|#TODO:NewFieldName|auth_attempts|integer|The number of authentication attemps we observed. There’s always at least one, since some servers might support no authentication at all. It’s important to note that not all of these are failures, since some servers require two-factor auth (e.g. password AND pubkey)|
|#TODO:NewFieldName|auth_success|boolean|Authentication result (T=success, F=failure, unset=unknown)|
|#TODO:NewFieldName|cipher_alg|string|The encryption algorithm in use|aes256-cbc;aes128-ctr
|#TODO:NewFieldName|client|string|The client’s version string|SSH-2.0-1.82 sshlib: ClientSftp;SSH-2.0-WinSCP_release_5.9.4
|#TODO:NewFieldName|compression_alg|string|The compression algorithm in use|zlib
|#TODO:NewFieldName|cshka|array_string|(present if https://github.com/salesforce/hassh is loaded)|ssh-rsa,rsa-sha2-512,rsa-sha2-256,ecdsa-sha2-nistp256,ssh-ed25519
|#TODO:NewFieldName|hassh|string|(present if https://github.com/salesforce/hassh is loaded)|
|#TODO:NewFieldName|hasshAlgorithms|array_string|(present if https://github.com/salesforce/hassh is loaded)|curve25519-sha256@libssh.org,ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256,diffie-hellman-group-exchange-sha1,diffie-hellman-group14-sha1,diffie-hellman-group1-sha1;aes128-ctr,aes192-ctr,aes256-ctr,arcfour256,arcfour128,aes128-gcm@openssh.com,aes256-gcm@openssh.com,chacha20-poly1305@openssh.com,aes128-cbc,3des-cbc,blowfish-cbc,cast128-cbc,aes192-cbc,aes256-cbc,arcfour,rijndael-cbc@lysator.liu.se;hmac-md5-etm@openssh.com,hmac-sha1-etm@openssh.com,umac-64-etm@openssh.com,umac-128-etm@openssh.com,hmac-sha2-256-etm@openssh.com,hmac-sha2-512-etm@openssh.com,hmac-ripemd160-etm@openssh.com,hmac-sha1-96-etm@openssh.com,hmac-md5-96-etm@openssh.com,hmac-md5,hmac-sha1,umac-64@openssh.com,umac-128@openssh.com,hmac-sha2-256,hmac-sha2-512,hmac-ripemd160,hmac-ripemd160@openssh.com,hmac-sha1-96,hmac-md5-96;none,zlib@openssh.com
|#TODO:NewFieldName|hasshServer|string|(present if https://github.com/salesforce/hassh is loaded)|
|#TODO:NewFieldName|hasshServerAlgorithms|array_string|(present if https://github.com/salesforce/hassh is loaded)|curve25519-sha256@libssh.org,ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256,diffie-hellman-group-exchange-sha1,diffie-hellman-group14-sha1,rsa2048-sha256,rsa1024-sha1,diffie-hellman-group1-sha1;aes256-ctr,aes256-cbc,rijndael-cbc@lysator.liu.se,aes192-ctr,aes192-cbc,aes128-ctr,aes128-cbc,chacha20-poly1305@openssh.com,blowfish-ctr,blowfish-cbc,3des-ctr,3des-cbc,arcfour256,arcfour128;hmac-sha2-256,hmac-sha1,hmac-sha1-96,hmac-md5,hmac-sha2-256-etm@openssh.com,hmac-sha1-etm@openssh.com,hmac-sha1-96-etm@openssh.com,hmac-md5-etm@openssh.com;none,zlib
|#TODO:NewFieldName|hasshVersion|string|(present if https://github.com/salesforce/hassh is loaded)|1
|#TODO:NewFieldName|host_key|string|The server’s key fingerprint|dd:cc:3a:81:40:2a:fa:9b:eb:7e:24:3d:a2:56:7c:e3
|#TODO:NewFieldName|host_key_alg|string|The server host key’s algorithm|ssh-rsa
|#TODO:NewFieldName|kex_alg|string|The key exchange algorithm in use|curve25519-sha256@libssh.org;diffie-hellman-group-exchange-sha256
|#TODO:NewFieldName|mac_alg|string|The signing (MAC) algorithm in use|hmac-sha1;hmac-sha1;hmac-sha2-512
|#TODO:NewFieldName|server|string|The server’s version string|SSH-2.0-Sun_SSH_2.4;SSH-2.0-OpenSSH_5.3
|#TODO:NewFieldName|version|integer|SSH major version (1 or 2)|1;2
|#TODO:NewFieldName|remote_location.|json_object|"(present if policy/protocols/ssh/geo-data.bro is loaded) Add geographic data related to the “remote” host of the connection."|
|#TODO:NewFieldName|remote_location.country_code|string|The country code.|
|#TODO:NewFieldName|remote_location.region|string|The region.|
|#TODO:NewFieldName|remote_location.city|string|The city.|
|#TODO:NewFieldName|remote_location.latitude|double|Latitude.|
|#TODO:NewFieldName|remote_location.longitude|double|Longitude.|