# Event ID 4610: An authentication package has been loaded by the Local Security Authority.

## Description

This event generates every time Authentication Package has been loaded by the Local Security Authority (LSA).

Each time the system starts, the LSA loads the Authentication Package DLLs from HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa\Authentication Packages registry value and performs the initialization sequence for every package located in these DLLs.

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4610.md)

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|logon_authentication_package_name|AuthenticationPackageName|string|the name of loaded Authentication Package. The format is: DLL_PATH_AND_NAME: AUTHENTICATION_PACKAGE_NAME.|C:\\Windows\\system32\\msv1\_0.DLL : MICROSOFT\_AUTHENTICATION\_PACKAGE\_V1\_0|