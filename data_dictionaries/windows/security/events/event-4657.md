# Event ID 4657 A registry value was modified

## Description
This event generates when a registry key value was modified. It doesn't generate when a registry key was modified. This event generates only if "Set Value" auditing is set in registry key's SACL.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|object_handle_id|HandleId|TBD|integer|hexadecimal value of a handle to Object Name.|0x54|
|user_sid|SubjectUserSid|TBD|string|SID of account that requested the "modify registry value" operation.|THEDOMAIN\TheUser|
|user_name|SubjectUserName|TBD|string|the name of the account that requested the "modify registry value" operation.|TheUser|
|user_domain|SubjectDomainName|TBD|string|subject's domain or computer name.|THEDOMAIN|
|user_logon_id|SubjectLogonId|TBD|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|0x364ef|
|registry_key_value_data|NewValue|TBD|string|new value for changed registry key value.|Andreas|
|registry_key_value_type|NewValueType|TBD|string|new type of changed registry key value.|REG_SZ|
|process_id|ProcessId|TBD|integer|hexadecimal Process ID of the process through which the registry key value was modified.|0xec43|
|process_path|ProcessName|TBD|string|full path and the name of the executable for the process.|C:\Windows\regedit.exe|
|registry_key_path|ObjectName|TBD|string|full path and name of the registry key which value was modified.|\REGISTRY\MACHINE|
|registry_key_value_name|ObjectValueName|TBD|string|the name of modified registry key value.|New_Name|
|registry_value_old_data|OldValue|TBD|string|old value for changed registry key value.||
|object_value_old_type|OldValueType|TBD|string|old type of changed registry key value.|REG_SZ|
|object_operation_type|OperationType|TBD|string|the type of performed operation with registry key value.|Existing registry value modified|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4657.md)
* [MS Security Auditing Category - Object Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#object-access)
* [MS Security Auditing Sub-category - Audit Registry](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-registry.md)

## Tags
* Object Access
* Audit Registry