# Event ID 4688: A new process has been created

## Description
Event ID 4688: A new process has been created

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account that requested the "create process" operation.|`S-1-5-18`|
|user_name|SubjectUserName|UnicodeString|the name of the account that requested the "create process" operation.|`WIN-GG82ULGC9GO$`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|contains error code for Failure events. For Success events this parameter has "0x0" value. hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x3e7`|
|process_id|NewProcessId|Pointer|hexadecimal Process ID of the new process.|`0x2bc`|
|process_path|NewProcessName|UnicodeString|full path and the name of the executable for the new process.|`C:\Windows\System32\rundll32.exe`|
|process_token_elevation_type|TokenElevationType|UnicodeString|Token elevation type. It can be Default(1), Full(2) or Limited(3)|`%%1938`|
|process_parent_id|ProcessId|Pointer|hexadecimal Process ID of the process which ran the new process.|`0xe74`|
|process_command_line|CommandLine|UnicodeString|contains the name of executable and arguments which were passed to it. You must enable "Administrative Templates\System\Audit Process Creation\Include command line in process creation events" group policy to include command line in process creation events|``|
|target_user_sid|TargetUserSid|SID|SID of target account.|`S-1-5-21-1377283216-344919071-3415362939-1104`|
|target_user_name|TargetUserName|UnicodeString|the name of the target account|`dadmin`|
|target_user_domain|TargetDomainName|UnicodeString|target account's domain or computer name.|`CONTOSO`|
|target_user_logon_id|TargetLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x4a5af0`|
|process_parent_path|ParentProcessName|UnicodeString|full path and the name of the executable for the process.|`C:\Windows\explorer.exe`|
|process_mandatory_sid|MandatoryLabel|SID|SID of integrity label which was assigned to the new process.|`S-1-16-8192`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4688.md)
* [MS Security Auditing Category - Detailed Tracking](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#detailed-tracking)
* [MS Security Auditing Sub-category - Audit Process Creation](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-process-creation.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* version_2
* Detailed Tracking
* Audit Process Creation