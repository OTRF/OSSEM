# Event ID 4693: Recovery of data protection master key was attempted.

## Description

This event generates every time that recovery is attempted for a DPAPI Master Key.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|string|SID of account that requested the “recover” operation.|S-1-5-21-3457937927-2839227994-823803824-1104|
|user_name|SubjectUserName|string|the name of the account that requested the “recover” operation.|dadmin|
|user_domain|SubjectDomainName|string|subject's domain or computer name. |CONTOSO|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x30d7c|
|master_key_id|MasterKeyId|string|unique identifier of a master key which was recovered.|0445c766-75f0-4de7-82ad-d9d97aad59f6|
|recovery_key_reason|RecoveryReason|integer|hexadecimal code of recovery reason.|0x5c005c|
|recovery_key_hostname|RecoveryServer|string|the name (typically – DNS name) of the computer that you contacted to recover your Master Key.|DC01.contoso.local|
|recovery_key_id|RecoveryKeyId|string|unique identifier of a recovery key.|None|
|event_failure_reason|FailureId|integer|hexadecimal unique status code.|0x380000|

## Reference

[MS SOURCE](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4693.md)