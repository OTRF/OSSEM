# Event ID 4904: An attempt was made to register a security event source.

## Description
This event generates every time a new security event source.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|TBD|string|SID of account that made an attempt to register a security event source.|S-1-5-18|
|user_name|SubjectUserName|TBD|string|the name of the account that made an attempt to register a security event source.|DC01$|
|user_domain|SubjectDomainName|TBD|string|subject's domain or computer name.|CONTOSO|
|user_logon_id|SubjectLogonId|TBD|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x3e7|
|event_source_name|AuditSourceName|TBD|string|the name of registered security event source. You can see all registered security event source names in this registry path: "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\EventLog\Security".|FSRM Audit|
|event_source_id|EventSourceId|TBD|integer|the unique hexadecimal identifier of registered security event source.|0x1cc4e|
|process_id|ProcessId|TBD|integer|hexadecimal Process ID of the process that attempted to register the security event source.|0x688|
|process_path|ProcessName|TBD|||C:\Windows\System32\svchost.exe|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4904.md)
* [MS Security Auditing Category - Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#policy-change)
* [MS Security Auditing Sub-category - Audit Policy Change](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-policy-change.md)

## Tags
* Policy Change
* Audit Policy Change