# Event ID 4793: The Password Policy Checking API was called
###### Version: 0

## Description
This event generates each time the Password Policy Checking API is called.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account that requested Password Policy Checking API operation.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|UnicodeString|the name of the account that requested Password Policy Checking API operation.|`dadmin`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|`0x36f67`|
|source_host_name|Workstation|UnicodeString|name of the computer from which the Password Policy Checking API was called. Typically, this is the same computer where this event was generated, for example, DC01. Computer name here does not contain $ symbol at the end. It also can be an IP address or the DNS name of the computer.|`DC01`|
|target_user_name|TargetUserName|UnicodeString|the name of account, which password was provided/requested for validation. This parameter might not be captured in the event, and in that case appears as "-".|`-`|
|event_status|Status|HexInt32|typically has "0x0" value. Status code is "0x0", no matter meets password domain Password Policy or not.|`0x0`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4793.md)
* [MS Security Auditing Category - Account Management](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#account-management)
* [MS Security Auditing Sub-category - Audit Other Account Management Events](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-other-account-management-events.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Account Management
* Audit Other Account Management Events