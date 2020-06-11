# Event ID 4782: The password hash an account was accessed

## Description
This event generates on domain controllers during password migration of an account using Active Directory Migration Toolkit. Typically "Subject\Security ID" is the SYSTEM account.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|target_user_name|TargetUserName|UnicodeString|the name of the account for which the password hash was migrated. For example: ServiceDesk|`Andrei`|
|target_user_domain|TargetDomainName|UnicodeString|domain name of the account for which the password hash was migrated.|`CONTOSO`|
|user_sid|SubjectUserSid|SID|SID of account that requested hash migration operation. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the even|`S-1-5-18`|
|user_name|SubjectUserName|UnicodeString|the name of the account that requested hash migration operation.|`DC01$`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x3e7`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4782.md)
* [MS Security Auditing Category - Account Management](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#account-management)
* [MS Security Auditing Sub-category - Audit Other Account Management Events](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-other-account-management-events.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Account Management
* Audit Other Account Management Events