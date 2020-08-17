# Event ID 5168: SPN check for SMB/SMB2 failed
###### Version: 0

## Description
This event generates when SMB SPN check fails.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|SID|SID of account for which SPN check operation was failed.|`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|SubjectUserName|UnicodeString|the name of the account for which SPN check operation was failed.|`dadmin`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name.|`CONTOSO`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|`0xd0cd4`|
|spn_name|SpnName|UnicodeString|SPN which was used to access the server.|`N/A`|
|error_code|ErrorCode|HexInt32|hexadecimal error code, for example "0xC0000022" = STATUS_ACCESS_DENIED.|`0xc0000022`|
|server_names|ServerNames|UnicodeString|information about possible server names to use to access the target server (NETBIOS, DNS, localhost, etc.).|`CONTOSO;contoso.local;DC01.contoso.local;DC01;LocalHost;`|
|configured_names|ConfiguredNames|UnicodeString|information about the names which were provided for validation.|`N/A`|
|ip_addresses|IpAddresses|UnicodeString|information about possible IP addresses to use to access the target server (IPv4, IPv6).|`127.0.0.1;::1;10.0.0.10;;fe80::31ea:6c3c:f40d:1973;;fe80::5efe:10.0.0.10;`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5168.md)
* [MS Security Auditing Category - Object Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#object-access)
* [MS Security Auditing Sub-category - Audit File Share](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-file-share.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Object Access
* Audit File Share