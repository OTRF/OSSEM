# Event ID 5633: A request was made to authenticate to a wired network

## Description
This event generates when 802.1x authentication attempt was made for wired network.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|host_interface_name|InterfaceName|UnicodeString|the name (description) of network interface which was used for authentication request. You can get the list of all available network adapters using "ipconfig /all" command.|`Microsoft Hyper-V Network Adapter`|
|user_identity|Identity|UnicodeString|User Principal Name (UPN) of account for which 802.1x authentication request was made.|`-`|
|user_name|SubjectUserName|UnicodeString|the name of the account for which 802.1x authentication request was made|`-`|
|user_domain|SubjectDomainName|UnicodeString|subject's domain or computer name|`-`|
|user_logon_id|SubjectLogonId|HexInt64|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|`0x0`|
|event_reason_code|ReasonCode|HexInt32|hexadecimal Reason Code for wired authentication results.|`0x70003`|
|event_reason_text|ReasonText|UnicodeString|contains Reason Text (explanation of Reason Code) and Reason Code for wired authentication results.|`The network does not support authentication`|
|event_error_code|ErrorCode|HexInt32|hexadecimal error code|`0x0`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5633.md)
* [MS Security Auditing Category - Account Logon](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#account-logon)
* [MS Security Auditing Category - Logon/Logoff](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#logonlogoff)
* [MS Security Auditing Sub-category - Audit Other Logon/Logoff Events](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-other-logon/logoff-events.md)

## Tags
* etw_level_Informational
* etw_task_task_0
* Account Logon
* Logon/Logoff
* Audit Other Logon/Logoff Events