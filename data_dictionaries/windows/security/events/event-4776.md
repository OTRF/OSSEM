# Event ID 4776: The computer attempted to validate the credentials for an account

## Description
This event generates every time that a credential validation occurs using NTLM authentication.This event occurs only on the computer that is authoritative for the provided credentials. For domain accounts, the domain controller is authoritative. For local accounts, the local computer is authoritative.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|logon_authentication_package_name|PackageName|string|The name of Authentication Package which was used for credential validation. It is always "MICROSOFT_AUTHENTICATION_PACKAGE_V1_0" for 4776 event.|`MICROSOFT_AUTHENTICATION_PACKAGE_V1_0`|
|user_name|TargetUserName|string|the name of the account that had its credentials validated by the Authentication Package. Can be user name, computer account name or well-known security principal account name.|`dadmin`|
|src_host_name|Workstation|string|The name of the computer from which the logon attempt originated.|`WIN81`|
|event_status|Status|integer|Contains error code for Failure events. For Success events this parameter has "0x0" value.|`0xc0000234`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4776.md)
* [MS Security Auditing Category - Account Logon](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#account-logon)
* [MS Security Auditing Category - Detailed Tracking](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#detailed-tracking)
* [MS Security Auditing Sub-category - Audit Credential Validation](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-credential-validation.md)

## Tags
* Account Logon
* Detailed Tracking
* Audit Credential Validation