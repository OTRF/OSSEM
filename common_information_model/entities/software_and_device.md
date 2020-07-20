# Software and Device Entity
Information about software or a (build) device and operating system. There are many similar information between and device and operating system and software that these will be kept in one general entity.

## Data Fields
|Standard Name|Type|Description|Sample Value|
|---|---|---|---|
| hash_software_checksum|string|The hash to verify software/package||
| software_additional|string|remaining/extra/additional values||
| software_architecture|string|CPU architecture, here is a list of examples (seperated by ";"|"arm";"amd64";"x64";"64bit";"32bit";"8bit";"mips"|
| software_build|string|| `|
| software_device_license_number|string|License number for the device. This would be something that is renewed/yearly/based-on-a-date/time aka based on a subscription. Versus a serial number which is burned/built in.||
| software_device_model_number|string|Hardware model number||
| software_device_name|string|short version of the device hardware name|"cisco";"paloalto"|
| software_device_name_original|string|original/entire/full unaltered/unedited value from the event||
| software_device_product_id|string|Hardware Version/Product ID|"asa5252";"direct2500"|
| software_device_serial_number|string|Hardware serial number. Sometimes this and the license number are used in similar meaning.||
| software_device_vendor|string|Hardware vendor/manufactuer of the device|Dell|
| software_license_number|string|License number for the software. This would be something that is renewed/yearly/based-on-a-date/time aka based on a subscription.||
| software_name|string|the short version of the software|"flash";"java"|
| software_name_original|string|the original/entire/full unaltered/unedited value from the event||
| software_os_additional|string|info for an OS. commonly from a user agent value||
| software_os_architecture|string|info for an OS. commonly from a user agent value|x64|
| software_os_build|string|info for an OS. commonly from a user agent value||
| software_os_name|string|info for an OS. commonly from a user agent value|"mac os x"|
| software_os_name_original|string|info for an OS. commonly from a user agent value|Mac OS X 10.6.8|
| software_os_patch|string|info for an OS. commonly from a user agent value||
| software_os_version_additional|string|info for an OS. commonly from a user agent value||
| software_os_version_full|string|info for an OS. commonly from a user agent value|10.6.8|
| software_os_version_major|string|info for an OS. commonly from a user agent value|10|
| software_os_version_minor1|string|info for an OS. commonly from a user agent value|6|
| software_os_version_minor2|string|info for an OS. commonly from a user agent value|8|
| software_os_version_minor3|string|info for an OS. commonly from a user agent value||
| software_os_version_minor4|string|info for an OS. commonly from a user agent value||
| software_patch|string|| `|
| software_vendor|string|vendor/manufactuer of the software|Adobe|
| software_version_additional|string|remaining/extra/additional values||
| software_version_full|string|(all) the full version numbers|10.6.4.1.5|
| software_version_major|string|the 1st/most version number|10|
| software_version_minor1|string|the 1st/most minor version number, if applicable, technically the 2nd value.|6|
| software_version_minor2|string|the 2nd minor version number, if applicable, technically the 3rd value.|4|
| software_version_minor3|string|the 3rd minor version number, if applicable, technically the 4th value.|1|
| software_version_minor4|string|the 4th minor version number, if applicable, technically the 5th value.|5|
