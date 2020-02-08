# Event ID 5632: A request was made to authenticate to a wireless network

## Description
This event generates when 802.1x authentication attempt was made for wireless network.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|wireless_ssid|SSID|string|SSID of the wireless network to which authentication request was sent.|`Nokia`|
|user_identity|Identity|string|User Principal Name (UPN) or another type of account identifier for which 802.1x authentication request was made.|`host/XXXXXXXX.redmond.corp.microsoft.com`|
|user_name|SubjectUserName|string|the name of the account for which 802.1x authentication request was made.|`-`|
|user_domain|SubjectDomainName|string|subject's domain or computer name|`-`|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID|`0x0`|
|host_peer_mac|PeerMac|string|peer's (typically - access point) MAC-address|`18:64:72:F3:33:91`|
|host_local_mac|LocalMac|string|local interface's MAC-address|`02:1A:C5:14:59:C9`|
|host_interface_guid|IntfGuid|string|GUID of the network interface which was used for authentication request.|`{2BB33827-6BB6-48DB-8DE6-DB9E0B9F9C9B}`|
|event_reason_code|ReasonCode|string|hexadecimal Reason Code for wired authentication results.|`0x0`|
|event_reason_text|ReasonText|string|contains Reason Text (explanation of Reason Code) and Reason Code for wireless authentication results.|`The operation was successful.`|
|event_error_code|ErrorCode|string|there is no information about this field in this document.|`0x0`|
|event_reason_code_eap|EAPReasonCode|string|Related to NPS (Network Policy Server) error code. [See NPS error codes](https://technet.microsoft.com/library/dd197570(v=ws.10).aspx)|`0x0`|
|event_root_cause_string_eap|EapRootCauseString|string|there is no information about this field in this document|`-`|
|event_error_code_eap|EAPErrorCode|string|there is no information about this field in this document|`0x0`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-5632.md)
* [MS Security Auditing Category - Account Logon](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#account-logon)
* [MS Security Auditing Category - Logon/Logoff](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#logonlogoff)
* [MS Security Auditing Sub-category - Audit Other Logon/Logoff Events](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-other-logon/logoff-events.md)

## Tags
* Account Logon
* Logon/Logoff
* Audit Other Logon/Logoff Events