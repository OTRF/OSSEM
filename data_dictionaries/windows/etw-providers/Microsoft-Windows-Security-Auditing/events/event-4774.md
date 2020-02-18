# Event ID 4774: An account was mapped for logon

## Description
Event ID 4774: An account was mapped for logon

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|logon_authentication_package_name|MappingBy|UnicodeString|The name of Authentication Package which was used for credential validation.|`Schannel`|
|user_name|ClientUserName|UnicodeString|the name of the account that had its credentials validated by the Authentication Package. Can be user name, computer account name or well-known security principal account name.|`host/WIN81.contoso.local`|
|target_user_name|MappedName|UnicodeString|The name of the account logged on / mapped.|`WIN81$`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4774.md)
* [MS Security Auditing Category - Account Logon](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#account-logon)
* [MS Security Auditing Category - Detailed Tracking](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#detailed-tracking)
* [MS Security Auditing Sub-category - Audit Credential Validation](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-credential-validation.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Account Logon
* Detailed Tracking
* Audit Credential Validation