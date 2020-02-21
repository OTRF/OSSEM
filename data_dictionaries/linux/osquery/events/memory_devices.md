# Memory_devices Table

## Description
Physical memory device (type 17) information retrieved from SMBIOS.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|handle| TEXT|Handle, or instance number, associated with the structure in SMBIOS|`TBD`|
|TBD|array_handle| TEXT|The memory array that the device is attached to|`TBD`|
|TBD|form_factor|TEXT|Implementation form factor for this memory device|`TBD`|
|TBD|total_width|INTEGER|Total width, in bits, of this memory device, including any check or error-correction bits|`TBD`|
|TBD|data_width|INTEGER|Data width, in bits, of this memory device|`TBD`|
|TBD|size|INTEGER|Size of memory device in Megabyte|`TBD`|
|TBD|set|INTEGER|Identifies if memory device is one of a set of devices.  A value of 0 indicates no set affiliation.|`TBD`|
|TBD|device_locator|TEXT|String number of the string that identifies the physically-labeled socket or board position where the memory device is located|`TBD`|
|TBD|bank_locator|TEXT|String number of the string that identifies the physically-labeled bank where the memory device is located|`TBD`|
|TBD|memory_type|TEXT|Type of memory used|`TBD`|
|TBD|memory_type_details|TEXT|Additional details for memory device|`TBD`|
|TBD|max_speed|INTEGER|Max speed of memory device in megatransfers per second (MT/s)|`TBD`|
|TBD|configured_clock_speed|INTEGER|Configured speed of memory device in megatransfers per second (MT/s)|`TBD`|
|TBD|manufacturer|TEXT|Manufacturer ID string|`TBD`|
|TBD|serial_number|TEXT|Serial number of memory device|`TBD`|
|TBD|asset_tag|TEXT|Manufacturer specific asset tag of memory device|`TBD`|
|TBD|part_number|TEXT|Manufacturer specific serial number of memory device|`TBD`|
|TBD|min_voltage|INTEGER|Minimum operating voltage of device in millivolts|`TBD`|
|TBD|max_voltage|INTEGER|Maximum operating voltage of device in millivolts|`TBD`|
|TBD|configured_voltage|INTEGER|Configured operating voltage of device in millivolts|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#memory_devices)

## Tags
* version_4.4.2