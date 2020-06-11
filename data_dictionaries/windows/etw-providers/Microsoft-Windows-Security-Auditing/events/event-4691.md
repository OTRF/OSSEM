# Event ID 4691: Indirect access to an object was requested.

## Description
This event indicates that indirect access to an object was requested.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account that requested an access to the object.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|UnicodeString|the name of the account that requested an access to the object.|`dadmin`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x36509`|
|object_type|ObjectType|UnicodeString|The type of an object for which access was requested.|`ALPC Port`|
|object_name|ObjectName|UnicodeString|full path and name of the object for which access was requested.|`\Sessions\2\Windows\DwmApiPort`|
|object_access_list|AccessList|UnicodeString|the list of user privileges which were requested|`%%4464`|
|object_access_mask|AccessMask|HexInt32|The value of this parameter is in decimal format. There is no detailed information about this parameter in this document. If Desired Access is not presented, then this parameter will have "0" value.|`0x1`|
|process_id|ProcessId|Pointer|hexadecimal Process ID of the process through which the access was requested.|`0xe60`|

## References
* [MS SOURCE](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4691.md)
* [MS Security Auditing Category - Object Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#object-access)
* [MS Security Auditing Sub-category - Audit Other Object Access Events](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-other-object-access-events.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Object Access
* Audit Other Object Access Events