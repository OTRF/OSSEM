# Event ID 4662: An operation was performed on an object

## Description
This event generates every time when an operation was performed on an Active Directory object. This event generates only if appropriate SACL was set for Active Directory object and performed operation meets this SACL. If operation failed then Failure event will be generated. You will get one 4662 for each operation type which was performed.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account that requested the operation. Event Viewer automatically tries to resolve SIDs and show the account name. If the SID cannot be resolved, you will see the source data in the event.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|UnicodeString|the name of the account that requested the operation.|`dadmin`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID.|`0x2e80c`|
|object_server|ObjectServer|UnicodeString|has "DS" value for this event.|`DS`|
|object_type|ObjectType|UnicodeString|type or class of the object that was accessed.|`%{bf967a86-0de6-11d0-a285-00aa003049e2}`|
|object_name|ObjectName|UnicodeString|distinguished name of the object that was accessed.|`%{38b3d2e6-9948-4dc1-ae90-1605d5eab9a2}`|
|object_operation_type|OperationType|UnicodeString|the type of operation which was performed on an object. Typically has "Object Access" value for this event.|`Object Access`|
|object_handle_id|HandleId|Pointer|hexadecimal value of a handle to Object Name. This field can help you correlate this event with other events that might contain the same Handle ID, for example, "4661: A handle to an object was requested." This parameter might not be captured in the event, and in that case appears as "0x0".|`0x0`|
|object_access_list|AccessList|UnicodeString|the type of access used for the operation.|`%%1537`|
|object_access_mask|AccessMask|HexInt32|hexadecimal mask for the type of access used for the operation. See|`0x10000`|
|object_properties|Properties|UnicodeString|first part is the type of access that was used. Typically has the same value as Accesses field.|`%%1537 {bf967a86-0de6-11d0-a285-00aa003049e2}`|
|additionalinfo|AdditionalInfo|UnicodeString|-|`-`|
|additionalinfo2|AdditionalInfo2|UnicodeString|-|`-`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4662.md)
* [MS Security Auditing Category - DS Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#ds-access)
* [MS Security Auditing Sub-category - Audit Directory Service Access](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-directory-service-access.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* DS Access
* Audit Directory Service Access