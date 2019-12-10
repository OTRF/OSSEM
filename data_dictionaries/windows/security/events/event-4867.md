# Event ID 4867: A trusted forest information entry was modified.

## Description

This event generates the trusted forest information entry was modified.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|forest_root|ForestRoot|string|the name of the Active Directory forest for which trusted forest information entry was modified.|Fabrikam.local|
|forest_sid|ForestRootSid|string|the SID of the Active Directory forest for which trusted forest information entry was modified. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.|S-1-5-21-2703072690-1374247579-2643703677|
|operation_id|OperationId|integer|unique hexadecimal identifier of the operation. You can correlate this event with other events (4865(S): A trusted forest information entry was added, 4866(S): A trusted forest information entry was removed) using this field.|0x648620|
|forest_entry_type|EntryType|integer|the type of modified entry.|2|
|forest_flags|Flags|integer|Forest flags flags.|0|
|forest_top_level_name|TopLevelName|string|the name of the modified trusted forest information entry.|-|
|dns_name|DnsName|string|DNS name of the trust partner. This parameter might not be captured in the event, and in that case appears as "-".|Fabrikam.local|
|netbios_name|NetbiosName|string|NetBIOS name of the trust partner. This parameter might not be captured in the event, and in that case appears as “-”.|FABRIKAM|
|domain_sid|DomainSid|string|SID of the trust partner. This parameter might not be captured in the event, and in that case appears as “NULL SID”.|S-1-5-21-2703072690-1374247579-2643703677|
|user_sid|SubjectUserSid|string|SID of account that requested the "modify/change a trusted forest information entry" operation.|S-1-5-21-3457937927-2839227994-823803824-1104|
|user_name|SubjectUserName|string|the name of the account that requested the "modify/change a trusted forest information entry" operation.|dadmin|
|user_domain|SubjectDomainName|string|subject's domain or computer name.|CONTOSO|
|user_login_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x138eb0|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4867.md)