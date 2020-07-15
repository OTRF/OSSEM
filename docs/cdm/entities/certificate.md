# certificate

This document is a work in progress, but is a foundational. Specifically the main foundations of certificate information is already in here.

## Attributes

| Name | Type | Description | Sample Value |
|:---|:---|:---|:---|
 | certificate_hash_imphash | string | IMPHASH hash of the image/binary/file | ```2505BD03D7BD285E50CE89CEC02B333B``` |
 | certificate_hash_md5 | string | MD5 hash of the image/binary/file | ```6A255BEBF3DBCD13585538ED47DBAFD7``` |
 | certificate_hash_sha1 | string | SHA1 hash of the image/binary/file | ```B0BF5AC2E81BBF597FAD5F349FEEB32CAC449FA2``` |
 | certificate_hash_sha256 | string | SHA256 hash of the image/binary/file | ```4668BB2223FFB983A5F1273B9E3D9FA2C5CE4A0F1FB18CA5C1B285762020073C``` |
 | certificate_hash_sha512 | string | SHA512 hash of the image/binary/file | ```1AD1D79F85D8F6A50EA282F63898D652661DAA0C1FD361C22647CABC98A70E8CBCE83200D579D10DD0A3D46BE9496DCDFDDF28B0C5E9709343B032A8796FBECB``` |
 | certificate_issuer | string | Information about the CA that issued the certificate | ```CN=neu5ron.local,OU=Admin``` |
 | certificate_serial_number | string | Serial number, this is chosen by the CA (certificate authority) which issued the certificate. Therefore this can relatively be arbritary if the CA does not follow a standard or is malicious. | ```5157550``` |
 | certificate_subject | string | Information about the CA that issued the certificate | ```CN=natetoken,OU=Admin,DC=neu5ron,DC=local``` |
