# SSL Log

## Description
None

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|@timestamp|ts|TBD|date_time|Timestamp of the beginning of the event in epoch format|1562945561.215724|
|src_ip_addr|id.orig_h|TBD|ip|The originating/source IP address|10.7.12.101|
|src_port|id.orig_p|TBD|integer|The originating/source port|49213|
|dst_ip_addr|id.resp_h|TBD|ip|The responding/destination IP address|216.98.148.151|
|dst_port|id.resp_p|TBD|integer|The responding/destination port|443|
|event_uid|uid|TBD|string|Unique ID for the connection.|CGaE3F32QyMo97CDkc|
|zeek_uid_cert_chain_fuids|cert_chain_fuids|TBD|array_string|present if base/protocols/ssl/files.bro is loaded An ordered vector of all certificate file unique IDs for the certificates offered by the server.|[ "FHL4Zp1jb1ExVM6gw4" ]|
|zeek_uid_client_cert_chain_fuids|client_cert_chain_fuids|TBD|array_string|present if base/protocols/ssl/files.bro is loaded An ordered vector of all certificate file unique IDs for the certificates offered by the client.|[]|
|dst_host_name|server_name|TBD|string|Value of the Server Name Indicator SSL/TLS extension. It indicates the server name that the client was requesting|``|
|tls_cipher|cipher|TBD|string|SSL/TLS cipher suite that the server chose.|TLS_RSA_WITH_AES_128_CBC_SHA|
|certificate_issuer|client_issuer|TBD|string|Subject of the signer of the X.509 certificate offered by the client.|``|
|certificate_hash_sha1|orig_certificate_sha1|TBD|string|sha1 representation of the client's|``|
|certificate_subject|client_subject|TBD|string|Subject of the X.509 certificate offered by the server|``|
|tls_curve|curve|TBD|string|Elliptic curve the server chose when using ECDH/ECDHE|``|
|tls_established|established|TBD|boolean|Flag to indicate if this ssl session has been established successfully, or if it was aborted during the handshake|true|
|hash_ja3|ja3|TBD|string|JA3 hash of client ciphers and encryption info present if https://github.com/salesforce/ja3/blob/master/bro/ja3.bro is loaded|6734f37431670b3ab4292b8f60f29984|
|hash_ja3s|ja3s|TBD|string|JA3 hash of server ciphers and encryption info present if https://github.com/salesforce/ja3/blob/master/bro/ja3s.bro.bro is loaded|4192c0a946c5bd9b544b4656d9f624a4|
|tls_last_alert|last_alert|TBD|string|Last alert that was seen during the connection.|handshake_failure|
|tls_next_protocol|next_protocol|TBD|string|Next protocol the server chose using the application layer next protocol extension, if present.|spdy/3.1|
|tls_notary_response|notary|TBD|string|A response from the ICSI certificate notary. present if policy/protocols/ssl/notary.bro is loaded|``|
|oscp_validation_status|ocsp_status|TBD|string|Result of ocsp validation for this connection. present if policy/protocols/ssl/validate-ocsp.bro is loaded|``|
|tls_resumed|resumed|TBD|boolean|Flag to indicate if the session was resumed reusing the key material exchanged in an earlier connection|false|
|dst_certificate_issuer_name|issuer|TBD|string|Subject of the signer of the X.509 certificate offered by the server. present if base/protocols/ssl/files.bro is loaded|CN=trcodoretur.4Arentthetifth.viajes,OU=Is.ow pandme,O=Pthemide Fteiosie PSU,L=Nicosia,C=CY|
|dst_certificate_sha1|resp_certificate_sha1|TBD|string|sha1 representation of the server's certificate|``|
|dst_certificate_subject_name|subject|TBD|string|Subject of the X.509 certificate offered by the server. present if base/protocols/ssl/files.bro is loaded|CN=trcodoretur.4Arentthetifth.viajes,OU=Is.ow pandme,O=Pthemide Fteiosie PSU,L=Nicosia,C=CY|
|TBD|valid_ct_logs|TBD|integer|Number of different Logs for which valid SCTs were encountered in the connection. present if policy/protocols/ssl/validate-sct.bro is loaded|``|
|TBD|valid_ct_operators|TBD|integer|Number of different Log operators of which valid SCTs were encountered in the connection. present if policy/protocols/ssl/validate-sct.bro is loaded|``|
|TBD|valid_ct_operators_list|TBD|array_string|List of operators for which valid SCTs were encountered in the connection. present if policy/protocols/ssl/validate-sct.bro is loaded|``|
|tls_certificate_validation_status|validation_status|TBD|boolean|Result of certificate validation for this connection. present if policy/protocols/ssl/validate-certs.bro is loaded|self signed certificate|
|tls_version|version|TBD|string|SSL/TLS version that the server chose.|TLSv10|
|tls_version_number|version_num|TBD|integer|Numeric SSL/TLS version that the server chose|``|
