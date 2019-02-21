# Audit Kerberos Authentication Service

If you configure this policy setting, an audit event is generated after a Kerberos authentication TGT request. Success audits record successful attempts and Failure audits record unsuccessful attempts.

This subcategory contains events about issued TGTs and failed TGT requests. It also contains events about failed Pre-Authentications, due to wrong user password or when the user’s password has expired.

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-kerberos-authentication-service)

## Data Dictionaries

| EventId | Description | Minimum OS |
|--------|---------|-------|
| [4768](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4768.md) | A Kerberos authentication ticket (TGT) was requested | Windows Vista, Windows Server 2008 |
| [4771](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4771.md) | Kerberos pre-authentication failed | Windows Vista, Windows Server 2008 |
| [4772](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4772.md) | A Kerberos authentication ticket request failed | Windows Vista, Windows Server 2008 |