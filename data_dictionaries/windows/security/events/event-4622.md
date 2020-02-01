# Event ID 4622: A security package has been loaded by the Local Security Authority.

## Description

This event generates every time Security Package has been loaded by the Local Security Authority (LSA).

Security Package is the software implementation of a security protocol (Kerberos, NTLM, for example). Security packages are contained in security support provider DLLs or security support provider/authentication package DLLs.

Each time the system starts, the LSA loads the Security Package DLLs from HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa\OSConfig\Security Packages registry value and performs the initialization sequence for every package located in these DLLs.

It is also possible to add security package dynamically using AddSecurityPackage function, not only during system startup process.

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4622.md)

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|logon_security_package_name|SecurityPackageName|string|the name of loaded Security Package. The format is: DLL_PATH_AND_NAME: SECURITY_PACKAGE_NAME.|C:\\Windows\\system32\\kerberos.DLL : Kerberos|