# Event ID 5061: Cryptographic operation.

## Description
Event ID 5061: Cryptographic operation.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account that requested specific cryptographic operation.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|UnicodeString|the name of the account that requested specific cryptographic operation.|`dadmin`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x38e2d`|
|key_provider_name|ProviderName|UnicodeString|the name of KSP through which the operation was performed.|`Microsoft Software Key Storage Provider`|
|key_algorithm_name|AlgorithmName|UnicodeString|the name of cryptographic algorithm through which the key was used or accessed.|`ECDH_P521`|
|key_name|KeyName|UnicodeString|the name of the key (key container) with which operation was performed.|`le-SuperAdmin-795fd6c1-2fae-4bef-a6bc-4f4d464bc083`|
|key_type|KeyType|UnicodeString|can have one of the following values: "User key." - user's cryptographic key. "Machine key." - machine's cryptographic key.|`%%2500`|
|key_operation|Operation|UnicodeString|performed operation.|`%%2464`|
|key_return_code|ReturnCode|HexInt32|has "0x0" value for Success events.|`0x0`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-5061.md)
* [MS Security Auditing Category - System](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#system)
* [MS Security Auditing Sub-category - Audit System Integrity](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-system-integrity.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* System
* Audit System Integrity