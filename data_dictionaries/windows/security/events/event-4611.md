# Event ID 4611: A trusted logon process has been registered with the Local Security Authority.

## Description
This event indicates that a logon process has registered with the Local Security Authority (LSA). Also, logon requests will now be accepted from this source.
At the technical level, the event does not come from the registration of a trusted logon process, but from a confirmation that the process is a trusted logon process. If it is a trusted logon process, the event generates.
A logon process is a trusted part of the operating system that handles the overall logon function for different logon methods (network, interactive, etc.).
You typically see these events during operating system startup or user logon and authentication actions

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|TBD|string|SID of account that registered the trusted logon process.|S-1-5-18|
|user_name|SubjectUserName|TBD|string|the name of the account that registered the trusted logon process.|DC01$|
|user_domain|SubjectDomainName|TBD|string|subject's domain or computer name.|CONTOSO|
|user_logon_id|SubjectLogonId|TBD|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x3e7|
|logon_process_name|LogonProcessName|TBD|string|the name of registered logon process.|Winlogon|

## Resources
* [MS SOURCE](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4611.md)
* [MS Security Auditing Category - System](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#system)
* [MS Security Auditing Sub-category - Audit Security System Extension](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-security-system-extension.md)

## Tags
* System
* Audit Security System Extension