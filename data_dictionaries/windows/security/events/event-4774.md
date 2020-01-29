# Event ID 4774: An account was mapped for logon

## Description


[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4774.md)

## Event Log Illustration & Event XML

[MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/event-4774.md)

## Data Dictionary

| Standard Name | Field Name | Type | Description | Sample Value |
| ---------------- | ---------------- | ---------------- | ----------------	| ---------------- |
| logon_authentication_package_name | MappingBy | string | The name of Authentication Package which was used for credential validation | Schannel |
| user_name | ClientUserName | string | the name of the account that had its credentials validated by the Authentication Package. Can be user name, computer account name or well-known security principal account name. | host/WIN81.contoso.local |
| target_user_name | MappedName | The name of the account logged on / mapped. | WIN81$ |