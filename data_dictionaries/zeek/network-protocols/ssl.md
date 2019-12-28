# SSL Log

## Description

## Event JSON

```json
{
    "ts": 1562945561.215724,
    "uid": "CGaE3F32QyMo97CDkc",
    "id.orig_h": "10.7.12.101",
    "id.orig_p": 49213,
    "id.resp_h": "216.98.148.151",
    "id.resp_p": 443,
    "version": "TLSv10",
    "cipher": "TLS_RSA_WITH_AES_128_CBC_SHA",
    "resumed": false,
    "established": true,
    "cert_chain_fuids": [
        "FHL4Zp1jb1ExVM6gw4"
    ],
    "client_cert_chain_fuids": [],
    "subject": "CN=trcodoretur.4Arentthetifth.viajes,OU=Is.ow pandme,O=Pthemide Fteiosie PSU,L=Nicosia,C=CY",
    "issuer": "CN=trcodoretur.4Arentthetifth.viajes,OU=Is.ow pandme,O=Pthemide Fteiosie PSU,L=Nicosia,C=CY",
    "validation_status": "self signed certificate",
    "ja3": "6734f37431670b3ab4292b8f60f29984",
    "ja3s": "4192c0a946c5bd9b544b4656d9f624a4"
}
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|     @timestamp     |     ts               |     date_time     |        Timestamp of the beginning of the event in epoch format     |     `1300475167.096535`  |
|     src_ip_addr     |     id.orig_h     |     ip     |     The originating/source IP address     |     `10.1.1.1`     |
|     src_port     |     id.orig_p          |     integer     |       The originating/source port        |     `37682`     |
|     dst_ip_addr     |     id.resp_h     |     ip     |     The responding/destination IP address     |     `10.2.2.2`     |
|     dst_port     |     id.resp_p          |     integer     |       The responding/destination port        |     `443`     |
|     event_uid     |     uid     |     string     |     Unique ID for the connection.     |     `CHhAvVGS1DHFjwGM9`     |
|     TBD     |     cert_chain_fuids     |     array_string     |          present if base/protocols/ssl/files.bro is loaded An ordered vector of all certificate file unique IDs for the certificates offered by the server.   |   ``  |
|     TBD     |     client_cert_chain_fuids     |     array_string     |          present if base/protocols/ssl/files.bro is loaded An ordered vector of all certificate file unique IDs for the certificates offered by the client.   |   ``  |
|     destination_hostname     |     server_name     |     string     |     Value of the Server Name Indicator SSL/TLS extension. It indicates the server name that the client was requesting     |     ``     |
|     TBD     |     cipher     |     string     |     SSL/TLS cipher suite that the server chose.   |   `TLS_RSA_WITH_NULL_MD5` |
|     TBD     |     client_issuer     |     string     |          present if base/protocols/ssl/files.bro is loaded Subject of the signer of the X.509 certificate offered by the client.   |   ``  |
|     TBD     |     orig_certificate_sha1     |     string     |     sha1 representation of the servers certificate. this is rock specific https://github.com/rocknsm/rock-scripts/pull/20/commits/70078609d3fcaf2eb518f63aa97196b8cae4a4d1#diff-e81eb6aac74c4d7ead9da22ed9198871 |     ``     |
|     TBD     |     client_subject     |     string     |          present if base/protocols/ssl/files.bro is loaded Subject of the X.509 certificate offered by the client.   |   ``  |
|     TBD     |     curve     |     string     |     Elliptic curve the server chose when using ECDH/ECDHE     |     ``     |
|     TBD     |     established     |     boolean     |     Flag to indicate if this ssl session has been established successfully, or if it was aborted during the handshake     |     ``     |
|     TBD     |     ja3     |     string     |     present if https://github.com/salesforce/ja3/blob/master/bro/ja3.bro is loaded     |   ``  |
|     TBD     |     ja3s     |     string     |     present if https://github.com/salesforce/ja3/blob/master/bro/ja3s.bro.bro is loaded     |   ``  |
|     TBD     |     last_alert     |     string     |     Last alert that was seen during the connection.   |   `handshake_failure` |
|     TBD     |     next_protocol     |     string     |     Next protocol the server chose using the application layer next protocol extension, if present.   |    `spdy/3.1`  |
|     TBD     |     notary     |     string     |          present if policy/protocols/ssl/notary.bro is loaded A response from the ICSI certificate notary.   |   ``  |
|     TBD     |     ocsp_status     |     string     |          present if policy/protocols/ssl/validate-ocsp.bro is loaded Result of ocsp validation for this connection.   |   ``  |
|     TBD     |     resumed     |     boolean     |     Flag to indicate if the session was resumed reusing the key material exchanged in an earlier connection     |     ``     |
|     TBD     |     issuer     |     string     |          present if base/protocols/ssl/files.bro is loaded Subject of the signer of the X.509 certificate offered by the server.   |   ``  |
|     TBD     |     resp_certificate_sha1     |     string     |     "sha1 representation of the clients certificate. this is rock specific https://github.com/rocknsm/rock-scripts/pull/20/commits/70078609d3fcaf2eb518f63aa97196b8cae4a4d1#diff-e81eb6aac74c4d7ead9da22ed9198871 |     ``     |
|     TBD     |     subject     |     string     |          present if base/protocols/ssl/files.bro is loaded Subject of the X.509 certificate offered by the server.   |   ``  |
|     TBD     |     valid_ct_logs     |     integer     |          present if policy/protocols/ssl/validate-sct.bro is loaded Number of different Logs for which valid SCTs were encountered in the connection.   |   ``  |
|     TBD     |     valid_ct_operators     |     integer     |          present if policy/protocols/ssl/validate-sct.bro is loaded Number of different Log operators of which valid SCTs were encountered in the connection.   |   ``  |
|     TBD     |     valid_ct_operators_list     |     array_string     |          present if policy/protocols/ssl/validate-sct.bro is loaded List of operators for which valid SCTs were encountered in the connection.   |   ``  |
|     TBD     |     validation_status     |     boolean     |          present if policy/protocols/ssl/validate-certs.bro is loaded Result of certificate validation for this connection.   | `self signed certificate` |
|     TBD     |     version     |     string     |     SSL/TLS version that the server chose.   |   ``TLSv13`   |
|     TBD     |     version_num     |     integer     |     Numeric SSL/TLS version that the server chose     |     ``     |