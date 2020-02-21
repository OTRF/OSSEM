# Bitlocker_info Table

## Description
Retrieve bitlocker status of the machine.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|device_id|TEXT|ID of the encrypted drive.|`TBD`|
|TBD|drive_letter|TEXT|Drive letter of the encrypted drive.|`TBD`|
|TBD|persistent_volume_id|TEXT|Persistent ID of the drive.|`TBD`|
|TBD|conversion_status|INTEGER|The bitlocker conversion status of the drive.|`TBD`|
|TBD|protection_status|INTEGER|The bitlocker protection status of the drive.|`TBD`|
|TBD|encryption_method|TEXT|The encryption type of the device.|`TBD`|
|TBD|version|INTEGER|The FVE metadata version of the drive.|`TBD`|
|TBD|percentage_encrypted|INTEGER|The percentage of the drive that is encrypted.|`TBD`|
|TBD|lock_status|INTEGER|The accessibility status of the drive from Windows.|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#bitlocker_info)

## Tags
* version_4.4.2