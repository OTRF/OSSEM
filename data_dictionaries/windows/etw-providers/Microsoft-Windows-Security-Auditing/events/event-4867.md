# Event ID 4867: A trusted forest information entry was modified.

## Description
This event generates the trusted forest information entry was modified.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account that requested the "modify/change a trusted forest information entry" operation.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|UnicodeString|the name of the account that requested the "modify/change a trusted forest information entry" operation.|`dadmin`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|user_login_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x138eb0`|
|forest_root|ForestRoot|UnicodeString|the name of the Active Directory forest for which trusted forest information entry was modified.|`Fabrikam.local`|
|forest_sid|ForestRootSid|SID|the SID of the Active Directory forest for which trusted forest information entry was modified. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.|`S-1-5-21-2703072690-1374247579-2643703677`|
|operation_id|OperationId|HexInt64|unique hexadecimal identifier of the operation. You can correlate this event with other events (4865(S): A trusted forest information entry was added, 4866(S): A trusted forest information entry was removed) using this field.|`0x648620`|
|forest_entry_type|EntryType|UInt32|the type of modified entry.|`2`|
|forest_flags|Flags|UInt32|Forest flags flags.|`0`|
|forest_top_level_name|TopLevelName|UnicodeString|the name of the modified trusted forest information entry.|`-`|
|dns_name|DnsName|UnicodeString|DNS name of the trust partner. This parameter might not be captured in the event, and in that case appears as "-".|`Fabrikam.local`|
|netbios_name|NetbiosName|UnicodeString|NetBIOS name of the trust partner. This parameter might not be captured in the event, and in that case appears as "-".|`FABRIKAM`|
|domain_sid|DomainSid|SID|SID of the trust partner. This parameter might not be captured in the event, and in that case appears as "NULL SID".|`S-1-5-21-2703072690-1374247579-2643703677`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4867.md)
* [MS Security Auditing Category - Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#policy-change)
* [MS Security Auditing Sub-category - Audit Authentication Policy Change](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-authentication-policy-change.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Policy Change
* Audit Authentication Policy Change