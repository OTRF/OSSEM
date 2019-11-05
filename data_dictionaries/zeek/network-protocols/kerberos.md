# Kerberos Log

## Description

## Event JSON

```json
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|     @timestamp     |     ts               |     date_time     |        Timestamp of the beginning of the event in epoch format     |     `1300475167.096535`  |
|     src_ip_addr     |     id.orig_h     |     ip     |     The originating/source IP address     |     `10.1.1.1`     |
|     src_port     |     id.orig_p          |     integer     |       The originating/source port        |     `37682`     |
|     dst_ip_addr     |     id.resp_h     |     ip     |     The responding/destination IP address     |     `10.2.2.2`     |
|     dst_port     |     id.resp_p          |     integer     |       The responding/destination port        |     `88`     |
|     TBD     |     uid     |     string     |     Unique ID for the connection.     |     `CHhAvVGS1DHFjwGM9`     |
|     TBD     |     server_cert_fuid     |     string     |     present if base/protocols/krb/files.bro is loaded File unique ID of server cert, if any |     ``     |
|     TBD     |     client_cert_fuid     |     string     |     present if base/protocols/krb/files.bro is loaded File unique ID of client cert, if any |     ``     |
|     TBD     |     error_code     |     integer     |     Error code  |   ``  |
|     TBD     |     error_msg     |     string     |     Error message| `KDC_ERR_C_PRINCIPAL_UNKNOWN`   |
|     TBD     |     success     |     boolean     |     Request result  |   ``  |
|     TBD     |     client     |     string     |     Client    |   `mycomputer-432aa2$/YOURDOMAIN.CORP.LOCAL`  |
|     TBD     |     client_cert_subject     |     string     |          present if base/protocols/krb/files.bro is loaded Subject of client certificate, if any |     ``     |
|     TBD     |     cipher     |     string     |     Ticket encryption type    |   `aes256-cts-hmac-sha1-96`    |
|     TBD     |     forwardable     |     boolean     |     Forwardable ticket requested    |   ``  |
|     TBD     |     auth_ticket     |     string     |          present if policy/protocols/krb/ticket-logging.bro is loaded Hash of ticket used to authorize request/transaction (client) (md5 hash) |     ``     |
|     TBD     |     renewable     |     boolean     |     Renewable ticket requested  |   ``  |
|     TBD     |     request_type     |     string     |     Request type - Authentication Service (“AS”) or Ticket Granting Service (“TGS”) |   `AS`    |
|     TBD     |     new_ticket     |     string     |          present if policy/protocols/krb/ticket-logging.bro is loaded Hash of ticket returned by the KDC (server) |     ``     |
|     TBD     |     server_cert_subject     |     string     |          present if base/protocols/krb/files.bro is loaded Subject of server certificate, if any |     ``     |
|     TBD     |     service     |     string     |     Service  | `MSSQLSvc/somecomputernam.YOURDOMAIN.CORP.LOCAL:1433` |
|     TBD     |     from    |   date_time   |   Ticket valid from   |   `June 11th 2018, 01:23:23.000`   |
|     TBD     |     till    |   date_time   |   Ticket valid till   |   `September 13th 2037, 02:48:05.000` |