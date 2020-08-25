# Portage_packages Table
###### Version: 4.4.2

## Description
List of currently installed packages.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|package|TEXT|Package name|`TBD`|
|TBD|version|TEXT|The version which are affected by the use flags, empty means all|`TBD`|
|TBD|slot|TEXT|The slot used by package|`TBD`|
|TBD|build_time|BIGINT|Unix time when package was built|`TBD`|
|TBD|repository|TEXT|From which repository the ebuild was used|`TBD`|
|TBD|eapi|BIGINT|The eapi for the ebuild|`TBD`|
|TBD|size|BIGINT|The size of the package|`TBD`|
|TBD|world|INTEGER|If package is in the world file|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#portage_packages)
