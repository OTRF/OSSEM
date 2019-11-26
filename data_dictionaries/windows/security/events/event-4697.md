# Event ID 4697: A service was installed in the system

## Description

This event generates when new service was installed in the system.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|----------------|----------------|----------------|----------------|----------------|
|user_sid|SubjectUserSid|string|SID of account that was used to install the service.|S-1-5-18|
|user_name|SubjectUserName|string|the name of the account that was used to install the service.|WIN-GG82ULGC9GO$|
|user_domain|SubjectDomainName|string|subject’s domain or computer name. |DOMAIN|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|0x3e7|
|service_account|ServiceAccount|string|The security context that the service will run as when started.|localSystem|
|service_path|ServiceFileName|string|This is the fully rooted path to the file that the Service Control Manager will execute to start the service.|%windir%\\system32\\svchost.exe -k apphost|
|service_name|ServiceName|string|the name of installed service.|AppHostSvc|
|service_start_type|ServiceStartType|integer|The service start type can have one of the following values (see: https://msdn.microsoft.com/library/windows/desktop/ms682450(v=vs.85).aspx)|2|
|service_type|ServiceType|integer|Indicates the type of service that was registered with the Service Control Manager.|0x20|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4697.md)