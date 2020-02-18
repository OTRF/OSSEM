# Event ID 4713: Kerberos policy was changed.

## Description
Event ID 4713: Kerberos policy was changed.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account that made a change to Kerberos policy.|`S-1-5-18`|
|user_name|SubjectUserName|UnicodeString|the name of the account that made a change to Kerberos policy.|`DC01$`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x3e7`|
|keberos_policy_change|KerberosPolicyChange|UnicodeString|'--' means no changes, otherwise each change is shown as: Parameter_Name: new_value (old_value).|`KerMaxT: 0x10c388d000 (0x861c46800); KerMaxR: 0x19254d38000 (0xc92a69c000);`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4713.md)
* [MS Security Auditing Category - Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#policy-change)
* [MS Security Auditing Sub-category - Audit Authentication Policy Change](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-authentication-policy-change.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Policy Change
* Audit Authentication Policy Change