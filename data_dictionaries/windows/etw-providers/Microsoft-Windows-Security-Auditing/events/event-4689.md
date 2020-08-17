# Event ID 4689: A process has exited
###### Version: 0

## Description
This event generates every time a process has exited.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account that requested the "terminate process" operation.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|UnicodeString|the name of the account that requested the "terminate process" operation.|`dadmin`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x31365`|
|event_status|Status|HexInt32|hexadecimal exit code of exited/terminated process.|`0x0`|
|process_id|ProcessId|Pointer|hexadecimal Process ID of the ended/terminated process.|`0xfb0`|
|process_name|ProcessName|UnicodeString|full path and the executable name of the exited/terminated process.|`C:\Windows\System32\notepad.exe`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4689.md)
* [MS Security Auditing Category - Detailed Tracking](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#detailed-tracking)
* [MS Security Auditing Sub-category - Audit Process Termination](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-process-termination.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Detailed Tracking
* Audit Process Termination