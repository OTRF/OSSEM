# Event ID 4673: A privileged service was called

## Description

This event generates when an attempt was made to perform privileged system service operations. This event generates, for example, when SeSystemtimePrivilege, SeCreateGlobalPrivilege, or SeTcbPrivilege privilege was used.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|----------------|----------------|----------------|----------------|----------------|
|user_sid|SubjectUserSid|string|SID of account that requested privileged operation.|ORG\UserA|
|user_name|SubjectUserName|strin|the name of the account that requested privileged operation.|UserA|
|user_domain|SubjectDomainName|string|subject’s domain or computer name.|ORG|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|0x432344|
|process_id|ProcessId|integer|hexadecimal Process ID of the process that attempted to call the privileged service.|0x1f0|
|process_path|ProcessName|string|full path and the name of the executable for the process.|C:\Windows\System32\lsass.exe|
|object_server|ObjectServer|string|contains the name of the Windows subsystem calling the routine.|NT Local Security Authority / Authentication Service|
|user_privilege_list|PrivilegeList|string|the list of user privileges which were requested.|SeCreateGlobalPrivilege|
||Service|string|supplies a name of the privileged subsystem service or function.|LsaRegisterLogonProcess()|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4673.md)