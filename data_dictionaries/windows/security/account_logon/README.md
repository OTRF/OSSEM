# Audit Account Logon

## Description

Configuring policy settings in this category can help you document attempts to authenticate account data on a domain controller or on a local Security Accounts Manager (SAM). Unlike Logon and Logoff policy settings and events, which track attempts to access a particular computer, settings and events in this category focus on the account database that is used. [Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#account-logon)

## Subcategories

| Subcategory | Description | Event Volume |
|---------|-------|---------|
| [Audit Credential Validation](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/account_logon/credential_validation/README.md) | Audit Credential Validation determines whether the operating system generates audit events on credentials that are submitted for a user account logon request | High on domain controllers. Low on member servers and workstations |
| [Audit Kerberos Authentication Service](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/account_logon/kerberos_authentication_service/README.md) | Audit Kerberos Authentication Service determines whether to generate audit events for Kerberos authentication ticket-granting ticket (TGT) requests | High on Kerberos Key Distribution Center servers |
| [Audit Kerberos Service Ticket Operations](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/account_logon/kerberos_service_ticket_operations/README.md) | Audit Kerberos Service Ticket Operations determines whether the operating system generates security audit events for Kerberos service ticket requests | Very High on Kerberos Key Distribution Center servers |
| [Audit Other Logon/Logoff Events](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/account_logon/other_logon_logoff/README.md) | Audit Other Logon/Logoff Events determines whether Windows generates audit events for other logon or logoff events | Low |