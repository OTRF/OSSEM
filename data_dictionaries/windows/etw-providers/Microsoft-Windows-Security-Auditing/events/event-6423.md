# Event ID 6423: The installation of this device is forbidden by system policy.

## Description
This event generates every time installation of this device is forbidden by system policy.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account that forbids the device installation.|`S-1-5-18`|
|user_name|SubjectUserName|UnicodeString|the name of the account that forbids the device installation.|`DESKTOP-NFC0HVN$`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`WORKGROUP`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x3e7`|
|device_id|DeviceId|UnicodeString|"Device instance path" attribute of device.|`USB\VID_04F3&PID_012D\7&1E3A8971&0&2`|
|device_description|DeviceDescription|UnicodeString|"Device description" attribute of device.|`Touchscreen`|
|class_id|ClassId|GUID|"Class Guid" attribute of device.|`{00000000-0000-0000-0000-000000000000}`|
|class_name|ClassName|UnicodeString|"Class" attribute of device.|`None`|
|hardware_ids|HardwareIds|UnicodeString|"Hardware Ids" attribute of device.|`USB\VID_04F3&PID_012D&REV_0013 USB\VID_04F3&PID_012D`|
|compatible_ids|CompatibleIds|UnicodeString|"Compatible Ids" attribute of device.|`USB\Class_03&SubClass_00&Prot_00 USB\Class_03&SubClass_00 USB\Class_03`|
|location_information|LocationInformation|UnicodeString|"Location information" attribute of device.|`Port#0002.Hub#0004`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-6423.md)
* [MS Security Auditing Category - Detailed Tracking](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#detailed-tracking)
* [MS Security Auditing Sub-category - Audit PNP Activity](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-pnp-activity.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Detailed Tracking
* Audit PNP Activity