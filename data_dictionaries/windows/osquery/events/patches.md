# Patches Table
###### Version: 4.4.2

## Description
Lists all the patches applied. Note: This does not include patches applied via MSI or downloaded from Windows Update (e.g. Service Packs).

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|csname|TEXT|The name of the host the patch is installed on.|`TBD`|
|TBD|hotfix_id|TEXT|The KB ID of the patch.|`TBD`|
|TBD|caption|TEXT|Short description of the patch.|`TBD`|
|TBD|description|TEXT|Fuller description of the patch.|`TBD`|
|TBD|fix_comments|TEXT|Additional comments about the patch.|`TBD`|
|TBD|installed_by|TEXT|The system context in which the patch as installed.|`TBD`|
|TBD|install_date|TEXT|Indicates when the patch was installed. Lack of a value does not indicate that the patch was not installed.|`TBD`|
|TBD|installed_on|TEXT|The date when the patch was installed.|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#patches)
