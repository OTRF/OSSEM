# Event ID 5633: A request was made to authenticate to a wired network

## Description
This event generates when 802.1x authentication attempt was made for wired network.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|host_interface_name|InterfaceName|TBD|string|the name (description) of network interface which was used for authentication request. You can get the list of all available network adapters using "ipconfig /all" command.|Microsoft Hyper-V Network Adapter|
|user_identity|Identity|TBD|string|User Principal Name (UPN) of account for which 802.1x authentication request was made.|-|
|user_name|SubjectUserName|TBD|string|the name of the account for which 802.1x authentication request was made|-|
|user_domain|SubjectDomainName|TBD|integer|subject's domain or computer name|-|
|user_logon_id|SubjectLogonId|TBD|string|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|0x0|
|event_reason_code|ReasonCode|TBD|string|hexadecimal Reason Code for wired authentication results.|0x70003|
|event_reason_text|ReasonText|TBD|string|contains Reason Text (explanation of Reason Code) and Reason Code for wired authentication results.|The network does not support authentication|
|event_error_code|ErrorCode|TBD|string|hexadecimal error code|0x0|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5633.md)
* [MS Security Auditing Category - Account Logon](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#account-logon)
* [MS Security Auditing Category - Logon/Logoff](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#logonlogoff)
* [MS Security Auditing Sub-category - Audit Other Logon/Logoff Events](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-other-logon/logoff-events.md)

## Tags
* Account Logon
* Logon/Logoff
* Audit Other Logon/Logoff Events