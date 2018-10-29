# Audit Privilege Use

## Description

Permissions on a network are granted for users or computers to complete defined tasks. Privilege Use security policy settings and audit events allow you to track the use of certain permissions on one or more systems.[Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#privilege-use)

## Subcategories

| Subcategory | Description | Event Volume |
|---------|-------|---------|
| [Audit Non Sensitive Privilege Use](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/privilege_use/non_sensitive_privilege/README.md) | Audit Non Sensitive Privilege Use contains events that show usage of non-sensitive privileges. | Very High|
| [Audit Sensitive Privilege Use](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/privilege_use/sensitive_privilege/README.md) | Audit Sensitive Privilege Use contains events that show the usage of sensitive privileges. | High |
| [Audit Other Privilege Use Events](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/privilege_use/other_privilege_use/README.md) | This auditing subcategory should not have any events in it, but for some reason Success auditing will enable generation of event 4985(S): The state of a transaction has changed. | |