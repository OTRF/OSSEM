# Kerberos TGS Schema

Event fields used to define Kerberos Ticket Granting Service.

## Data Fields

| Standard Name | Type | Description | Sample Value |
|--------|---------|-------|-------|
|service_name|string|the name of the account or computer for which the TGS ticket was requested|WIN2008R2$|
|ticket_options|string|this is a set of different ticket flags in hexadecimal format.|0x40810010|
|ticket_status|string|hexadecimal result code of TGS issue operation.|0x0|
|ticket_encryption_type|string|the cryptographic suite that was used for issued TGS.|0x12|