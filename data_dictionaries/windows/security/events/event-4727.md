# Event ID 4727: A security-enabled global group was created.

## Description
Event 4727 is the same as 4731, but it is generated for a global security group instead of a local security group. All event fields, XML, and recommendations are the same. The type of group is the only difference.
Event 4727(S) generates only for domain groups, so the Local sections in event 4731 do not apply.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|group_name|TargetUserName|TBD|string|the name of the group that was created|AccountOperators|
|group_domain|TargetDomainName|TBD|string|domain or computer name of the created group.|CONTOSO|
|group_sid|TargetSid|TBD|string|SID of created group|S-1-5-21-3457937927-2839227994-823803824-6605|
|user_sid|SubjectUserSid|TBD|string|SID of account that requested the "create group" operation. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.|S-1-5-21-3457937927-2839227994-823803824-1104|
|user_name|SubjectUserName|TBD|string|the name of the account that requested the "create group" operation|dadmin|
|user_domain|SubjectDomainName|TBD|string|subject's domain or computer name.|CONTOSO|
|user_logon_id|SubjectLogonId|TBD|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x3031e|
|user_privilege_list|PrivilegeList|TBD|string|the list of user privileges which were used during the operation, for example, SeBackupPrivilege. This parameter might not be captured in the event, and in that case appears as "-".|-|
|group_sam_name|SamAccountName|TBD|string|this is a name of new group used to support clients and servers from previous versions of Windows (pre-Windows 2000 logon name). The value of sAMAccountName attribute of new group object. For example: ServiceDesk. For local groups it is simply a name of new group|AccountOperators|
|group_sid_history|SidHistory|TBD|string|contains previous SIDs used for the object if the object was moved from another domain. Whenever an object is moved from one domain to another, a new SID is created and becomes the objectSID. The previous SID is added to the sIDHistory property. This parameter contains the value of sIDHistory attribute of new group object. This parameter might not be captured in the event, and in that case appears as "-". For local groups it is not applicable and always has "-" value.|-|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4731.md)
* [MS Security Auditing Category - Account Management](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#account-management)
* [MS Security Auditing Sub-category - Audit Security Group Management](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-security-group-management.md)

## Tags
* Account Management
* Audit Security Group Management