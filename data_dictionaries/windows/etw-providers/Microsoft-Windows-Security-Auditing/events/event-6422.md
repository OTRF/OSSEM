# Event ID 6422: A device was enabled.

## Description
This event generates every time specific device was enabled.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account that enabled the device.|`S-1-5-18`|
|user_name|SubjectUserName|UnicodeString|the name of the account that enabled the device.|`DESKTOP-NFC0HVN$`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`WORKGROUP`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x3e7`|
|device_id|DeviceId|UnicodeString|"Device instance path" attribute of device.|`USB\VID_138A&PID_0017\ffbc12c950a0`|
|device_description|DeviceDescription|UnicodeString|"Device description" attribute of device.|`Synaptics FP Sensors (WBF) (PID=0017)`|
|class_id|ClassId|GUID|"Class Guid" attribute of device.|`{53D29EF7-377C-4D14-864B-EB3A85769359}`|
|class_name|ClassName|UnicodeString|"Class" attribute of device.|`Biometric`|
|hardware_ids|HardwareIds|UnicodeString|"Hardware Ids" attribute of device.|`USB\VID_138A&PID_0017&REV_0078 USB\VID_138A&PID_0017`|
|compatible_ids|CompatibleIds|UnicodeString|"Compatible Ids" attribute of device.|`USB\Class_FF&SubClass_00&Prot_00 USB\Class_FF&SubClass_00 USB\Class_FF`|
|location_information|LocationInformation|UnicodeString|"Location information" attribute of device.|`Port#0002.Hub#0004`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-6422.md)
* [MS Security Auditing Category - Detailed Tracking](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#detailed-tracking)
* [MS Security Auditing Sub-category - Audit PNP Activity](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-pnp-activity.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Detailed Tracking
* Audit PNP Activity