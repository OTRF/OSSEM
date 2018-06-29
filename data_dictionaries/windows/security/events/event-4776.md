# Event ID 4776: The computer attempted to validate the credentials for an account

## Description

This event generates every time that a credential validation occurs using NTLM authentication.This event occurs only on the computer that is authoritative for the provided credentials. For domain accounts, the domain controller is authoritative. For local accounts, the local computer is authoritative.

* It shows successful and unsuccessful credential validation attempts
* It shows only the computer name (Source Workstation) from which the authentication attempt was performed (authentication source). For example, if you authenticate from CLIENT-1 to SERVER-1 using a domain account you will see CLIENT-1 in the Source Workstation field. Information about the destination computer (SERVER-1) is not presented in this event.
* If a credential validation attempt fails, you will see a Failure event with Error Code parameter value not equal to “0x0”.
* The main advantage of this event is that on domain controllers you can see all authentication attempts for domain accounts when NTLM authentication was used.
* For monitoring local account logon attempts, it is better to use event “4624: An account was successfully logged on” because it contains more details and is more informative.
* This event also generates when a workstation unlock event occurs.
* This event does not generate when a domain account logs on locally to a domain controller.

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4776.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4776.md)

## Data Dictionary

| Standard Name | Field Name | Type | Description | Sample Value |
| ---------------- | ---------------- | ---------------- | ----------------	| ---------------- |
| logon_authentication_package_name | PackageName | string | The name of Authentication Package which was used for credential validation. It is always “MICROSOFT_AUTHENTICATION_PACKAGE_V1_0” for 4776 event. | MICROSOFT\_AUTHENTICATION\_PACKAGE\_V1\_0 |
| user_name | TargetUserName | string | the name of the account that had its credentials validated by the Authentication Package. Can be user name, computer account name or well-known security principal account name. | dadmin |
| src_host_name | Workstation | string | The name of the computer from which the logon attempt originated. | WIN81 |
| event_status | Status | integer | Contains error code for Failure events. For Success events this parameter has “0x0” value. | 0xc0000234 |