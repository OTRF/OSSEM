# Event ID 4739: Domain Policy was changed.

## Description
This event generates when one of the following changes was made to local computer security policy: Computer's "\Security Settings\Account Policies\Account Lockout Policy" settings were modified. Computer's "\Security Settings\Account Policies\Password Policy" settings were modified. "Network security: Force logoff when logon hours expire" group policy setting was changed. Domain functional level was changed or some other attributes changed (see details in event description).

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|domain_policy_name|DomainPolicyChanged|TBD|string|the type of change which was made. The format is "policy_name modified".|Password Policy|
|domain_name|DomainName|TBD|string|the name of domain for which policy changes were made.|CONTOSO|
|domain_sid|DomainSid|TBD|string|the SID of domain for which policy changes were made.|S-1-5-21-3457937927-2839227994-823803824|
|user_sid|SubjectUserSid|TBD|string|SID of account that made a change to specific local policy.|S-1-5-18|
|user_name|SubjectUserName|TBD|string|the name of the account that made a change to specific local policy.|DC01$|
|user_domain|SubjectDomainName|TBD|strng|subject's domain or computer name.|CONTOSO|
|user_logon_id|SubjectLogonId|TBD|integer|hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID, for example, "4624: An account was successfully logged on."|0x3e7|
|user_privilege_list|PrivilegeList|TBD|string|the list of user privileges which were used during the operation, for example, SeBackupPrivilege.|-|
|password_policy_min_age|MinPasswordAge|TBD|string|"\Security Settings\Account Policies\Password Policy\Minimum password age" group policy. Numeric value.|-|
|password_policy_max_age|MaxPasswordAge|TBD|string|"\Security Settings\Account Policies\Password Policy\Maximum password age" group policy. Numeric value.|-|
|network_security_policy_force_logoff|ForceLogoff|TBD|string|"\Security Settings\Local Policies\Security Options\Network security: Force logoff when logon hours expire" group policy.|-|
|lockout_policy_threshold|LockoutThreshold|TBD|integer|"\Security Settings\Account Policies\Account Lockout Policy\Account lockout threshold" group policy. Numeric value.|-|
|lockout_policy_observation_window|LockoutObservationWindow|TBD|integer|"\Security Settings\Account Policies\Account Lockout Policy\Reset account lockout counter after" group policy. Numeric value.|-|
|lockout_policy_duration|LockoutDuration|TBD|integer|"\Security Settings\Account Policies\Account Lockout Policy\Account lockout duration" group policy. Numeric value.|-|
|password_policy_properties|PasswordProperties|TBD|integer||-|
|password_policy_min_length|MinPasswordLength|TBD|integer|"\Security Settings\Account Policies\Password Policy\Minimum password length" group policy. Numeric value.|-|
|password_policy_history_length|PasswordHistoryLength|TBD|integer|"\Security Settings\Account Policies\Password Policy\Enforce password history" group policy. Numeric value.|13|
|domain_policy_machine_account_quota|MachineAccountQuota|TBD|integer|ms-DS-MachineAccountQuota domain attribute was modified. Numeric value.|-|
|domain_policy_mixed_mode|MixedDomainMode|TBD|integer||-|
|domain_policy_behavior_version|DomainBehaviorVersion|TBD|integer|msDS-Behavior-Version domain attribute was modified. Numeric value.|-|
|TBD|OemInformation|TBD|string|not used. present for backward compatibility|-|

## Resources
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4739.md)
* [MS Security Auditing Category - Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#policy-change)
* [MS Security Auditing Sub-category - Audit Authentication Policy Change](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-authentication-policy-change.md)

## Tags
* Policy Change
* Audit Authentication Policy Change