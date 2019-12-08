# Event ID 4692: Backup of data protection master key was attempted.

## Description

This event generates every time that a backup is attempted for the DPAPI Master Key.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|string|SID of account that requested backup operation.|S-1-5-21-3457937927-2839227994-823803824-500|
|user_name|SubjectUserName|string|the name of the account that requested backup operation.|ladmin|
|user_domain|SubjectDomainName|string|subject’s domain or computer name.|CONTOSO|
|user_logon_id|SubjectLogonId|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x30c08|
|master_key_id|MasterKeyId|string|unique identifier of a master key which backup was created.|16cfaea0-dbe3-4d92-9523-d494edb546bc|
|recovery_key_hostname|RecoveryServer|string|the name (typically – DNS name) of the computer that you contacted to back up your Master Key.|None|
|recovery_key_id|RecoveryKeyId|string|unique identifier of a recovery key.|806a0350-aeb1-4c56-91f9-ef16cf759291|
|event_failure_reason|FailureReason|integer|hexadecimal unique status code of performed operation.|0x0|

## Reference

[MS SOURCE](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4692.md)