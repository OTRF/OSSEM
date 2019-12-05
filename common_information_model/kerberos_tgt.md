# Kerberos TGT Schema

Event fields used to define Kerberos Ticket Granting Tickets.

## Data Fields

| Standard Name | Type | Description | Sample Value |
|--------|---------|-------|-------|
|service_name|string|the name of the service in the Kerberos Realm to which TGT request was sent. Typically has value "krbtgt" for TGT requests, which means Ticket Granting Ticket issuing service. For Failure events Service Name typically has the following format: krbtgt/REALM_NAME. For example: krbtgt/CONTOSO.|krbtgt|
|ticket_options|string|this is a set of different ticket flags in hexadecimal format.|0x40810010|
|ticket_status|string|hexadecimal result code of TGT issue operation.|0x0|
|ticket_encryption_type|string|the cryptographic suite that was used for issued TGT|0x12|
|ticket_pre_auth_type|integer|the code number of pre-Authentication type which was used in TGT request.|15|
|certificate_issuer_name|string|the name of the Certification Authority that issued the smart card certificate. Populated in Issued by field in certificate.|contoso-DC01-CA-1|
|certificate_serial_number|string|smart card certificates serial number. Can be found in Serial number field in the certificate.|1D0000000D292FBE3C6CDDAFA200020000000D|
|certificate_thumbprint|string|smart card certificates thumbprint. Can be found in Thumbprint field in the certificate.|564DFAEE99C71D62ABC553E695BD8DBC46669413|