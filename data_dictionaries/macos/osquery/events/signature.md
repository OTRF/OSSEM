# Signature Table
###### Version: 4.4.2

## Description
File (executable, bundle, installer, disk) code signing status.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|path|TEXT|Must provide a path or directory|`TBD`|
|TBD|arch|TEXT|If applicable, the arch of the signed code|`TBD`|
|TBD|signed|INTEGER|1 If the file is signed else 0|`TBD`|
|TBD|identifier|TEXT|The signing identifier sealed into the signature|`TBD`|
|TBD|cdhash|TEXT|Hash of the application Code Directory|`TBD`|
|TBD|team_identifier|TEXT|The team signing identifier sealed into the signature|`TBD`|
|TBD|authority|TEXT|Certificate Common Name|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#signature)
