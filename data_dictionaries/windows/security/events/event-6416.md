# Event ID 6416: A new external device was recognized by the System.

## Description
This event generates every time a new external device is recognized by a system.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|TBD|string|SID of account that registered the new device.|S-1-5-18|
|user_name|SubjectUserName|TBD|string|the name of the account that registered the new device.|DESKTOP-NFC0HVN$|
|user_domain|SubjectDomainName|TBD|string|subject's domain or computer name.|WORKGROUP|
|user_logon_id|SubjectLogonId|TBD|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x3e7|
|device_id|DeviceId|TBD|string|"Device instance path" attribute of device.|SCSI\Disk&Ven_Seagate&Prod_Expansion\000000|
|device_description|DeviceDescription|TBD|string|"Device description" attribute of device.|Seagate Expansion SCSI Disk Device|
|class_id|ClassId|TBD|string|"Class Guid" attribute of device.|{4D36E967-E325-11CE-BFC1-08002BE10318}|
|class_name|ClassName|TBD|string|"Class" attribute of device.|DiskDrive|
|vendor_ids|VendorIds|TBD|string|"Hardware Ids" attribute of device.|SCSI\DiskSeagate_Expansion___0636 SCSI\DiskSeagateExpansion__ SCSI\DiskSeagate_ SCSI\Seagate_Expansion___0 Seagate_Expansion___0 GenDisk|
|compatible_ids|CompatibleIds|TBD|string|"Compatible Ids" attribute of device.|SCSI\Disk SCSI\RAW|
|location_information|LocationInformation|TBD|string|"Location information" attribute of device.|Bus Number 0, Target Id 0, LUN 0|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-6416.md)
* [MS Security Auditing Category - Detailed Tracking](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#detailed-tracking)
* [MS Security Auditing Sub-category - Audit PNP Activity](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-pnp-activity.md)

## Tags
* Detailed Tracking
* Audit PNP Activity