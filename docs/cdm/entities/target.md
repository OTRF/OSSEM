# target

Event fields used to define entities being targeted by other entities locally in a system. This is different from a network connection event. It is more related to events that involve relationships defined locally by entities such as files, processes,users, etc.

## Attributes

| Name | Type | Description | Sample Value |
|:---|:---|:---|:---|
 | target_process_call_trace | string | Stack trace of where open process is called | ```C:\WINDOWS\SYSTEM32\ntdll.dll+a0344 | C:\WINDOWS\System32\KERNELBASE.dll+64794| c:\windows\system32\lsm.dll+10e93| c:\windows\system32\lsm.dll+f9ea| C:\WINDOWS\System32\RPCRT4.dll+76d23| C:\WINDOWS\System32\RPCRT4.dll+d9390| C:\WINDOWS\System32\RPCRT4.dll+a81c| C:\WINDOWS\System32\RPCRT4.dll+273b4| C:\WINDOWS\System32\RPCRT4.dll+2654e| C:\WINDOWS\System32\RPCRT4.dll+26cfb| C:\WINDOWS\System32\RPCRT4.dll+3083f| C:\WINDOWS\System32\RPCRT4.dll+313a6| C:\WINDOWS\System32\RPCRT4.dll+2d12e| C:\WINDOWS\System32\RPCRT4.dll+2e853| C:\WINDOWS\System32\RPCRT4.dll+5cc68| C:\WINDOWS\SYSTEM32\ntdll.dll+365ce| C:\WINDOWS\SYSTEM32\ntdll.dll+34b46| C:\WINDOWS\System32\KERNEL32.DLL+11fe4| C:\WINDOWS\SYSTEM32\ntdll.dll+6efc1``` |
 | target_process_command_line | string | Command arguments that were were executed by the process in the endpoint. | ```C:\WINDOWS\system32\conhost.exe 0xffffffff -ForceV1``` |
 | target_process_company | string | Company name metadata of the Image file | ```Microsoft Corporation``` |
 | target_process_current_directory | string | The full path to the current directory for the process. The string can also specify a UNC path. | ```C:\Users\Panda\Test``` |
 | target_process_file_description | string | Description of the Image file | ```Console Window Host``` |
 | target_process_file_name | string | Name of the Image file or executable file used to define the initial code and data mapped into the process' virtual address space. This does not contain the full patth of the Image file. | ```conhost.exe``` |
 | target_process_file_path | string | The complete path and name of the Image file or executable file used to define the initial code and data mapped into the process' virtual address space. | ```C:\Windows\System32\conhost.exe``` |
 | target_process_file_product | string | The Image's file product name | ```Microsoft Windows Operating System``` |
 | target_process_file_version | string | Version of the Image file | ```10.0.16299.15 (WinBuild.160101.0800)``` |
 | target_process_granted_access | string | granted access code requested/used to open a target process | ```0x1000``` |
 | target_process_guid | string | Process global unique identifer used to identify a process across other operating systems. This can be created by group hashing values such as Process Name, Process Id, Process Start Time, Process Path and even Computer Name. Datasets such as Sysmon call this the ProcessGuid. This is similar to the output from the UUIDGEN command. | ```A98268C1-9C2E-5ACD-0000-0010396CAB00``` |
 | target_process_hash_imphash | string | IMPHASH hash of the image/binary/file | ```2505BD03D7BD285E50CE89CEC02B333B``` |
 | target_process_hash_md5 | string | MD5 hash of the image/binary/file | ```6A255BEBF3DBCD13585538ED47DBAFD7``` |
 | target_process_hash_sha1 | string | SHA1 hash of the image/binary/file | ```B0BF5AC2E81BBF597FAD5F349FEEB32CAC449FA2``` |
 | target_process_hash_sha256 | string | SHA256 hash of the image/binary/file | ```4668BB2223FFB983A5F1273B9E3D9FA2C5CE4A0F1FB18CA5C1B285762020073C``` |
 | target_process_hash_sha512 | string | SHA512 hash of the image/binary/file | ```1AD1D79F85D8F6A50EA282F63898D652661DAA0C1FD361C22647CABC98A70E8CBCE83200D579D10DD0A3D46BE9496DCDFDDF28B0C5E9709343B032A8796FBECB``` |
 | target_process_id | integer | Process unique identifier used by the current operating system to identify a process. | ```4756``` |
 | target_process_injected_address | string | The memory address where the subprocess is injected | ```0xFFFFBC6422DD9C20``` |
 | target_process_integrity_level | string | Integrity label assigned to a process | ```Medium``` |
 | target_process_is_hidden | boolean | Describes if the process is hidden. | ```True``` |
 | target_process_name | string | Name of the process derived from the Image file or executable file used to define the initial code and data mapped into the process' virtual address space. This does not contain the full patth of the Image file. | ```conhost.exe``` |
 | target_process_parent_call_trace | string | Stack trace of where open process is called | ```C:\WINDOWS\SYSTEM32\ntdll.dll+a0344 | C:\WINDOWS\System32\KERNELBASE.dll+64794| c:\windows\system32\lsm.dll+10e93| c:\windows\system32\lsm.dll+f9ea| C:\WINDOWS\System32\RPCRT4.dll+76d23| C:\WINDOWS\System32\RPCRT4.dll+d9390| C:\WINDOWS\System32\RPCRT4.dll+a81c| C:\WINDOWS\System32\RPCRT4.dll+273b4| C:\WINDOWS\System32\RPCRT4.dll+2654e| C:\WINDOWS\System32\RPCRT4.dll+26cfb| C:\WINDOWS\System32\RPCRT4.dll+3083f| C:\WINDOWS\System32\RPCRT4.dll+313a6| C:\WINDOWS\System32\RPCRT4.dll+2d12e| C:\WINDOWS\System32\RPCRT4.dll+2e853| C:\WINDOWS\System32\RPCRT4.dll+5cc68| C:\WINDOWS\SYSTEM32\ntdll.dll+365ce| C:\WINDOWS\SYSTEM32\ntdll.dll+34b46| C:\WINDOWS\System32\KERNEL32.DLL+11fe4| C:\WINDOWS\SYSTEM32\ntdll.dll+6efc1``` |
 | target_process_parent_command_line | string | Command arguments that were were executed by the process in the endpoint. | ```C:\WINDOWS\system32\conhost.exe 0xffffffff -ForceV1``` |
 | target_process_parent_company | string | Company name metadata of the Image file | ```Microsoft Corporation``` |
 | target_process_parent_current_directory | string | The full path to the current directory for the process. The string can also specify a UNC path. | ```C:\Users\Panda\Test``` |
 | target_process_parent_file_description | string | Description of the Image file | ```Console Window Host``` |
 | target_process_parent_file_name | string | Name of the Image file or executable file used to define the initial code and data mapped into the process' virtual address space. This does not contain the full patth of the Image file. | ```conhost.exe``` |
 | target_process_parent_file_path | string | The complete path and name of the Image file or executable file used to define the initial code and data mapped into the process' virtual address space. | ```C:\Windows\System32\conhost.exe``` |
 | target_process_parent_file_product | string | The Image's file product name | ```Microsoft Windows Operating System``` |
 | target_process_parent_file_version | string | Version of the Image file | ```10.0.16299.15 (WinBuild.160101.0800)``` |
 | target_process_parent_granted_access | string | granted access code requested/used to open a target process | ```0x1000``` |
 | target_process_parent_guid | string | Process global unique identifer used to identify a process across other operating systems. This can be created by group hashing values such as Process Name, Process Id, Process Start Time, Process Path and even Computer Name. Datasets such as Sysmon call this the ProcessGuid. This is similar to the output from the UUIDGEN command. | ```A98268C1-9C2E-5ACD-0000-0010396CAB00``` |
 | target_process_parent_hash_imphash | string | IMPHASH hash of the image/binary/file | ```2505BD03D7BD285E50CE89CEC02B333B``` |
 | target_process_parent_hash_md5 | string | MD5 hash of the image/binary/file | ```6A255BEBF3DBCD13585538ED47DBAFD7``` |
 | target_process_parent_hash_sha1 | string | SHA1 hash of the image/binary/file | ```B0BF5AC2E81BBF597FAD5F349FEEB32CAC449FA2``` |
 | target_process_parent_hash_sha256 | string | SHA256 hash of the image/binary/file | ```4668BB2223FFB983A5F1273B9E3D9FA2C5CE4A0F1FB18CA5C1B285762020073C``` |
 | target_process_parent_hash_sha512 | string | SHA512 hash of the image/binary/file | ```1AD1D79F85D8F6A50EA282F63898D652661DAA0C1FD361C22647CABC98A70E8CBCE83200D579D10DD0A3D46BE9496DCDFDDF28B0C5E9709343B032A8796FBECB``` |
 | target_process_parent_id | integer | Process unique identifier used by the current operating system to identify a process. | ```4756``` |
 | target_process_parent_injected_address | string | The memory address where the subprocess is injected | ```0xFFFFBC6422DD9C20``` |
 | target_process_parent_integrity_level | string | Integrity label assigned to a process | ```Medium``` |
 | target_process_parent_is_hidden | boolean | Describes if the process is hidden. | ```True``` |
 | target_process_parent_name | string | Name of the process derived from the Image file or executable file used to define the initial code and data mapped into the process' virtual address space. This does not contain the full patth of the Image file. | ```conhost.exe``` |
 | target_server_name | string | the name of the server on which the new process was run. Has "localhost" value if the process was run locally. | ```localhost``` |
 | target_user_aadid | string | The User Azure AD ID of the identity associated with a cloud network session. It applies to source and destination entities. | ```5e8b0f4d-2cd4-4e17-9467-b0f6a5c0c4d0``` |
 | target_user_cred_type | string | types of credentials which were presented for delegation | ```%%8098``` |
 | target_user_domain | string | The domain or computer name associated to the user in a session. In active directory, this would be the name of the domain the user belongs to. | ```CONTOSO``` |
 | target_user_identity | string | User Principal Name (UPN) or another type of account identifier for which 802.1x authentication request was made. | ```host/XXXXXXXX.redmond.corp.microsoft.com``` |
 | target_user_linked_logon_id | integer | A hexadecimal value of the paired logon session. | ```0x0``` |
 | target_user_logon_authentication_lan_package_name | string | The name of the LAN Manager sub-package (NTLM-family protocol name) that was used during logon. Possible values are: NTLM V1, NTLM V2, LM. Only populated if Authentication Package = NTLM. | ```-``` |
 | target_user_logon_authentication_package_name | string | The name of the authentication package which was used for the logon authentication process. Default packages loaded on LSA startup are located in "HKLM\SYSTEM\CurrentControlSet\Control\Lsa\OSConfig" registry key. Other packages can be loaded at runtime. When a new package is loaded a "4610: An authentication package has been loaded by the Local Security Authority" (typically for NTLM) or "4622: A security package has been loaded by the Local Security Authority" (typically for Kerberos) event is logged to indicate that a new package has been loaded along with the package name. | ```Negotiate``` |
 | target_user_logon_device_claims | string | list of device claims for new logon session | ```-``` |
 | target_user_logon_elevated_token | string | a "Yes" or "No" flag. If "Yes" then the session this event represents is elevated and has administrator privileges. | ```%%1842``` |
 | target_user_logon_guid | string | a GUID that can help you correlate this event with another event that can contain the same Logon GUID, "4769(S, F): A Kerberos service ticket was requested event on a domain controller. It also can be used for correlation between a 4624 event and several other events (on the same computer) that can contain the same Logon GUID, "4648(S): A logon was attempted using explicit credentials" and "4964(S): Special groups have been assigned to a new logon." | ```{00000000-0000-0000-0000-000000000000}``` |
 | target_user_logon_id | integer | hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID | ```0x8dcdc``` |
 | target_user_logon_impersonation_level | string | Impersonation level | ```%%1833``` |
 | target_user_logon_key_length | integer | the length of NTLM Session Security key. Typically it has 128 bit or 56 bit length. This parameter is always 0 if "Authentication Package" = "Kerberos", because it is not applicable for Kerberos protocol. This field will also have "0" value if Kerberos was negotiated using Negotiate authentication package. | ```0``` |
 | target_user_logon_process_name | string | The name of the trusted logon process that was used for the logon. See event "4611: A trusted logon process has been registered with the Local Security Authority" description for more information. | ```User32``` |
 | target_user_logon_restricted_admin_mode | string | Only populated for RemoteInteractive logon type sessions. This is a Yes/No flag indicating if the credentials provided were passed using Restricted Admin mode. Restricted Admin mode was added in Win8.1/2012R2 but this flag was added to the event in Win10. If not a RemoteInteractive logon, then this will be "-" string. | ```-``` |
 | target_user_logon_transmitted_services | string | the list of transmitted services. Transmitted services are populated if the logon was a result of a S4U (Service For User) logon process. S4U is a Microsoft extension to the Kerberos Protocol to allow an application service to obtain a Kerberos service ticket on behalf of a user - most commonly done by a front-end website to access an internal resource on behalf of a user. | ```-``` |
 | target_user_logon_type | integer | the type of logon which was performed | ```2``` |
 | target_user_logon_user_claims | string | list of user claims for new logon session. This field contains user claims if user account was logged in and device claims if computer account was logged in | ```ad://ext/cn:88d2b96fdb2b4c49 <%%1818> : "dadmin" ad://ext/Department:88d16a8edaa8c66b <%%1818> : "IT"``` |
 | target_user_logon_user_linked_id | integer | A hexadecimal value of the paired logon session. If there is no other logon session associated with this logon session, then the value is "0x0". | ```0x0``` |
 | target_user_logon_virtual_account | string | a "Yes" or "No" flag, which indicates if the account is a virtual account (e.g., "Managed Service Account"), which was introduced in Windows 7 and Windows Server 2008 R2 to provide the ability to identify the account that a given Service uses, instead of just using "NetworkService". | ```%%1843``` |
 | target_user_name | string | Name of the user associated with the main event (i.e. Network session). There could be a sense of direction depending how it is used together with other entities (i.e. src_user_name or dst_user_name) | ```wardog``` |
 | target_user_network_account_domain | string | Domain for the user that will be used for outbound (network) connections. | ```-``` |
 | target_user_network_account_name | string | User name used for outbound (network) connections | ```-``` |
 | target_user_password | string | User password if seen in the request. Commonly seen in network logs and authentication proxy/logs. | ```bobspassword``` |
 | target_user_reporter_domain | string | domain name of the user that reported the main event | ```WORKGROUP``` |
 | target_user_reporter_id | integer | unique identifier of the user that reported the main event | ```0x3e7``` |
 | target_user_reporter_name | string | the name of the account that reported information about the main event | ```WIN-GG82ULGC9GO$``` |
 | target_user_reporter_sid | string | SID of account that reported information about the main event | ```S-1-5-18``` |
 | target_user_security_package | string | the name of Security Package used during an authentication event. | ```CREDSSP``` |
 | target_user_session_id | integer | ID of the session the user belongs to. | ```1``` |
 | target_user_sid | string | Security identifier of the user. Typically, the identity used to authenticate a server. | ```S-1-5-21-1377283216-344919071-3415362939-500``` |
 | target_user_sid_list | string | the list of special group SIDs, which New Logon\Security ID is a member of. | ```{S-1-5-21-3457937927-2839227994-823803824-512}``` |
 | target_user_upn | string | In Active Directory, the User Principal Name (UPN) attribute is a user identifier for logging in, separate from a Windows domain login. | ```dadmin@contoso``` |
