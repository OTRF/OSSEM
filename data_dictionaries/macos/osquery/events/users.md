# Users Table
###### Version: 4.4.2

## Description
Local user accounts (including domain accounts that have logged on locally (Windows)).

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|uid|BIGINT|User ID|`TBD`|
|TBD|gid|BIGINT|Group ID (unsigned)|`TBD`|
|TBD|uid_signed|BIGINT|User ID as int64 signed (Apple)|`TBD`|
|TBD|gid_signed|BIGINT|Default group ID as int64 signed (Apple)|`TBD`|
|TBD|username|TEXT|Username|`TBD`|
|TBD|description|TEXT|Optional user description|`TBD`|
|TBD|directory|TEXT|User's home directory|`TBD`|
|TBD|shell|TEXT|User's configured default shell|`TBD`|
|TBD|uuid|TEXT|User's UUID (Apple) or SID (Windows)|`TBD`|
|TBD|type|TEXT|Whether the account is roaming (domain), local, or a system profile [WINDOWS]|`TBD`|
|TBD|is_hidden|INTEGER|IsHidden attribute set in OpenDirectory [DARWIN]|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#users)
