# SSL Log

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
|#TODO:NewFieldName|cert_chain_fuids|array_string|"(present if base/protocols/ssl/files.bro is loaded) An ordered vector of all certificate file unique IDs for the certificates offered by the server."|
|#TODO:NewFieldName|client_cert_chain_fuids|array_string|"(present if base/protocols/ssl/files.bro is loaded) An ordered vector of all certificate file unique IDs for the certificates offered by the client."|
|#TODO:NewFieldName|server_name|string|Value of the Server Name Indicator SSL/TLS extension. It indicates the server name that the client was requesting.|
|#TODO:NewFieldName|cipher|string|SSL/TLS cipher suite that the server chose.|unknown-44;TLS_RSA_WITH_NULL_MD5;TLS_PSK_WITH_3DES_EDE_CBC_SHA;TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 ;TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256;TLS_DHE_DSS_WITH_AES_128_CBC_SHA;TLS_ECDH_ANON_WITH_NULL_SHA
|#TODO:NewFieldName|client_issuer|string|"(present if base/protocols/ssl/files.bro is loaded) Subject of the signer of the X.509 certificate offered by the client."|
|#TODO:NewFieldName|orig_certificate_sha1|string|"sha1 representation of the servers certificate. this is rock specific https://github.com/rocknsm/rock-scripts/pull/20/commits/70078609d3fcaf2eb518f63aa97196b8cae4a4d1#diff-e81eb6aac74c4d7ead9da22ed9198871"|
|#TODO:NewFieldName|client_subject|string|"(present if base/protocols/ssl/files.bro is loaded) Subject of the X.509 certificate offered by the client."|
|#TODO:NewFieldName|curve|string|Elliptic curve the server chose when using ECDH/ECDHE.|
|#TODO:NewFieldName|established|boolean|Flag to indicate if this ssl session has been established successfully, or if it was aborted during the handshake.|
|#TODO:NewFieldName|ja3|string|(prsent if https://github.com/salesforce/ja3/blob/master/bro/ja3.bro is loaded)|
|#TODO:NewFieldName|ja3s|string|(prsent if https://github.com/salesforce/ja3/blob/master/bro/ja3s.bro.bro is loaded)|
|#TODO:NewFieldName|last_alert|string|Last alert that was seen during the connection.|handshake_failure; unknown_ca; bad_certificate; certificate_unknown; close_notify; unrecognized_name; protocol_version; decrypt_error; certificate_expired; internal_error; inappropriate_fallback; bad_record_mac; unexpected_message; decode_error; illegal_parameter; unknown-138; unknown-27; unknown-55; no_certificate; unknown-116; unknown-145; unknown-19; unknown-209; unknown-232; unknown-37; unknown-93; access_denied; decryption_failed; unknown-102; unknown-106; unknown-11; unknown-119; unknown-12; unknown-125; unknown-136; unknown-143; unknown-148; unknown-156; unknown-159; unknown-16; unknown-162; unknown-171; unknown-175; unknown-177; unknown-184; unknown-185; unknown-186; unknown-188; unknown-192; unknown-193; unknown-195; unknown-199; unknown-200; unknown-201; unknown-215; unknown-219; unknown-222; unknown-224; unknown-229; unknown-245; unknown-246; unknown-247; unknown-38; unknown-61; unknown-63; unknown-67; unknown-69; unknown-73; unknown-78; unknown-79; unknown-81; unknown-85; unknown-91; unknown-97; bad_certificate_hash_value; certificate_unobtainable; insufficient_security; no_application_protocol; no_renegotiation; unknown-101; unknown-103; unknown-105; unknown-107; unknown-109; unknown-117; unknown-121; unknown-122; unknown-123; unknown-13; unknown-131; unknown-134; unknown-141; unknown-146; unknown-153; unknown-154; unknown-163; unknown-165; unknown-166; unknown-168; unknown-176; unknown-179; unknown-18; unknown-181; unknown-189; unknown-191; unknown-196; unknown-197; unknown-203; unknown-205; unknown-206; unknown-207; unknown-212; unknown-214; unknown-217; unknown-220; unknown-221; unknown-228; unknown-230; unknown-235; unknown-236; unknown-237; unknown-238; unknown-241; unknown-242; unknown-244; unknown-249; unknown-25; unknown-250; unknown-252; unknown-28; unknown-33; unknown-34; unknown-35; unknown-36; unknown-52; unknown-54; unknown-56; unknown-57; unknown-58; unknown-68; unknown-7; unknown-74; unknown-76; unknown-8; unknown-83; unknown-95; unknown-98; unknown-99; unknown_psk_identity; user_canceled
|#TODO:NewFieldName|next_protocol|string|Next protocol the server chose using the application layer next protocol extension, if present.|spdy/3.1;grpc-exp;apns-pack-v1:4096:4096;http/1.1;h2
|#TODO:NewFieldName|notary|string|"(present if policy/protocols/ssl/notary.bro is loaded) A response from the ICSI certificate notary."|
|#TODO:NewFieldName|ocsp_status|string|"(present if policy/protocols/ssl/validate-ocsp.bro is loaded) Result of ocsp validation for this connection."|
|#TODO:NewFieldName|resumed|boolean|Flag to indicate if the session was resumed reusing the key material exchanged in an earlier connection.|
|#TODO:NewFieldName|issuer|string|"(present if base/protocols/ssl/files.bro is loaded) Subject of the signer of the X.509 certificate offered by the server."|
|#TODO:NewFieldName|resp_certificate_sha1|string|"sha1 representation of the clients certificate. this is rock specific https://github.com/rocknsm/rock-scripts/pull/20/commits/70078609d3fcaf2eb518f63aa97196b8cae4a4d1#diff-e81eb6aac74c4d7ead9da22ed9198871"|
|#TODO:NewFieldName|subject|string|"(present if base/protocols/ssl/files.bro is loaded) Subject of the X.509 certificate offered by the server."|
|#TODO:NewFieldName|valid_ct_logs|integer|"(present if policy/protocols/ssl/validate-sct.bro is loaded) Number of different Logs for which valid SCTs were encountered in the connection."|
|#TODO:NewFieldName|valid_ct_operators|integer|"(present if policy/protocols/ssl/validate-sct.bro is loaded) Number of different Log operators of which valid SCTs were encountered in the connection."|
|#TODO:NewFieldName|valid_ct_operators_list|array_string|"(present if policy/protocols/ssl/validate-sct.bro is loaded) List of operators for which valid SCTs were encountered in the connection."|
|#TODO:NewFieldName|validation_status|boolean|"(present if policy/protocols/ssl/validate-certs.bro is loaded) Result of certificate validation for this connection."|ok;unable to get local issuer certificate;self signed certificate in certificate chain;self signed certificate;certificate has expired
|#TODO:NewFieldName|version|string|SSL/TLS version that the server chose.|TLSv12;TLSv10'TLSv11;SSLv3;TLSv13
|#TODO:NewFieldName|version_num|integer|Numeric SSL/TLS version that the server chose.|