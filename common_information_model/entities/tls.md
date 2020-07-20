# TLS Entity
TLS(SSL) attributes. Most commonly associated with an HTTPS connection

## Data Fields
|Standard Name|Type|Description|Sample Value|
|---|---|---|---|
|tls_cipher|string|The cipher (encryption) parameters used to make the TLS connection|TLS_RSA_WITH_AES_128_CBC_SHA|
|tls_curve|string|Elliptic curve the server chose when using ECDH/ECDHE|TLS_RSA_WITH_AES_128_CBC_SHA|
|tls_established|boolean|Indicates if the session has been established successfully, or if it was aborted during the handshake|true|
|tls_next_protocol|string|Next protocol the server chose using the application layer next protocol extension, if present|spdy/3.1|
| tls_server_name|string|The name of the requested server/destination, this should be copied to `dst_host_name`|www.google.com|
|tls_resumed|boolean|If the session was resumed from previous established connection|false|
|tls_version|string|Version of TLS/SSL used (ie: SSLv3.0, TLSv1.1, TLSv1.2, TLSv1.3|TLSv10|
| tls_version_number|integer|Numeric value of the `tls_version`||
