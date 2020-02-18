# Event ID 4706: A new trust was created to a domain.

## Description
Event ID 4706: A new trust was created to a domain.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|trust_name|DomainName|UnicodeString|the name of new trusted domain.|`corp.contoso.local`|
|trust_sid|DomainSid|SID|SID of new trusted domain.|`S-1-5-21-2226861337-2836268956-2433141405`|
|user_sid|SubjectUserSid|SID|SID of account that requested the "create domain trust" operation.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|UnicodeString|the name of the account that requested the "create domain trust" operation.|`dadmin`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x3e99d6`|
|trust_type|TdoType|UInt32|the type of new trust.|`2`|
|trust_direction|TdoDirection|UInt32|the direction of new trust.|`3`|
|trust_attributes|TdoAttributes|UInt32|the decimal value of attributes for new trust.|`32`|
|trust_filtering|SidFilteringEnabled|UnicodeString|SID Filtering state for the new trust.|`%%1796`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4706.md)
* [MS Security Auditing Category - Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#policy-change)
* [MS Security Auditing Sub-category - Audit Authentication Policy Change](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-authentication-policy-change.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Policy Change
* Audit Authentication Policy Change