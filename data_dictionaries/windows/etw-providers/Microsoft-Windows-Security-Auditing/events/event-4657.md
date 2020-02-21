# Event ID 4657 A registry value was modified

## Description
Event ID 4657 A registry value was modified

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account that requested the "modify registry value" operation.|`THEDOMAIN\TheUser`|
|user_name|SubjectUserName|UnicodeString|the name of the account that requested the "modify registry value" operation.|`TheUser`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`THEDOMAIN`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|`0x364ef`|
|registry_key_path|ObjectName|UnicodeString|full path and name of the registry key which value was modified.|`\REGISTRY\MACHINE`|
|registry_key_value_name|ObjectValueName|UnicodeString|the name of modified registry key value.|`New_Name`|
|object_handle_id|HandleId|Pointer|hexadecimal value of a handle to Object Name.|`0x54`|
|object_operation_type|OperationType|UnicodeString|the type of performed operation with registry key value.|`Existing registry value modified`|
|object_value_old_type|OldValueType|UnicodeString|old type of changed registry key value.|`REG_SZ`|
|registry_value_old_data|OldValue|UnicodeString|old value for changed registry key value.|``|
|registry_key_value_type|NewValueType|UnicodeString|new type of changed registry key value.|`REG_SZ`|
|registry_key_value_data|NewValue|UnicodeString|new value for changed registry key value.|`Andreas`|
|process_id|ProcessId|Pointer|hexadecimal Process ID of the process through which the registry key value was modified.|`0xec43`|
|process_path|ProcessName|UnicodeString|full path and the name of the executable for the process.|`C:\Windows\regedit.exe`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4657.md)
* [MS Security Auditing Category - Object Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#object-access)
* [MS Security Auditing Sub-category - Audit Registry](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-registry.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Object Access
* Audit Registry