# Account_policy_data Table
###### Version: 4.4.2

## Description
Additional OS X user account data from the AccountPolicy section of OpenDirectory.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|uid|BIGINT|User ID|`TBD`|
|TBD|creation_time|DOUBLE|When the account was first created|`TBD`|
|TBD|failed_login_count|BIGINT|The number of times the user failed to login with the correct password. Resets after a correct password is entered|`TBD`|
|TBD|failed_login_timestamp|DOUBLE|The time of the last failed login attempt. Resets after a correct password is entered|`TBD`|
|TBD|password_last_set_time|DOUBLE|The time the password was last changed|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#account_policy_data)
