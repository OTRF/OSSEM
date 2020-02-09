# Certificates Table

## Description
Certificate Authorities installed in Keychains/ca-bundles.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|common_name|TEXT|Certificate CommonName|`TBD`|
|TBD|subject|TEXT|Certificate distinguished name|`TBD`|
|TBD|issuer|TEXT|Certificate issuer distinguished name|`TBD`|
|TBD|ca|INTEGER|1 if CA: true (certificate is an authority) else 0|`TBD`|
|TBD|self_signed|INTEGER|1 if self-signed, else 0|`TBD`|
|TBD|not_valid_before|DATETIME|Lower bound of valid date|`TBD`|
|TBD|not_valid_after|DATETIME|Certificate expiration data|`TBD`|
|TBD|signing_algorithm|TEXT|Signing algorithm used|`TBD`|
|TBD|key_algorithm|TEXT|Key algorithm used|`TBD`|
|TBD|key_strength|TEXT|Key size used for RSA/DSA, or curve name|`TBD`|
|TBD|key_usage|TEXT|Certificate key usage and extended key usage|`TBD`|
|TBD|subject_key_id|TEXT|SKID an optionally included SHA1|`TBD`|
|TBD|authority_key_id|TEXT|AKID an optionally included SHA1|`TBD`|
|TBD|sha1|TEXT|SHA1 hash of the raw certificate contents|`TBD`|
|TBD|path|TEXT|Path to Keychain or PEM bundle|`TBD`|
|TBD|serial|TEXT|Certificate serial number|`TBD`|
|TBD|sid|TEXT|SID [WINDOWS]|`TBD`|
|TBD|store_location|TEXT|Certificate system store location [WINDOWS]|`TBD`|
|TBD|store|TEXT|Certificate system store [WINDOWS]|`TBD`|
|TBD|username|TEXT|Username [WINDOWS]|`TBD`|
|TBD|store_id|TEXT|Exists for service/user stores. Contains raw store id provided by WinAPI. [WINDOWS]|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#certificates)

## Tags
* version_4.4.2