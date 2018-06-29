# Audit Account Management

## Description

This audit setting determines whether to track management of users and groups. For example, users and groups should be tracked when a user or computer account, a security group, or a distribution group is created, changed, or deleted; when a user or computer account is renamed, disabled, or enabled; or when a user or computer password is changed. An event can be generated for users or groups that are added to or removed from other groups. [Microsoft Source](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#account-management)

## Subcategories

| Subcategory | Description | Event Volume |
|---------|-------|---------|
| [Audit Computer Account Management](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/account_management/computer_account_management/README.md) | Audit Computer Account Management determines whether the operating system generates audit events when a computer account is created, changed, or deleted | Low on domain controllers |
| [Audit Distribution Group Management](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/account_management/distribution_management/README.md) | Audit Distribution Group Management determines whether the operating system generates audit events for specific distribution-group management tasks | Low on domain controllers |
| [Audit Other Account Management](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/account_management/other_account_management/README.md) | Audit Other Account Management Events determines whether the operating system generates user account management audit events | Typically Low on all types of computers |
| [Audit Security Group Management](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/account_management/security_group_management/README.md) | Audit Security Group Management determines whether the operating system generates audit events when specific security group management tasks are performed | Low |
| [Audit User Account Management](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/security/account_management/user_account_management/README.md) | Audit User Account Management determines whether the operating system generates audit events when specific user account management tasks are performed | Low |
