# Preferences Table

## Description
OS X defaults and managed preferences.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|domain|TEXT|Application ID usually in com.name.product format|`TBD`|
|TBD|key|TEXT|Preference top-level key|`TBD`|
|TBD|subkey|TEXT|Intemediate key path, includes lists/dicts|`TBD`|
|TBD|value|TEXT|String value of most CF types|`TBD`|
|TBD|forced|INTEGER|1 if the value is forced/managed, else 0|`TBD`|
|TBD|username|TEXT|(optional) read preferences for a specific user|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#preferences)

## Tags
* version_4.4.2