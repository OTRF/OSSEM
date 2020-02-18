# Event ID 4648: A logon was attempted using explicit credentials

## Description
Event ID 4648: A logon was attempted using explicit credentials

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account that requested the new logon session with explicit credentials.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|UnicodeString|the name of the account that requested the new logon session with explicit credentials.|`dadmin`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name|`CONTOSO`|
|user_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|`0x31844`|
|user_logon_guid|LogonGuid|GUID|a GUID that can help you correlate this event with another event that can contain the same Logon GUID|`{00000000-0000-0000-0000-000000000000}`|
|target_user_name|TargetUserName|UnicodeString|the name of the account whose credentials were used|`ladmin`|
|target_user_domain|TargetDomainName|UnicodeString|subject's domain or computer name|`CONTOSO`|
|target_user_logon_guid|TargetLogonGuid|GUID|a GUID that can help you correlate this event with another event that can contain the same Logon GUID, "4769(S, F): A Kerberos service ticket was requested event on a domain controller.|`{0887F1E4-39EA-D53C-804F-31D568A06274}`|
|target_server_name|TargetServerName|UnicodeString|the name of the server on which the new process was run. Has "localhost" value if the process was run locally.|`localhost`|
|target_info|TargetInfo|UnicodeString|there is no detailed information about this field in this document.|`localhost`|
|process_id|ProcessId|Pointer|hexadecimal Process ID of the process which was run using explicit credentials. Process ID (PID) is a number used by the operating system to uniquely identify an active process.|`0x368`|
|process_path|ProcessName|UnicodeString|full path and the name of the executable for the process.|`C:\Windows\System32\svchost.exe`|
|src_ip_addr|IpAddress|UnicodeString|IP address of machine from which logon attempt was performed.|`::1`|
|src_port|IpPort|UnicodeString|source port which was used for logon attempt from remote machine.|`0`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4648.md)
* [MS Security Auditing Category - Logon/Logoff](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#logonlogoff)
* [MS Security Auditing Sub-category - Audit Logon](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-logon.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Logon/Logoff
* Audit Logon