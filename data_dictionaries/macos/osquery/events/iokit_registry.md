# Iokit_registry Table
###### Version: 4.4.2

## Description
The full IOKit registry without selecting a plane.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|name|TEXT|Default name of the node|`TBD`|
|TBD|class|TEXT|Best matching device class (most-specific category)|`TBD`|
|TBD|id|BIGINT|IOKit internal registry ID|`TBD`|
|TBD|parent|BIGINT|Parent registry ID|`TBD`|
|TBD|busy_state|INTEGER|1 if the node is in a busy state else 0|`TBD`|
|TBD|retain_count|INTEGER|The node reference count|`TBD`|
|TBD|depth|INTEGER|Node nested depth|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#iokit_registry)
