# SSL Log
aka TLS

## Description

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
| @timestamp                        | ts                      | date_time    | Timestamp of the beginning of the event in epoch format                                                                                              | `1562945561.215724`                                                                           |
| zeek_id_cert_chain_fuids          | cert_chain_fuids        | array_string | present if base/protocols/ssl/files.bro is loaded An ordered vector of all certificate file unique IDs for the certificates offered by the server.   | `[ "FHL4Zp1jb1ExVM6gw4" ]`                                                                    |
| tls_cipher                        | cipher                  | string       | SSL/TLS cipher suite that the server chose.                                                                                                          | `TLS_RSA_WITH_AES_128_CBC_SHA`                                                                |
| zeek_id_client_cert_chain_fuids   | client_cert_chain_fuids | array_string | present if base/protocols/ssl/files.bro is loaded An ordered vector of all certificate file unique IDs for the certificates offered by the client.   | `[]`                                                                                          |
| certificate_issuer                | client_issuer           | string       | Subject of the signer of the X.509 certificate offered by the client.                                                                                | ``                                                                                            |
| certificate_subject               | client_subject          | string       | Subject of the X.509 certificate offered by the server                                                                                               | ``                                                                                            |
| tls_curve                         | curve                   | string       | Elliptic curve the server chose when using ECDH/ECDHE                                                                                                | ``                                                                                            |
| tls_established                   | established             | boolean      | Flag to indicate if this ssl session has been established successfully, or if it was aborted during the handshake                                    | `true`                                                                                        |
| src_ip_addr                       | id.orig_h               | ip           | The originating/source IP address                                                                                                                    | `10.7.12.101`                                                                                 |
| src_port                          | id.orig_p               | integer      | The originating/source port                                                                                                                          | `49213`                                                                                       |
| dst_ip_addr                       | id.resp_h               | ip           | The responding/destination IP address                                                                                                                | `216.98.148.151`                                                                              |
| dst_port                          | id.resp_p               | integer      | The responding/destination port                                                                                                                      | `443`                                                                                         |
| dst_certificate_issuer_name       | issuer                  | string       | Subject of the signer of the X.509 certificate offered by the server. present if base/protocols/ssl/files.bro is loaded                              | `CN=trcodoretur.4Arentthetifth.viajes,OU=Is.ow pandme,O=Pthemide Fteiosie PSU,L=Nicosia,C=CY` |
| hash_ja3                          | ja3                     | string       | JA3 hash of client ciphers and encryption info present if https://github.com/salesforce/ja3/blob/master/bro/ja3.bro is loaded                        | `6734f37431670b3ab4292b8f60f29984`                                                            |
| hash_ja3s                         | ja3s                    | string       | JA3 hash of server ciphers and encryption info present if https://github.com/salesforce/ja3/blob/master/bro/ja3s.bro.bro is loaded                   | `4192c0a946c5bd9b544b4656d9f624a4`                                                            |
| tls_last_alert                    | last_alert              | string       | Last alert that was seen during the connection.                                                                                                      | `handshake_failure`                                                                           |
| tls_next_protocol                 | next_protocol           | string       | Next protocol the server chose using the application layer next protocol extension, if present.                                                      | `spdy/3.1`                                                                                    |
| tls_notary_response               | notary                  | string       | A response from the ICSI certificate notary. present if policy/protocols/ssl/notary.bro is loaded                                                    | ``                                                                                            |
| oscp_validation_status            | ocsp_status             | string       | Result of ocsp validation for this connection. present if policy/protocols/ssl/validate-ocsp.bro is loaded                                           | ``                                                                                            |
| certificate_hash_sha1             | orig_certificate_sha1   | string       | sha1 representation of the client's                                                                                                                  | ``                                                                                            |
| dst_certificate_sha1              | resp_certificate_sha1   | string       | sha1 representation of the server's certificate                                                                                                      | ``                                                                                            |
| tls_resumed                       | resumed                 | boolean      | Flag to indicate if the session was resumed reusing the key material exchanged in an earlier connection                                              | `false`                                                                                       |
| tls_server_name                   | server_name             | string       | Value of the Server Name Indicator SSL/TLS extension. It indicates the server name that the client was requesting                                    | ``                                                                                            |
| dst_certificate_subject_name      | subject                 | string       | Subject of the X.509 certificate offered by the server. present if base/protocols/ssl/files.bro is loaded                                            | `CN=trcodoretur.4Arentthetifth.viajes,OU=Is.ow pandme,O=Pthemide Fteiosie PSU,L=Nicosia,C=CY` |
| event_uid                         | uid                     | string       | Unique ID for the connection.                                                                                                                        | `CGaE3F32QyMo97CDkc`                                                                          |
| TBD                               | valid_ct_logs           | integer      | Number of different Logs for which valid SCTs were encountered in the connection. present if policy/protocols/ssl/validate-sct.bro is loaded         | ``                                                                                            |
| TBD                               | valid_ct_operators      | integer      | Number of different Log operators of which valid SCTs were encountered in the connection. present if policy/protocols/ssl/validate-sct.bro is loaded | ``                                                                                            |
| TBD                               | valid_ct_operators_list | array_string | List of operators for which valid SCTs were encountered in the connection. present if policy/protocols/ssl/validate-sct.bro is loaded                | ``                                                                                            |
| tls_certificate_validation_status | validation_status       | boolean      | Result of certificate validation for this connection. present if policy/protocols/ssl/validate-certs.bro is loaded                                   | `self signed certificate`                                                                     |
| tls_version                       | version                 | string       | SSL/TLS version that the server chose.                                                                                                               | `TLSv10`                                                                                      |
| tls_version_number                | version_num             | integer      | Numeric SSL/TLS version that the server chose                                                                                                        | ``                                                                                            |
| dst_host_name                     | z_Enrichment            | string       | Enrichment copied from `tls_server_name`                                                                                                             | ``                                                                                            |
| network_protocol                  | z_Enrichment            | string       | Enrichment implied tcp                                                                                                                               | `tcp`                                                                                         |
| zeek_dst_chained_certs_count      | z_Enrichment            | string       | Count of the number of chained certs based on the length of the array of `zeek_id_cert_chain_fuids`                                                  | `4`                                                                                           |
| zeek_src_chained_certs_count      | z_Enrichment            | string       | Count of the number of chained certs based on the length of the array of `zeek_id_client_cert_chain_fuids`                                           | `2`                                                                                           |

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
