# Event ID 6423: The installation of this device is forbidden by system policy.

## Description

This event generates every time installation of this device is forbidden by system policy.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|string|SID of account that forbids the device installation.|S-1-5-18|
|user_name|SubjectUserName|string|the name of the account that forbids the device installation.|DESKTOP-NFC0HVN$|
|user_domain|SubjectDomainName|string|subject's domain or computer name.|WORKGROUP|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x3e7|
|device_id|DeviceId|string|"Device instance path" attribute of device.|USB\\VID\_04F3&PID\_012D\\7&1E3A8971&0&2|
|device_description|DeviceDescription|string|"Device description" attribute of device.|Touchscreen|
|class_id|ClassId|string|"Class Guid" attribute of device.|{00000000-0000-0000-0000-000000000000}|
|class_name|ClassName|string|"Class" attribute of device.|None|
|hardware_ids|HardwareIds|string|"Hardware Ids" attribute of device.|USB\\VID\_04F3&PID\_012D&REV\_0013 USB\\VID\_04F3&PID\_012D|
|compatible_ids|CompatibleIds|string|"Compatible Ids" attribute of device.|USB\\Class\_03&SubClass\_00&Prot\_00 USB\\Class\_03&SubClass\_00 USB\\Class\_03|
|location_information|LocationInformation|string|"Location information" attribute of device.|Port\_\#0002.Hub\_\#0004|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-6423.md)