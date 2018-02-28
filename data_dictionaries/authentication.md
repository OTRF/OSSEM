# Authentication Data Dictionary

Security events that are generated when a user attempts to logon to a computer.

## Data sources schema applies to

| OS | Data source | Event ID | Description |
|--------|---------|-------|---------|
| Windows | Security | 4624 | An account was successfully logged on |
| Windows | Security | 4648 | A logon was attempted using explicit credential |

## References

* https://github.com/MicrosoftDocs/windows-itpro-docs/blob/master/windows/security/threat-protection/auditing/audit-logon.md

## Data Fields

| field name | field type | description | valid values |
|--------|---------|-------|---------|
| reporter_user_sid | string | SID of account that reported information about successful logon or invokes it | S-1-5-18 |
| reporter_user_name | string | Name of the account that reported information about successful logon | WIN-GG82ULGC9GO$ |
| reporter_user_domain | string | Domain name of the account that reported information about successful logon | WORKGROUP |
| reporter_user_logon_id | string | The name of a process. Considered also the child or source process in the event | 0x3e7 |
| user_name | string | Name of the account for which logon was performed | Administrator |
| user_domain | string | Domain name of the account for which logon was performed | WIN-GG82ULGC9GO |
| user_logon_id | string | Value that can help you correlate this event with recent events that might contain the same Logon ID | 0x8dcdc |
| user_logon_guid | GUID that can help you correlate this event with another event that can contain the same Logon GUID | 00000000-0000-0000-0000-000000000000 |
| logon_type | string | the type of logon which was performed | 3|
| logon_process_name | string | Name of the trusted logon process that was used for the logon | User32 |
| process_id | string | Process ID of the process that attempted the logon | 0x44 |
| process_path | string | Full path and the name of the executable for the process that attempted the logon | C:\Windows\System32\svchost.exe |
| logon_authentication_package | string | The name of the authentication package which was used for the logon authentication process | Negotiate |
| src_host | string | Machine name from which logon attempt was performed | WIN-GG82ULGC9GO |
| logon_transmitted_services | string | List of transmitted services. Transmitted services are populated if the logon was a result of a S4U (Service For User) logon process | - |
| host_name | string | Machine where the log gets created | WK002 |
| logon_package_name | string | The name of the LAN Manager sub-package (NTLM-family protocol name) that was used during logon | LM |
| logon_key_lenght | string | the length of NTLM Session Security key. Typically it has 128 bit or 56 bit length. This parameter is always 0 if “Authentication Package” = “Kerberos”, because it is not applicable for Kerberos protocol | 128 |
| src_ip | string | IP address of machine from which logon attempt was performed | 10.0.0.1 |
| src_port_number | string | source port which was used for logon attempt from remote machine | 0 |
| impersonation_level | string | impersonation level | %%183 |
| logon_restricted_adminmode | string | Only populated for RemoteInteractive logon type sessions. This is a Yes/No flag indicating if the credentials provided were passed using Restricted Admin mode. Restricted Admin mode was added in Win8.1/2012R2 but this flag was added to the event in Win10 | yes |
| virtual_account | string | a “Yes” or “No” flag, which indicates if the account is a virtual account (e.g., "Managed Service Account"), which was introduced in Windows 7 and Windows Server 2008 R2 to provide the ability to identify the account that a given Service uses, instead of just using "NetworkService" | yes |
| elevated_token | string | “Yes” or “No” flag. If “Yes” then the session this event represents is elevated and has administrator privileges | yes |