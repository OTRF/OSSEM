# Event ID 5058: Key file operation.

## Description

This event generates when an operation (read, write, delete, and so on) was performed on a file that contains a KSP key by using a Key Storage Provider.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|user_sid|SubjectUserSid|string|SID of account that requested key file operation.|S-1-5-21-3457937927-2839227994-823803824-1104|
|user_name|SubjectUserName|string|the name of the account that requested key file operation.|dadmin|
|user_domain|SubjectDomainName|string|subject's domain or computer name. |CONTOSO|
|user_logon_id|SubjectLogonId|string|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x38e2d|
|event_provider_name|ProviderName|string|the name of KSP through which the operation was performed.|Microsoft Software Key Storage Provider|
|algorithm_name|AlgorithmName|string|the name of cryptographic algorithm through which the key was used or accessed.|ECDH\_P521|
|key_name|KeyName|string|the name of the key (key container) with which operation was performed.|le-SuperAdmin-5e350d8e-ae46-458c-bac0-d8f3279c944e|
|key_type|KeyType|string|can have one of the following values: "User key." – user's cryptographic key. "Machine key." – machine's cryptographic key.|%%2500|
|key_path|KeyFilePath|string|full path and filename of the key file on which the operation was performed.|C:\\Users\\dadmin\\AppData\\Roaming\\Microsoft\\Crypto\\Keys\\c0a496c6786f0d25e8624fee96e4e580\_7a1bf91d-ebdd-449c-825d-c97f2f47cd01|
|operation|Operation|string|performed operation.|%%2459|
|return_code|ReturnCode|integer|has “0x0” value for Success events.|0x0|

## Reference

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-5058.md)