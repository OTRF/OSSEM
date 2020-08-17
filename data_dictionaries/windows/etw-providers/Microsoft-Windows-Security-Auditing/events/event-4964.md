# Event ID 4964: Special groups have been assigned to a new logon
###### Version: 0

## Description
This event occurs when an account that is a member of any defined Special Group logs in.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account that requested logon for New Logon account|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|UnicodeString|the name of the account that requested logon for New Logon account|`dadmin`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID,|`0xd972e`|
|user_logon_guid|LogonGuid|GUID|a GUID that can help you correlate this event with another event that can contain the same Logon GUID, "4769(S, F): A Kerberos service ticket was requested event on a domain controller.|`{00000000-0000-0000-0000-000000000000}`|
|target_user_sid|TargetUserSid|SID|SID of account that performed the logon.|`S-1-5-21-3457937927-2839227994-823803824-500`|
|target_user_name|TargetUserName|UnicodeString|the name of the account that performed the logon.|`ladmin`|
|target_user_domain|TargetDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|target_user_logon_id|TargetLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x139faf`|
|target_user_logon_guid|TargetLogonGuid|GUID|a GUID that can help you correlate this event with another event that can contain the same Logon GUID, "4769(S, F): A Kerberos service ticket was requested event on a domain controller.|`{B03B6192-09AE-E77F-DD10-2DC430766040}`|
|target_user_sid_list|SidList|UnicodeString|the list of special group SIDs, which New Logon\Security ID is a member of.|`%{S-1-5-21-3457937927-2839227994-823803824-512}`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4964.md)
* [MS Security Auditing Category - Logon/Logoff](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#logonlogoff)
* [MS Security Auditing Sub-category - Audit Special Logon](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-special-logon.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Logon/Logoff
* Audit Special Logon