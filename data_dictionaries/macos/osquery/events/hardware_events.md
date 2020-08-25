# Hardware_events Table
###### Version: 4.4.2

## Description
Hardware (PCI/USB/HID) events from UDEV or IOKit.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|action|TEXT|Remove, insert, change properties, etc|`TBD`|
|TBD|path|TEXT|Local device path assigned (optional)|`TBD`|
|TBD|type|TEXT|Type of hardware and hardware event|`TBD`|
|TBD|driver|TEXT|Driver claiming the device|`TBD`|
|TBD|vendor|TEXT|Hardware device vendor|`TBD`|
|TBD|vendor_id|TEXT|Hex encoded Hardware vendor identifier|`TBD`|
|TBD|model|TEXT|Hardware device model|`TBD`|
|TBD|model_id|TEXT|Hex encoded Hardware model identifier|`TBD`|
|TBD|serial|TEXT|Device serial (optional)|`TBD`|
|TBD|revision|TEXT|Device revision (optional)|`TBD`|
|TBD|time|BIGINT|Time of hardware event|`TBD`|
|TBD|eid|TEXT|Event ID|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#hardware_events)
