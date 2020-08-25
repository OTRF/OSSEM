# Shadow Table
###### Version: 4.4.2

## Description
Local system users encrypted passwords and related information. Please note, that you usually need superuser rights to access `/etc/shadow`.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|password_status|TEXT|Password status|`TBD`|
|TBD|hash_alg|TEXT|Password hashing algorithm|`TBD`|
|TBD|last_change|BIGINT|Date of last password change (starting from UNIX epoch date)|`TBD`|
|TBD|min|BIGINT|Minimal number of days between password changes|`TBD`|
|TBD|max|BIGINT|Maximum number of days between password changes|`TBD`|
|TBD|warning|BIGINT|Number of days before password expires to warn user about it|`TBD`|
|TBD|inactive|BIGINT|Number of days after password expires until account is blocked|`TBD`|
|TBD|expire|BIGINT|Number of days since UNIX epoch date until account is disabled|`TBD`|
|TBD|flag|BIGINT|Reserved|`TBD`|
|TBD|username|TEXT|Username|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#shadow)
