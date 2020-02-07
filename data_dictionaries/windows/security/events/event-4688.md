# Event ID 4688: A new process has been created

## Description
This event generates every time a new process starts.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|TBD|string|SID of account that requested the "create process" operation.|S-1-5-18|
|user_name|SubjectUserName|TBD|string|the name of the account that requested the "create process" operation.|WIN-GG82ULGC9GO$|
|user_domain|SubjectDomainName|TBD|string|subject's domain or computer name.|CONTOSO|
|user_logon_id|SubjectLogonId|TBD|integer|contains error code for Failure events. For Success events this parameter has "0x0" value. hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x3e7|
|process_id|NewProcessId|TBD|integer|hexadecimal Process ID of the new process.|0x2bc|
|process_path|NewProcessName|TBD|string|full path and the name of the executable for the new process.|C:\Windows\System32\rundll32.exe|
|process_token_elevation_type|TokenElevationType|TBD|string|Token elevation type. It can be Default(1), Full(2) or Limited(3)|%%1938|
|process_parent_id|ProcessId|TBD|integer|hexadecimal Process ID of the process which ran the new process.|0xe74|
|process_command_line|CommandLine|TBD|string|contains the name of executable and arguments which were passed to it. You must enable "Administrative Templates\System\Audit Process Creation\Include command line in process creation events" group policy to include command line in process creation events||
|target_user_sid|TargetUserSid|TBD|string|SID of target account.|S-1-5-21-1377283216-344919071-3415362939-1104|
|target_user_name|TargetUserName|TBD|string|the name of the target account|dadmin|
|target_user_domain|TargetDomainName|TBD|string|target account's domain or computer name.|CONTOSO|
|target_user_logon_id|TargetLogonId|TBD|sinteger|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x4a5af0|
|process_parent_path|ParentProcessName|TBD|string|full path and the name of the executable for the process.|C:\Windows\explorer.exe|
|process_mandatory_sid|MandatoryLabel|TBD|string|SID of integrity label which was assigned to the new process.|S-1-16-8192|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4688.md)
* [MS Security Auditing Category - Detailed Tracking](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#detailed-tracking)
* [MS Security Auditing Sub-category - Audit Process Creation](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-process-creation.md)

## Tags
* Detailed Tracking
* Audit Process Creation