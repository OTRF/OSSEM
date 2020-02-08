# Event ID 4618: A monitored security event pattern has occurred.

## Description
This event is generated when Windows is configured to generate alerts in accordance with the Common Criteria Security Audit Analysis requirements (FAU_SAA) and an auditable event pattern occurs.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|event_id|EventId|integer||`4624`|
|computer_name|ComputerName|string||`DC01.contoso.local`|
|user_sid|TargetUserSid|string||`S-1-5-21-3457937927-2839227994-823803824-1104`|
|user_name|TargetUserName|string||`dadmin`|
|user_domain|TargetUserDomain|string||`CONTOSO`|
|user_logon_id|TargetLogonId|integer||`0x1`|
|TBD|EventCount|integer||`10`|
|TBD|Duration|string||`"Hour"`|

## References
* [MS SOURCE](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4618.md)
* [MS Security Auditing Category - System](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#system)
* [MS Security Auditing Sub-category - Audit System Integrity](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-system-integrity.md)

## Tags
* System
* Audit System Integrity