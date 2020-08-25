# User_ssh_keys Table
###### Version: 4.4.2

## Description
Returns the private keys in the users ~/.ssh directory and whether or not they are encrypted.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|uid|BIGINT|The local user that owns the key file|`TBD`|
|TBD|path|TEXT|Path to key file|`TBD`|
|TBD|encrypted|INTEGER|1 if key is encrypted, 0 otherwise|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#user_ssh_keys)
