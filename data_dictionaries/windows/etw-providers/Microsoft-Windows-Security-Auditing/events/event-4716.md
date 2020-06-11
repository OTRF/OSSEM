# Event ID 4716: Trusted domain information was modified.

## Description
This event generates when the trust was modified.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account that requested the "modify domain trust settings" operation.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|UnicodeString|the name of the account that requested the "modify domain trust settings" operation.|`dadmin`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|user_login_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x138eb0`|
|trust_name|DomainName|UnicodeString|the name of changed trusted domain. If this attribute was not changed, then it will have "-" value.|`-`|
|trust_sid|DomainSid|SID|the name of changed trusted domain. If this attribute was not changed, then it will have "-" value.|`S-1-5-21-2226861337-2836268956-2433141405`|
|trust_type|TdoType|UInt32|the type of new trust. If this attribute was not changed, then it will have "-" value or its old value.|`2`|
|trust_direction|TdoDirection|UInt32|the direction of new trust. If this attribute was not changed, then it will have "-" value or its old value.|`3`|
|trust_attributes|TdoAttributes|UInt32|the decimal value of attributes for new trust.|`32`|
|trust_filtering|SidFilteringEnabled|UnicodeString|SID Filtering state for the new trust.|`-`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4716.md)
* [MS Security Auditing Category - Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#policy-change)
* [MS Security Auditing Sub-category - Audit Authentication Policy Change](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-authentication-policy-change.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Policy Change
* Audit Authentication Policy Change