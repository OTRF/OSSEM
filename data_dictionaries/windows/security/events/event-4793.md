# Event ID 4793: The Password Policy Checking API was called

## Description
This event generates each time the Password Policy Checking API is called.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|TBD|string|SID of account that requested Password Policy Checking API operation.|S-1-5-21-3457937927-2839227994-823803824-1104|
|user_name|SubjectUserName|TBD|string|the name of the account that requested Password Policy Checking API operation.|dadmin|
|user_domain|SubjectDomainName|TBD|string|subject's domain name.|CONTOSO|
|user_logon_id|SubjectLogonId|TBD|string|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x36f67|
|source_host_name|Workstation|TBD|string|name of the computer from which the Password Policy Checking API was called. Typically, this is the same computer where this event was generated, for example, DC01. Computer name here does not contain $ symbol at the end. It also can be an IP address or the DNS name of the computer.|DC01|
|target_user_name|TargetUserName|TBD|string|the name of account, which password was provided/requested for validation. This parameter might not be captured in the event, and in that case appears as "-".|-|
|event_status|Status|TBD|string|typically has "0x0" value. Status code is "0x0", no matter meets password domain Password Policy or not.|0x0|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4793.md)
* [MS Security Auditing Category - Account Management](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#account-management)
* [MS Security Auditing Sub-category - Audit Other Account Management Events](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-other-account-management-events.md)

## Tags
* Account Management
* Audit Other Account Management Events