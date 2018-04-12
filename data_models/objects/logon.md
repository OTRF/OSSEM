# Logon Object

## Data Fields

| field name | field type | description |
|--------|---------|-------|
| logon_type | string | the type of logon which was performed by the user while authenticating to a box |
| logon_authentication_package | string | The name of the authentication package which was used for the authentication process |
| logon_transmitted_services | string | List of transmitted services. Transmitted services are populated if the logon was a result of a S4U (Service For User) logon process |
| logon_package_name | string | TThe name of the LAN Manager sub-package (NTLM-family protocol name) that was used during logon |
| logon_key_length | string | the length of NTLM Session Security key. Typically it has 128 bit or 56 bit length. This parameter is always 0 if “Authentication Package” = “Kerberos”, because it is not applicable for Kerberos protocol |