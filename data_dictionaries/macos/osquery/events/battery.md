# Battery Table

## Description
Provides information about the internal battery of a Macbook.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|manufacturer|TEXT|The battery manufacturer's name|`TBD`|
|TBD|manufacture_date|INTEGER|The date the battery was manufactured UNIX Epoch|`TBD`|
|TBD|model|TEXT|The battery's model number|`TBD`|
|TBD|serial_number|TEXT|The battery's unique serial number|`TBD`|
|TBD|cycle_count|INTEGER|The number of charge/discharge cycles|`TBD`|
|TBD|health|TEXT|One of the following: \|`TBD`|
|TBD|condition|TEXT|One of the following: \|`TBD`|
|TBD|state|TEXT|One of the following: \|`TBD`|
|TBD|charging|INTEGER|1 if the battery is currently being charged by a power source. 0 otherwise|`TBD`|
|TBD|charged|INTEGER|1 if the battery is currently completely charged. 0 otherwise|`TBD`|
|TBD|designed_capacity|INTEGER|The battery's designed capacity in mAh|`TBD`|
|TBD|max_capacity|INTEGER|The battery's actual capacity when it is fully charged in mAh|`TBD`|
|TBD|current_capacity|INTEGER|The battery's current charged capacity in mAh|`TBD`|
|TBD|percent_remaining|INTEGER|The percentage of battery remaining before it is drained|`TBD`|
|TBD|amperage|INTEGER|The battery's current amperage in mA|`TBD`|
|TBD|voltage|INTEGER|The battery's current voltage in mV|`TBD`|
|TBD|minutes_until_empty|INTEGER|The number of minutes until the battery is fully depleted. This value is -1 if this time is still being calculated|`TBD`|
|TBD|minutes_to_full_charge|INTEGER|The number of minutes until the battery is fully charged. This value is -1 if this time is still being calculated|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#battery)

## Tags
* version_4.4.2