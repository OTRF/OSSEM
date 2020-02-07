# Kerberos Log

## Description
None

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|@timestamp|ts|TBD|date_time|Timestamp of the beginning of the event in epoch format|1300475167.096535|
|src_ip_addr|id.orig_h|TBD|ip|The originating/source IP address|10.1.1.1|
|src_port|id.orig_p|TBD|integer|The originating/source port|37682|
|dst_ip_addr|id.resp_h|TBD|ip|The responding/destination IP address|10.2.2.2|
|dst_port|id.resp_p|TBD|integer|The responding/destination port|88|
|event_uid|uid|TBD|string|Unique ID for the connection.|CHhAvVGS1DHFjwGM9|
|TBD|server_cert_fuid|TBD|string|present if base/protocols/krb/files.bro is loaded File unique ID of server cert, if any|``|
|TBD|client_cert_fuid|TBD|string|present if base/protocols/krb/files.bro is loaded File unique ID of client cert, if any|``|
|TBD|error_code|TBD|integer|Error code|``|
|TBD|error_msg|TBD|string|Error message|KDC_ERR_C_PRINCIPAL_UNKNOWN|
|TBD|success|TBD|boolean|Request result|``|
|TBD|client|TBD|string|Client|mycomputer-432aa2$/YOURDOMAIN.CORP.LOCAL|
|TBD|client_cert_subject|TBD|string|present if base/protocols/krb/files.bro is loaded Subject of client certificate, if any|``|
|TBD|cipher|TBD|string|Ticket encryption type|aes256-cts-hmac-sha1-96|
|TBD|forwardable|TBD|boolean|Forwardable ticket requested|``|
|TBD|auth_ticket|TBD|string|present if policy/protocols/krb/ticket-logging.bro is loaded Hash of ticket used to authorize request/transaction (client) (md5 hash)|``|
|TBD|renewable|TBD|boolean|Renewable ticket requested|``|
|ticket_request_type|request_type|TBD|string|Request type - Authentication Service ("AS") or Ticket Granting Service ("TGS")|AS|
|TBD|new_ticket|TBD|string|present if policy/protocols/krb/ticket-logging.bro is loaded Hash of ticket returned by the KDC (server)|``|
|TBD|server_cert_subject|TBD|string|present if base/protocols/krb/files.bro is loaded Subject of server certificate, if any|``|
|TBD|service|TBD|string|Service|MSSQLSvc/somecomputernam.YOURDOMAIN.CORP.LOCAL:1433|
|TBD|from|TBD|date_time|Ticket valid from|June 11th 2018, 01:23:23.000|
|TBD|till|TBD|date_time|Ticket valid till|September 13th 2037, 02:48:05.000|
