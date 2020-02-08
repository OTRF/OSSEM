# Event ID 4614: A notification package has been loaded by the Security Account Manager.

## Description
This event generates every time a Notification Package has been loaded by the Security Account Manager.
In reality, starting with Windows Vista, a notification package should be interpreted as afs Password Filter.
Password Filters are DLLs that are loaded or called when passwords are set or changed.
Each time a system starts, it loads the notification package DLLs from HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa\Notification Packages registry value and performs the initialization sequence for every package.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|logon_notification_package_name|NotificationPackageName|string|the name of loaded Notification Package.|`WDIGEST`|

## References
* [MS SOURCE](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4614.md)
* [MS Security Auditing Category - System](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#system)
* [MS Security Auditing Sub-category - Audit Security System Extension](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-security-system-extension.md)

## Tags
* System
* Audit Security System Extension