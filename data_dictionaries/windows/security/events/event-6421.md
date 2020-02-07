# Event ID 6421: A request was made to enable a device.

## Description
This event generates every time when someone made a request to enable a device.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|TBD|string|"Location information" attribute of device.|S-1-5-21-2695983153-1310895815-1903476278-1001|
|user_name|SubjectUserName|TBD|string|the name of the account that made the request.|ladmin|
|user_domain|SubjectDomainName|TBD|string|subject's domain or computer name.|DESKTOP-NFC0HVN|
|user_logon_id|SubjectLogonId|TBD|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x3fcc7|
|device_id|DeviceId|TBD|string|"Device instance path" attribute of device.|USB\VID_138A&PID_0017\FFBC12C950A0|
|device_description|DeviceDescription|TBD|string|"Device description" attribute of device.|Synaptics FP Sensors (WBF) (PID=0017)|
|class_id|ClassId|TBD|string|"Class Guid" attribute of device.|{53D29EF7-377C-4D14-864B-EB3A85769359}|
|class_name|ClassName|TBD|string|"Class" attribute of device.|Biometric|
|hardware_ids|HardwareIds|TBD|string|"Hardware Ids" attribute of device.|USB\VID_138A&PID_0017&REV_0078 USB\VID_138A&PID_0017|
|compatible_ids|CompatibleIds|TBD|string|"Compatible Ids" attribute of device.|USB\Class_FF&SubClass_00&Prot_00 USB\Class_FF&SubClass_00 USB\Class_FF|
|location_information|LocationInformation|TBD|string|"Location information" attribute of device.|Port#0002.Hub#0004|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-6421.md)
* [MS Security Auditing Category - Detailed Tracking](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#detailed-tracking)
* [MS Security Auditing Sub-category - Audit PNP Activity](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-pnp-activity.md)

## Tags
* Detailed Tracking
* Audit PNP Activity