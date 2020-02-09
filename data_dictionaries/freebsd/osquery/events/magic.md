# Magic Table

## Description
Magic number recognition library table.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|path|TEXT|Absolute path to target file|`TBD`|
|TBD|magic_db_files|TEXT|Colon(:) separated list of files where the magic db file can be found. By default one of the following is used: /usr/share/file/magic/magic, /usr/share/misc/magic or /usr/share/misc/magic.mgc|`TBD`|
|TBD|data|TEXT|Magic number data from libmagic|`TBD`|
|TBD|mime_type|TEXT|MIME type data from libmagic|`TBD`|
|TBD|mime_encoding|TEXT|MIME encoding data from libmagic|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#magic)

## Tags
* version_4.4.2