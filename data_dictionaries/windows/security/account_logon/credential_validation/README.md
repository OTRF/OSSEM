# Audit Credential Validation

These events occur on the computer that is authoritative for the credentials as follows:

* For domain accounts, the domain controller is authoritative.
* For local accounts, the local computer is authoritative.

Because domain accounts are used much more frequently than local accounts in enterprise environments, most of the Account Logon events in a domain environment occur on the domain controllers that are authoritative for the domain accounts. However, these events can occur on any computer, and they may occur in conjunction with or on separate computers from Logon and Logoff events.

The main reason to enable this auditing subcategory is to handle local accounts authentication attempts and, for domain accounts, NTLM authentication in the domain. It is especially useful for monitoring unsuccessful attempts, to find brute-force attacks, account enumeration, and potential account compromise events on domain controllers

[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-credential-validation)

## Data Dictionaries

| EventId | Description | Minimum OS |
|--------|---------|-------|
| 4774 | An account was mapped for logon [Event does not occour] | Windows Vista, Windows Server 2008 |
| 4775 | An account could not be mapped for logon [Event does not occour] | Windows Vista, Windows Server 2008 |
| [4776](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/events/event-4776.md) | The computer attempted to validate the credentials for an account | Windows Vista, Windows Server 2008 |
| 4777 | AThe domain controller failed to validate the credentials for an account | Windows Vista, Windows Server 2008 |