# Kerberos Log

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
|#TODO:NewFieldName|server_cert_fuid|string|"(present if base/protocols/krb/files.bro is loaded) File unique ID of server cert, if any"|
|#TODO:NewFieldName|client_cert_fuid|string|"(present if base/protocols/krb/files.bro is loaded) File unique ID of client cert, if any"|
|#TODO:NewFieldName|error_code|integer|Error code|
|#TODO:NewFieldName|error_msg|string|Error message|KDC_ERR_CLIENT_REVOKED;KDC_ERR_PREAUTH_FAILED;KDC_ERR_C_PRINCIPAL_UNKNOWN;KRB_AP_ERR_TKT_EXPIRED;KRB_ERR_RESPONSE_TOO_BIG;KDC_ERR_NEVER_VALID;KRB_AP_ERR_BADMATCH;KRB_AP_ERR_TKT_EXPIRED
|#TODO:NewFieldName|success|boolean|Request result|
|#TODO:NewFieldName|client|string|Client|mycomputer-432vd2$/YOURDOMAIN.CORP.LOCAL;tom.sawyer/YOURDOMAIN.CORP.LOCAL
|#TODO:NewFieldName|client_cert_subject|string|"(present if base/protocols/krb/files.bro is loaded) Subject of client certificate, if any"|
|#TODO:NewFieldName|cipher|string|Ticket encryption type|aes256-cts-hmac-sha1-96;rc4-hmac
|#TODO:NewFieldName|forwardable|boolean|Forwardable ticket requested|
|#TODO:NewFieldName|auth_ticket|string|"(present if policy/protocols/krb/ticket-logging.bro is loaded) Hash of ticket used to authorize request/transaction (client) (md5 hash)"|
|#TODO:NewFieldName|renewable|boolean|Renewable ticket requested|
|#TODO:NewFieldName|request_type|string|Request type - Authentication Service (“AS”) or Ticket Granting Service (“TGS”)|AS;TGS
|#TODO:NewFieldName|new_ticket|string|"(present if policy/protocols/krb/ticket-logging.bro is loaded) Hash of ticket returned by the KDC (server)"|
|#TODO:NewFieldName|server_cert_subject|string|"(present if base/protocols/krb/files.bro is loaded) Subject of server certificate, if any"|
|#TODO:NewFieldName|service|string|Service|krbtgt/YOURDOMAIN.CORP.LOCAL;somecomputername$;cifs/SOMECOMPUTER01.yourdomain.corp.local/yourdomain.corp.local;HTTP/website.yourdomain.corp.local;tom.sawyer@YOURDOMAIN.CORP.LOCAL;MSSQLSvc/somecomputernam.YOURDOMAIN.CORP.LOCAL:1433;LDAP/SOMECOMPUTERNAME.YOURDOMAIN.CORP.LOCAL/YOURDOMAIN.CORP.LOCAL;exchangeRFR/somesite.yourdomain.corp.local;HOST/rtcps;GC/somecomputername.yourdomain.corp.local/yourdomain.corp.local;DNS/somecomputername.yourdomain.corp.local;
|#TODO:NewFieldName|from|date_time|Ticket valid from|June 11th 2018, 01:23:23.000
|#TODO:NewFieldName|till|date_time|Ticket valid till|September 13th 2037, 02:48:05.000