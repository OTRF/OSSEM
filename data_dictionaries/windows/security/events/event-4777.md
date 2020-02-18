# Event ID 4777: The domain controller failed to validate the credentials for an account.

## Description
Currently this event doesn’t generate. It is a defined event, but it is never invoked by the operating system. 4776 failure event is generated instead.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|ClientUserName|UnicodeString|None|`None`|
|TBD|TargetUserName|UnicodeString|None|`None`|
|TBD|Workstation|UnicodeString|None|`None`|
|TBD|Status|UnicodeString|None|`None`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4777.md)
* [MS Security Auditing Category - Account Logon](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#account-logon)
* [MS Security Auditing Category - Detailed Tracking](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#detailed-tracking)
* [MS Security Auditing Sub-category - Audit Credential Validation](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-credential-validation.md)

## Tags
* Account Logon
* Detailed Tracking
* Audit Credential Validation