# Event ID 6421: A request was made to enable a device.

## Description

This event generates every time when someone made a request to enable a device.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|string|"Location information" attribute of device.|S-1-5-21-2695983153-1310895815-1903476278-1001|
|user_name|SubjectUserName|string|the name of the account that made the request.|ladmin|
|user_domain|SubjectDomainName|string|subject's domain or computer name.|DESKTOP-NFC0HVN|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x3fcc7|
|device_id|DeviceId|string|"Device instance path" attribute of device.|USB\\VID\_138A&PID\_0017\\FFBC12C950A0|
|device_description|DeviceDescription|string|"Device description" attribute of device.|Synaptics FP Sensors (WBF) (PID=0017)|
|class_id|ClassId|string|"Class Guid" attribute of device.|{53D29EF7-377C-4D14-864B-EB3A85769359}|
|class_name|ClassName|string|"Class" attribute of device.|Biometric|
|hardware_ids|HardwareIds|string|"Hardware Ids" attribute of device.|USB\\VID\_138A&PID\_0017&REV\_0078 USB\\VID\_138A&PID\_0017|
|compatible_ids|CompatibleIds|string|"Compatible Ids" attribute of device.|USB\\Class\_FF&SubClass\_00&Prot\_00 USB\\Class\_FF&SubClass\_00 USB\\Class\_FF|
|location_information|LocationInformation|string|"Location information" attribute of device.|Port\_\#0002.Hub\_\#0004|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-6421.md)