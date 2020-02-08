# Event ID 4649: A replay attack was detected

## Description
This event generates on domain controllers when KRB_AP_ERR_REPEAT Kerberos response was sent to the client.
Domain controllers cache information from recently received tickets. If the server name, client name, time, and microsecond fields from the Authenticator match recently seen entries in the cache, it will return KRB_AP_ERR_REPEAT. You can read more about this in RFC-1510. One potential cause for this is a misconfigured network device between the client and server that could send the same packet(s) repeatedly.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_reporter_sid|SubjectUserSid|string|SID of account that that reported information about the replay.|`S-1-5-18`|
|user_reporter_name|SubjectUserName|string|the name of the account that reported information about the replay.|`DC01$`|
|user_reporter_domain|SubjectDomainName|string|subject’s domain or computer name.|`CONTOSO`|
|user_reporter_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID.|`0x3e7`|
|user_name|TargetUserName|string|the name of the account whose credential were replayed.|`DC02$`|
|user_domain|TargetDomainName|string|the domain of the account whose credential were replayed.|`CONTOSO.LOCAL`|
|logon_process_name|LogonProcessName|string|The name of the trusted logon process that was used for the replay.|`Kerberos`|
|logon_authentication_package_name|AuthenticationPackageName|string|The name of the authentication package which was used for the Kerberos.|`Kerberos`|
|src_host_name|WorkstationName|string|machine name from which attempt was performed. May not exist.|`-`|
|logon_transmitted_services|TransmittedServices|string|the list of transmitted services. Transmitted services are populated if the logon was a result of a S4U (Service For User) logon process. S4U is a Microsoft extension to the Kerberos Protocol to allow an application service to obtain a Kerberos service ticket on behalf of a user – most commonly done by a front-end website to access an internal resource on behalf of a user.|`-`|
|ticket_request_type|RequestType|string|The type of request.|`KRB_AP_REQ`|
|process_id|ProcessId|string|hexadecimal Process ID of the process.|`0xb9adc08`|
|process_path|ProcessName|string|full path and the name of the executable for the process.|`C:\Windows\System32\dns.exe`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4649.md)
* [MS Security Auditing Category - Logon/Logoff](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#logonlogoff)
* [MS Security Auditing Sub-category - Audit Other Logon/Logoff Events](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/audit-other-logonlogoff-events.md)

## Tags
* Logon/Logoff
* Audit Logoff