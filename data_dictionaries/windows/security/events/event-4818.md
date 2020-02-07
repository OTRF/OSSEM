# Event ID 4818: Proposed Central Access Policy does not grant the same access permissions as the current Central Access Policy.

## Description
This event generates when Dynamic Access Control Proposed Central Access Policy is enabled and access was not granted by Proposed Central Access Policy.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|TBD|string|SID of account that made an access request.|S-1-5-21-3457937927-2839227994-823803824-2104|
|user_name|SubjectUserName|TBD|string|the name of the account that made an access request.|Auditor|
|user_domain|SubjectDomainName|TBD|string|subject's domain or computer name.|CONTOSO|
|user_logon_id|SubjectLogonId|TBD|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x1e5f21|
|object_server|ObjectServer|TBD|string|has "Security" value for this event.|Security|
|object_type|ObjectType|TBD|string|The type of an object that was accessed during the operation. Always "File" for this event.|File|
|file_path|ObjectName|TBD|string|full path and name of the file or folder for which access was requested.|C:\Finance Documents\desktop.ini|
|object_handle_id|HandleId|TBD|integer|hexadecimal value of a handle to Object Name.|0xc64|
|process_id|ProcessId|TBD|integer|hexadecimal Process ID of the process through which the access was requested.|0x4|
|process_path|ProcessName|TBD|string|full path and the name of the executable for the process.|None|
|access_reason|AccessReason|TBD|string|the list of access check results for Current Access Policy.|%%1538: %%1801 D:(A;ID;0x1200a9;;;BU) %%1541: %%1801 D:(A;ID;0x1200a9;;;BU) %%4416: %%1801 D:(A;ID;0x1200a9;;;BU) %%4419: %%1801 D:(A;ID;0x1200a9;;;BU) %%4423: %%1801 D:(A;ID;0x1200a9;;;BU)|
|staging_reason|StagingReason|TBD|string|the list of access check results for Proposed Central Access Policy.|%%1538: %%1814Finance Documents Rule %%1541: %%1814Finance Documents Rule %%4416: %%1814Finance Documents Rule %%4419: %%1814Finance Documents Rule %%4423: %%1814Finance Documents Rule|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4818.md)
* [MS Security Auditing Category - Object Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#object-access)
* [MS Security Auditing Sub-category - Audit Central Access Policy Staging](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/audit-central-access-policy-staging.md)

## Tags
* Object Access
* Audit Central Access Policy Staging