# Event ID 4866: A trusted forest information entry was removed.

## Description
This event generates when the trusted forest information entry was removed.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|forest_root|ForestRoot|TBD|string|the name of the Active Directory forest for which trusted forest information entry was removed.|Fabrikam.local|
|forest_sid|ForestRootSid|TBD|string|the SID of the Active Directory forest for which trusted forest information entry was removed.|S-1-5-21-2703072690-1374247579-2643703677|
|operation_id|OperationId|TBD|integer|unique hexadecimal identifier of the operation. You can correlate this event with other events (4865(S): A trusted forest information entry was added, 4867(S): A trusted forest information entry was modified.) using this field.|0x648620|
|forest_entry_type|EntryType|TBD|integer|the type of removed entry|2|
|forest_flags|Flags|TBD|integer|Forest flags flags.|0|
|forest_top_level_name|TopLevelName|TBD|string|the name of the removed trusted forest information entry.|-|
|dns_name|DnsName|TBD|string|DNS name of the trust partner. This parameter might not be captured in the event, and in that case appears as "-".|Fabrikam.local|
|netbios_name|NetbiosName|TBD|string|NetBIOS name of the trust partner. This parameter might not be captured in the event, and in that case appears as "-".|FABRIKAM|
|domain_sid|DomainSid|TBD|string|SID of the trust partner. This parameter might not be captured in the event, and in that case appears as "NULL SID".|S-1-5-21-2703072690-1374247579-2643703677|
|user_sid|SubjectUserSid|TBD|string|SID of account that requested the "remove a trusted forest information entry" operation.|S-1-5-21-3457937927-2839227994-823803824-1104|
|user_name|SubjectUserName|TBD|string|the name of the account that requested the "remove a trusted forest information entry" operation.|dadmin|
|user_domain|SubjectDomainName|TBD|string|subject's domain or computer name.|CONTOSO|
|user_logon_id|SubjectLogonId|TBD|string|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x138eb0|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4866.md)
* [MS Security Auditing Category - Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#policy-change)
* [MS Security Auditing Sub-category - Audit Authentication Policy Change](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-authentication-policy-change.md)

## Tags
* Policy Change
* Audit Authentication Policy Change