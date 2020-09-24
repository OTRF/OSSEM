# user

Event fields used to define/normalize metadata about users in a network environment.

## Attributes

| Name | Type | Description | Sample Value |
|:---|:---|:---|:---|
 | user_aadid | string | The User Azure AD ID of the identity associated with a cloud network session. It applies to source and destination entities. | ```5e8b0f4d-2cd4-4e17-9467-b0f6a5c0c4d0``` |
 | user_cred_type | string | types of credentials which were presented for delegation | ```%%8098``` |
 | user_domain | string | The domain or computer name associated to the user in a session. In active directory, this would be the name of the domain the user belongs to. | ```CONTOSO``` |
 | user_identity | string | User Principal Name (UPN) or another type of account identifier for which 802.1x authentication request was made. | ```host/XXXXXXXX.redmond.corp.microsoft.com``` |
 | user_linked_logon_id | integer | A hexadecimal value of the paired logon session. | ```0x0``` |
 | user_logon_authentication_lan_package_name | string | The name of the LAN Manager sub-package (NTLM-family protocol name) that was used during logon. Possible values are: NTLM V1, NTLM V2, LM. Only populated if Authentication Package = NTLM. | ```-``` |
 | user_logon_authentication_package_name | string | The name of the authentication package which was used for the logon authentication process. Default packages loaded on LSA startup are located in "HKLM\SYSTEM\CurrentControlSet\Control\Lsa\OSConfig" registry key. Other packages can be loaded at runtime. When a new package is loaded a "4610: An authentication package has been loaded by the Local Security Authority" (typically for NTLM) or "4622: A security package has been loaded by the Local Security Authority" (typically for Kerberos) event is logged to indicate that a new package has been loaded along with the package name. | ```Negotiate``` |
 | user_logon_device_claims | string | list of device claims for new logon session | ```-``` |
 | user_logon_elevated_token | string | a "Yes" or "No" flag. If "Yes" then the session this event represents is elevated and has administrator privileges. | ```%%1842``` |
 | user_logon_guid | string | a GUID that can help you correlate this event with another event that can contain the same Logon GUID, "4769(S, F): A Kerberos service ticket was requested event on a domain controller. It also can be used for correlation between a 4624 event and several other events (on the same computer) that can contain the same Logon GUID, "4648(S): A logon was attempted using explicit credentials" and "4964(S): Special groups have been assigned to a new logon." | ```{00000000-0000-0000-0000-000000000000}``` |
 | user_logon_id | integer | hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID | ```0x8dcdc``` |
 | user_logon_impersonation_level | string | Impersonation level | ```%%1833``` |
 | user_logon_key_length | integer | the length of NTLM Session Security key. Typically it has 128 bit or 56 bit length. This parameter is always 0 if "Authentication Package" = "Kerberos", because it is not applicable for Kerberos protocol. This field will also have "0" value if Kerberos was negotiated using Negotiate authentication package. | ```0``` |
 | user_logon_process_name | string | The name of the trusted logon process that was used for the logon. See event "4611: A trusted logon process has been registered with the Local Security Authority" description for more information. | ```User32``` |
 | user_logon_restricted_admin_mode | string | Only populated for RemoteInteractive logon type sessions. This is a Yes/No flag indicating if the credentials provided were passed using Restricted Admin mode. Restricted Admin mode was added in Win8.1/2012R2 but this flag was added to the event in Win10. If not a RemoteInteractive logon, then this will be "-" string. | ```-``` |
 | user_logon_transmitted_services | string | the list of transmitted services. Transmitted services are populated if the logon was a result of a S4U (Service For User) logon process. S4U is a Microsoft extension to the Kerberos Protocol to allow an application service to obtain a Kerberos service ticket on behalf of a user - most commonly done by a front-end website to access an internal resource on behalf of a user. | ```-``` |
 | user_logon_type | integer | the type of logon which was performed | ```2``` |
 | user_logon_user_claims | string | list of user claims for new logon session. This field contains user claims if user account was logged in and device claims if computer account was logged in | ```ad://ext/cn:88d2b96fdb2b4c49 <%%1818> : "dadmin" ad://ext/Department:88d16a8edaa8c66b <%%1818> : "IT"``` |
 | user_logon_user_linked_id | integer | A hexadecimal value of the paired logon session. If there is no other logon session associated with this logon session, then the value is "0x0". | ```0x0``` |
 | user_logon_virtual_account | string | a "Yes" or "No" flag, which indicates if the account is a virtual account (e.g., "Managed Service Account"), which was introduced in Windows 7 and Windows Server 2008 R2 to provide the ability to identify the account that a given Service uses, instead of just using "NetworkService". | ```%%1843``` |
 | user_name | string | Name of the user associated with the main event (i.e. Network session). There could be a sense of direction depending how it is used together with other entities (i.e. src_user_name or dst_user_name) | ```wardog``` |
 | user_network_account_domain | string | Domain for the user that will be used for outbound (network) connections. | ```-``` |
 | user_network_account_name | string | User name used for outbound (network) connections | ```-``` |
 | user_password | string | User password if seen in the request. Commonly seen in network logs and authentication proxy/logs. | ```bobspassword``` |
 | user_reporter_domain | string | domain name of the user that reported the main event | ```WORKGROUP``` |
 | user_reporter_id | integer | unique identifier of the user that reported the main event | ```0x3e7``` |
 | user_reporter_name | string | the name of the account that reported information about the main event | ```WIN-GG82ULGC9GO$``` |
 | user_reporter_sid | string | SID of account that reported information about the main event | ```S-1-5-18``` |
 | user_security_package | string | the name of Security Package used during an authentication event. | ```CREDSSP``` |
 | user_session_id | integer | ID of the session the user belongs to. | ```1``` |
 | user_sid | string | Security identifier of the user. Typically, the identity used to authenticate a server. | ```S-1-5-21-1377283216-344919071-3415362939-500``` |
 | user_sid_list | string | the list of special group SIDs, which New Logon\Security ID is a member of. | ```{S-1-5-21-3457937927-2839227994-823803824-512}``` |
 | user_upn | string | In Active Directory, the User Principal Name (UPN) attribute is a user identifier for logging in, separate from a Windows domain login. | ```dadmin@contoso``` |
