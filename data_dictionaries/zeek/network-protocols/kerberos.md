# Kerberos Log

## Description

## Event JSON

```json
{
    "ts": 1138098996.611848,
    "uid": "CxEr9TKbnWC1fzeJk",
    "id.orig_h": "10.5.12.5",
    "id.orig_p": 2565,
    "id.resp_h": "10.5.3.1",
    "id.resp_p": 88,
    "request_type": "TGS",
    "client": "u1/DENYDC.COM",
    "service": "HTTP/fc4.denyDC.com",
    "success": true,
    "till": 2136422885,
    "cipher": "rc4-hmac",
    "forwardable": true,
    "renewable": true
}
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|     @timestamp     |     ts               |     date_time     |        Timestamp of the beginning of the event in epoch format     |     `1138098996.611848`  |
|     src_ip_addr     |     id.orig_h     |     ip     |     The originating/source IP address     |     `10.5.12.5`     |
|     src_port     |     id.orig_p          |     integer     |       The originating/source port        |     `2565`     |
|     dst_ip_addr     |     id.resp_h     |     ip     |     The responding/destination IP address     |     `10.5.3.1`     |
|     dst_port     |     id.resp_p          |     integer     |       The responding/destination port        |     `88`     |
|     event_uid     |     uid     |     string     |     Unique ID for the connection.     |     `CHhAvVGS1DHFjwGM9`     |
|     TBD     |     server_cert_fuid     |     string     |     present if base/protocols/krb/files.bro is loaded File unique ID of server cert, if any |     ``     |
|     TBD     |     client_cert_fuid     |     string     |     present if base/protocols/krb/files.bro is loaded File unique ID of client cert, if any |     ``     |
|     TBD     |     error_code     |     integer     |     Error code  |   ``  |
|     TBD     |     error_msg     |     string     |     Error message| ``   |
|     TBD     |     success     |     boolean     |     Request result  |   `true`  |
|     TBD     |     client     |     string     |     Client    |   `u1/DENYDC.COM`  |
|     TBD     |     client_cert_subject     |     string     |          present if base/protocols/krb/files.bro is loaded Subject of client certificate, if any |     ``     |
|     TBD     |     cipher     |     string     |     Ticket encryption type    |   `aes256-cts-hmac-sha1-96`    |
|     TBD     |     forwardable     |     boolean     |     Forwardable ticket requested    |   `true`  |
|     TBD     |     auth_ticket     |     string     |          present if policy/protocols/krb/ticket-logging.bro is loaded Hash of ticket used to authorize request/transaction (client) (md5 hash) |     ``     |
|     TBD     |     renewable     |     boolean     |     Renewable ticket requested  |   `true`  |
|     ticket_request_type     |     request_type     |     string     |     Request type - Authentication Service (“AS”) or Ticket Granting Service (“TGS”) |   `TGS`    |
|     TBD     |     new_ticket     |     string     |          present if policy/protocols/krb/ticket-logging.bro is loaded Hash of ticket returned by the KDC (server) |     ``     |
|     TBD     |     server_cert_subject     |     string     |          present if base/protocols/krb/files.bro is loaded Subject of server certificate, if any |     ``     |
|     TBD     |     service     |     string     |     Service  | `HTTP/fc4.denyDC.com` |
|     TBD     |     from    |   date_time   |   Ticket valid from, in epoch format  |   ``   |
|     TBD     |     till    |   date_time   |   Ticket valid till, in epoch format  |   `2136422885` |