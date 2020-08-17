# Event ID 4627: Group membership information
###### Version: 0

## Description
This event generates with "4624(S): An account was successfully logged on" and shows the list of groups that the logged-on account belongs to.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_reporter_sid|SubjectUserSid|SID|SID of account that reported information about claims.|`S-1-0-0`|
|user_reporter_name|SubjectUserName|UnicodeString|the name of the account that reported information about claims.|`-`|
|user_reporter_domain|SubjectDomainName|UnicodeString|subject's domain or computer name|`-`|
|user_reporter_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|`0x0`|
|user_sid|TargetUserSid|SID|SID of account for which logon was performed.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|TargetUserName|UnicodeString|the name of the account for which logon was performed|`dadmin`|
|user_domain|TargetDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|user_logon_id|TargetLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|`0x136f7b`|
|logon_type|LogonType|UInt32|the type of logon which was performed.|`3`|
|event_sequence_id|EventIdx|UInt32|If is there is not enough space in one event to put all groups, you will see "1 of N" in this field and additional events will be generated. Typically this field has "1 of 1" value.|`1`|
|event_count_total|EventCountTotal|UInt32|Total number of events in the sequence.|`1`|
|TBD|GroupMembership|UnicodeString|the list of group SIDs which logged account belongs to (member of). Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.|`%{S-1-5-21-1377283216-344919071-3415362939-513} %{S-1-1-0} %{S-1-5-32-544} %{S-1-5-32-545} %{S-1-5-32-554} %{S-1-5-2} %{S-1-5-11} %{S-1-5-15} %{S-1-5-21-1377283216-344919071-3415362939-512} %{S-1-5-21-1377283216-344919071-3415362939-572} %{S-1-5-64-10} %{S-1-16-12288}`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4627.md)
* [MS Security Auditing Category - Logon/Logoff](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#logonlogoff)
* [MS Security Auditing Sub-category - Audit Group Membership](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-group-membership.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Logon/Logoff
* Audit Group Membership