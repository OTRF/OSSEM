# Iokit_devicetree Table

## Description
The IOKit registry matching the DeviceTree plane.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|name|TEXT|Device node name|`TBD`|
|TBD|class|TEXT|Best matching device class (most-specific category)|`TBD`|
|TBD|id|BIGINT|IOKit internal registry ID|`TBD`|
|TBD|parent|BIGINT|Parent device registry ID|`TBD`|
|TBD|device_path|TEXT|Device tree path|`TBD`|
|TBD|service|INTEGER|1 if the device conforms to IOService else 0|`TBD`|
|TBD|busy_state|INTEGER|1 if the device is in a busy state else 0|`TBD`|
|TBD|retain_count|INTEGER|The device reference count|`TBD`|
|TBD|depth|INTEGER|Device nested depth|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#iokit_devicetree)

## Tags
* version_4.4.2