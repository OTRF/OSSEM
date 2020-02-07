# Event ID 4905: An attempt was made to unregister a security event source.

## Description
This event generates every time a security event source.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|TBD|string|SID of account that made an attempt to unregister a security event source.|S-1-5-18|
|user_name|SubjectUserName|TBD|string|the name of the account that made an attempt to unregister a security event source.|DC01$|
|user_domain|SubjectDomainName|TBD|string|subject's domain or computer name.|CONTOSO|
|user_logon_id|SubjectLogonId|TBD|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x3e7|
|event_source_name|AuditSourceName|TBD|string|the name of unregistered security event source. You can see all registered security event source names in this registry path: "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\EventLog\Security".|IIS-METABASE|
|event_source_id|EventSourceId|TBD|integer|the unique hexadecimal identifier of unregistered security event source.|0x20c15f|
|process_id|ProcessId|TBD|integer|hexadecimal Process ID of the process that attempted to unregister the security event source.|0xd90|
|process_path|ProcessName|TBD|string|full path and the name of the executable for the process.|-|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4905.md)
* [MS Security Auditing Category - Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#policy-change)
* [MS Security Auditing Sub-category - Audit Policy Change](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-policy-change.md)

## Tags
* Policy Change
* Audit Policy Change