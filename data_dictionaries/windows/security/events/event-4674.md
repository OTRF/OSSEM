# Event ID 4674: An operation was attempted on a privileged object.

## Description

This event generates when an attempt is made to perform privileged operations on a protected subsystem object after the object is already opened.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|string|SID of account that requested privileged operation.|S-1-5-19|
|user_name|SubjectUserName|string|the name of the account that requested privileged operation.|LOCAL SERVICE|
|user_domain|SubjectDomainName|string|subject's domain or computer name.|NT AUTHORITY|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x3e5|
|object_server|ObjectServer|string|Contains the name of the Windows subsystem calling the routine.|LSA|
|object_type|ObjectType|string|Contains the name of the Windows subsystem calling the routine.|-|
|object_name|ObjectName|string|the name of the object that was accessed during the operation.|-|
|object_handle_id|HandleId|integer|hexadecimal value of a handle to Object Name. This field can help you correlate this event with other events that might contain the same Handle ID, for example, “4656: A handle to an object was requested” event in appropriate/other subcategory.|0x0|
|object_access_mask|AccessMask|integer|The desired access mask. This mask depends on Object Server and Object Type parameters values.|16777216|
|object_privilege_list|PrivilegeList|string|the list of user privileges which were requested.|SeSecurityPrivilege|
|process_id|ProcessId|integer|hexadecimal Process ID of the process that attempted the operation on the privileged object.|0x1f0|
|process_path|ProcessName|string|full path and the name of the executable for the process.|C:\\Windows\\System32\\lsass.exe|

## Reference

[MS SOURCE](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4674.md)