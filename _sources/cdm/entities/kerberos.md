# kerberos

Event fields used to define Kerberos Ticket Granting Service and Kerberos Ticket Granting Tickets. For certificate information within Kerberos see the ./x509_and_certificates.md

## Attributes

| Name | Type | Description | Sample Value |
|:---|:---|:---|:---|
 | krb_service_name | string | the name of the account or computer for which the TGS ticket was requested | ```WIN2008R2$``` |
 | krb_ticket_encryption_type | string | the cryptographic suite that was used for issued TGS. | ```0x12``` |
 | krb_ticket_options | string | this is a set of different ticket flags in hexadecimal format. | ```0x40810010``` |
 | krb_ticket_pre_auth_type | integer | the code number of pre-Authentication type which was used in TGT request. | ```15``` |
 | krb_ticket_request_type | string | Request type - Authentication Service ("AS") or Ticket Granting Service ("TGS") | ```TGS``` |
 | krb_ticket_status | string | hexadecimal result code of TGS issue operation. | ```0x0``` |
