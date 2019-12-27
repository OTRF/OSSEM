# Event ID 6416: A new external device was recognized by the System.

## Description

This event generates every time a new external device is recognized by a system.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|string|SID of account that registered the new device.|S-1-5-18|
|user_name|SubjectUserName|string|the name of the account that registered the new device.|DESKTOP-NFC0HVN$|
|user_domain|SubjectDomainName|string|subject's domain or computer name.|WORKGROUP|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x3e7|
|device_id|DeviceId|string|"Device instance path" attribute of device.|SCSI\\Disk&Ven\_Seagate&Prod\_Expansion\\000000|
|device_description|DeviceDescription|string|"Device description" attribute of device.|Seagate Expansion SCSI Disk Device|
|class_id|ClassId|string|"Class Guid" attribute of device.|{4D36E967-E325-11CE-BFC1-08002BE10318}|
|class_name|ClassName|string|"Class" attribute of device.|DiskDrive|
|vendor_ids|VendorIds|string|"Hardware Ids" attribute of device.|SCSI\\DiskSeagate\_Expansion\_\_\_\_\_\_\_0636 SCSI\\DiskSeagate\_Expansion\_\_\_\_\_\_\_ SCSI\\DiskSeagate\_ SCSI\\Seagate\_Expansion\_\_\_\_\_\_\_0 Seagate\_Expansion\_\_\_\_\_\_\_0 GenDisk|
|compatible_ids|CompatibleIds|string|"Compatible Ids" attribute of device.|SCSI\\Disk SCSI\\RAW|
|location_information|LocationInformation|string|"Location information" attribute of device.|Bus Number 0, Target Id 0, LUN 0|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-6416.md)