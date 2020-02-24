# Event ID 4696: A primary token was assigned to process

## Description
This event generates every time a process runs using the non-current access token, for example, UAC elevated token, RUN AS different user actions, scheduled task with defined user, services, and so on.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account that requested the "assign token to process" operation.|`S-1-5-18`|
|user_name|SubjectUserName|UnicodeString|the name of the account that requested the "assign token to process" operation.|`WIN2008$`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x3e7`|
|target_user_sid|TargetUserSid|SID|SID of account through which the security token will be assigned to the new process. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.|`S-1-5-18`|
|target_user_name|TargetUserName|UnicodeString|the name of the account through which the security token will be assigned to the new process.|`dadmin`|
|target_user_domain|TargetDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|target_user_logon_id|TargetLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x1c8c5`|
|target_process_id|TargetProcessId|Pointer|hexadecimal Process ID of the new process with new security token. If you convert the hexadecimal value to decimal, you can compare it to the values in Task Manager.|`0xf40`|
|target_process_path|TargetProcessName|UnicodeString|full path and the name of the executable for the new process.|`C:\Windows\System32\WerFault.exe`|
|process_id|ProcessId|Pointer|hexadecimal Process ID of the process which started the new process with the new security token.|`0x698`|
|process_path|ProcessName|UnicodeString|full path and the name of the executable for the process which ran the new process with new security token.|`C:\Windows\System32\svchost.exe`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4696.md)
* [MS Security Auditing Category - Detailed Tracking](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#detailed-tracking)
* [MS Security Auditing Sub-category - Audit Process Creation](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-process-creation.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Detailed Tracking
* Audit Process Creation