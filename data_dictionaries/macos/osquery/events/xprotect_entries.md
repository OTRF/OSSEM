# Xprotect_entries Table

## Description
Database of the machine's XProtect signatures.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|name|TEXT|Description of XProtected malware|`TBD`|
|TBD|launch_type|TEXT|Launch services content type|`TBD`|
|TBD|identity|TEXT|XProtect identity (SHA1) of content|`TBD`|
|TBD|filename|TEXT|Use this file name to match|`TBD`|
|TBD|filetype|TEXT|Use this file type to match|`TBD`|
|TBD|optional|INTEGER|Match any of the identities/patterns for this XProtect name|`TBD`|
|TBD|uses_pattern|INTEGER|Uses a match pattern instead of identity|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#xprotect_entries)

## Tags
* version_4.4.2