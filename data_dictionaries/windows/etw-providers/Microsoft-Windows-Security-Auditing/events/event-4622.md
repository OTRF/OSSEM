# Event ID 4622: A security package has been loaded by the Local Security Authority.

## Description
Event ID 4622: A security package has been loaded by the Local Security Authority.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|logon_security_package_name|SecurityPackageName|UnicodeString|the name of loaded Security Package. The format is: DLL_PATH_AND_NAME: SECURITY_PACKAGE_NAME.|`C:\Windows\system32\kerberos.DLL : Kerberos`|

## References
* [MS SOURCE](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4622.md)
* [MS Security Auditing Category - System](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#system)
* [MS Security Auditing Sub-category - Audit Security System Extension](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-security-system-extension.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* System
* Audit Security System Extension