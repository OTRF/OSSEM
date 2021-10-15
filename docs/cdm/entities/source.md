# source

Event fields used to define/normalize the source (client) in a network connection event.

## Attributes

| Name | Type | Description | Sample Value |
|:---|:---|:---|:---|
 | src_bytes | integer | The number of bytes sent from the source to the destination for the connection or session. | ```100``` |
 | src_domain_hostname | string | The source server, host, hostname, domain, or domain name. Some examples, would include the TLS server name, HTTP Host, DNS Query Name, etc. For information on how to define and use this field refer to the documentation [here](https://ossemproject.com/cdm/guidelines/domain_or_hostname_or_fqdn.html) | ```www.google.com``` |
 | src_dvc_action | string | If reported by an intermediary device such as a firewall, the action taken by device. | ```allow``` |
 | src_dvc_domain | string | Name of the domain the device is part of. | ```hunt.wardog.com``` |
 | src_dvc_fqdn | string | The fully qualified domain name of the host | ```WKHR001.hunt.wardog.com``` |
 | src_dvc_hostname | string | The host name from which the event/log came from. There may be multiple host names in an event (i.e. syslog could have forwarder host name), this field is to be the most true log host name (i.e. NOT the forwarders name). | ```bobs.uncle-pc``` |
 | src_dvc_inbound_interface | string | If reported by an intermediary device such as a firewall, the network interface used by it for the connection to the source device | ```eth0``` |
 | src_dvc_interface_guid | string | GUID of the network interface which was used for authentication request | ```{2BB33827-6BB6-48DB-8DE6-DB9E0B9F9C9B}``` |
 | src_dvc_interface_name | string | the name (description) of the network interface that was used for authentication request. You can get the list of all available network adapters using "ipconfig /all" command | ```Microsoft Hyper-V Network Adapter``` |
 | src_dvc_ip_addr | ip | IP address assigned to the device generating the event and/or the IP address in the network packet. This could be used in the context of source, destination, device and even NAT when it is provided by an intermediary NAT device such as a firewall. | ```192.168.1.2``` |
 | src_dvc_ip_dhcp_assigned_ip_addr | ip | IP address assigned by the DHCP server. | ```192.168.1.2``` |
 | src_dvc_ip_is_ipv6 | boolean | If IP address is IP version 6 | ```false``` |
 | src_dvc_mac_addr | string | MAC address of the device where the event was generated or network interface where a connection starts or ends. | ```00:11:22:33:44:55``` |
 | src_dvc_model_name | string | The model name of the device | ```Samsung Galaxy Note``` |
 | src_dvc_model_number | string | The model number of the device | ```10``` |
 | src_dvc_os | string | The OS of the device | ```iOS``` |
 | src_dvc_outbound_interface | string | If reported by an intermediary device such as a firewall, the network interface used by it for the connection to the destination device. | ```Ethernet 4``` |
 | src_dvc_type | string | The type of the device | ```mobile``` |
 | src_file_accessed_time | date | When the file was last accessed . Also known as `atime` | ```2016-11-25 18:21:47``` |
 | src_file_changed_time | date | When the file was last changed. Also known as `ctime` | ```2016-11-25 18:21:47``` |
 | src_file_company | string | Company name a file belongs to | ```Microsoft Corporation``` |
 | src_file_creation_time | date | When the file was created. Also known as `crtime` | ```2016-11-25 18:21:47``` |
 | src_file_description | string | Description of a file | ```Console Window Host``` |
 | src_file_directory | string | Directory of file(s). It does not include the file name | ```C:\users\wardog\``` |
 | src_file_extension | string | The extension name or type of the file. | ```exe``` |
 | src_file_hard_links | integer | Number of hard links | ```3``` |
 | src_file_hash_imphash | string | IMPHASH hash of the image/binary/file | ```2505BD03D7BD285E50CE89CEC02B333B``` |
 | src_file_hash_md5 | string | MD5 hash of the image/binary/file | ```6A255BEBF3DBCD13585538ED47DBAFD7``` |
 | src_file_hash_sha1 | string | SHA1 hash of the image/binary/file | ```B0BF5AC2E81BBF597FAD5F349FEEB32CAC449FA2``` |
 | src_file_hash_sha256 | string | SHA256 hash of the image/binary/file | ```4668BB2223FFB983A5F1273B9E3D9FA2C5CE4A0F1FB18CA5C1B285762020073C``` |
 | src_file_hash_sha512 | string | SHA512 hash of the image/binary/file | ```1AD1D79F85D8F6A50EA282F63898D652661DAA0C1FD361C22647CABC98A70E8CBCE83200D579D10DD0A3D46BE9496DCDFDDF28B0C5E9709343B032A8796FBECB``` |
 | src_file_inode | integer | Filesystem inode number | `````` |
 | src_file_link_name | string | path of the hard link | ```C:\Docs\My.exe``` |
 | src_file_mime_type | string | MIME type name specified for the file | ```application/msword``` |
 | src_file_modified_time | date | When the file was last modified. Also known as `mtime` | ```2016-11-25 18:21:47``` |
 | src_file_name | string | name of the file without its full path. This could be a local file or one transmitted over the network. | ```a.exe``` |
 | src_file_path | string | full path of a file including the name of the file. This could be a local file or one transmitted over the network. | ```C:\users\wardog\z.exe``` |
 | src_file_previous_accessed_time | date | When the file was previously accessed | ```2016-11-25 18:21:47``` |
 | src_file_previous_changed_time | date | When the file was previously changed | ```2016-11-25 18:21:47``` |
 | src_file_previous_creation_time | date | When the file was previously created | ```2016-11-25 18:21:47``` |
 | src_file_previous_modified_time | date | When the file was previously modified | ```2016-11-25 18:21:47``` |
 | src_file_previous_name | string | The file's previous name | ```cmd.exe``` |
 | src_file_previous_path | string | The file's previous path | ```C:\\Windows\system32\cmd.exe``` |
 | src_file_product | string | The file's product name | ```Microsoft® Windows® Operating System``` |
 | src_file_size | integer | Size of the file, in bytes. | ```45``` |
 | src_file_symlink | integer | 1 if the path is a symlink, otherwise 0 | ```0``` |
 | src_file_symlink_name | string | path of the symlink | ```C:\Docs\My.exe``` |
 | src_file_system_block_size | integer | Block size of filesystem | `````` |
 | src_file_system_type | string | The file system type, ex:  fat32, ntfs, vmfs, ext3, ext4, xfs | ```ntfs``` |
 | src_file_version | string | file version. i.e. image loaded version | ```10.0.16299.15 (WinBuild.160101.0800)``` |
 | src_geo_city | string | The city associated to the IP address in the network session. | ```San Miguel``` |
 | src_geo_continent | string | The continent associated with the IP address in the network session. | ```South America``` |
 | src_geo_country | string | The country associated with the IP address in the network session. | ```Peru``` |
 | src_geo_country_capital | string | The capital of the country associated with the IP address in the network session. | ```Lima``` |
 | src_geo_country_code | string | 51 | ```Country code``` |
 | src_geo_latitude | string | The latitude of the geographical coordinate associated with the IP address in the network session. | ```38.8951``` |
 | src_geo_longitude | string | The longitude of the geographical coordinate associated with the IP address in the network session. | ```-77.0364``` |
 | src_geo_region | string | The region within a country associated with the IP address in the network session. | ```East US``` |
 | src_interface_guid | string | GUID of the network interface which was used for authentication request (if applicable). Most of the time you would use the interface_name field for the uid. | ```7C202E90-2FBE-4275-AB0E-9BF67E04BEDF``` |
 | src_interface_name | string | The network interface used for the connection or session by the source device. | ```eth02``` |
 | src_ip_addr | ip | IP address assigned to the device generating the event and/or the IP address in the network packet. This could be used in the context of source, destination, device and even NAT when it is provided by an intermediary NAT device such as a firewall. | ```192.168.1.2``` |
 | src_ip_dhcp_assigned_ip_addr | ip | IP address assigned by the DHCP server. | ```192.168.1.2``` |
 | src_ip_is_ipv6 | boolean | If IP address is IP version 6 | ```false``` |
 | src_mac_addr | string | MAC address of the device where the event was generated or network interface where a connection starts or ends. | ```00:11:22:33:44:55``` |
 | src_mime_type | string | Source MIME type as seen in (layer 7) application layer details or as defined by an application scanner such as an anti-virus/EDR. For HTTP this is usually from the server's "Content-Type" header. https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Complete_list_of_MIME_types | ```application/pdf``` |
 | src_packets | integer | The number of packets sent from the source to the destination for the connection or session. The meaning of a packet is defined by the reporting device. | ```5``` |
 | src_port_name | string | Name of the port used in a network connection. This is usually determined by IANA common port assignment. Therefore, this means its a guess and NOT actually what the application/ is what the actually. | ```netbios-dgm``` |
 | src_port_number | integer | Port number used in a network connection. This could be used in the context of source, destination and even NAT when it is provided by an intermediary NAT device such as a firewall. | ```138``` |
 | src_process_call_trace | string | Stack trace of where open process is called | ```C:\WINDOWS\SYSTEM32\ntdll.dll+a0344 | C:\WINDOWS\System32\KERNELBASE.dll+64794| c:\windows\system32\lsm.dll+10e93| c:\windows\system32\lsm.dll+f9ea| C:\WINDOWS\System32\RPCRT4.dll+76d23| C:\WINDOWS\System32\RPCRT4.dll+d9390| C:\WINDOWS\System32\RPCRT4.dll+a81c| C:\WINDOWS\System32\RPCRT4.dll+273b4| C:\WINDOWS\System32\RPCRT4.dll+2654e| C:\WINDOWS\System32\RPCRT4.dll+26cfb| C:\WINDOWS\System32\RPCRT4.dll+3083f| C:\WINDOWS\System32\RPCRT4.dll+313a6| C:\WINDOWS\System32\RPCRT4.dll+2d12e| C:\WINDOWS\System32\RPCRT4.dll+2e853| C:\WINDOWS\System32\RPCRT4.dll+5cc68| C:\WINDOWS\SYSTEM32\ntdll.dll+365ce| C:\WINDOWS\SYSTEM32\ntdll.dll+34b46| C:\WINDOWS\System32\KERNEL32.DLL+11fe4| C:\WINDOWS\SYSTEM32\ntdll.dll+6efc1``` |
 | src_process_command_line | string | Command arguments that were were executed by the process in the endpoint. | ```C:\WINDOWS\system32\conhost.exe 0xffffffff -ForceV1``` |
 | src_process_company | string | Company name metadata of the Image file | ```Microsoft Corporation``` |
 | src_process_current_directory | string | The full path to the current directory for the process. The string can also specify a UNC path. | ```C:\Users\Panda\Test``` |
 | src_process_file_description | string | Description of the Image file | ```Console Window Host``` |
 | src_process_file_name | string | Name of the Image file or executable file used to define the initial code and data mapped into the process' virtual address space. This does not contain the full patth of the Image file. | ```conhost.exe``` |
 | src_process_file_path | string | The complete path and name of the Image file or executable file used to define the initial code and data mapped into the process' virtual address space. | ```C:\Windows\System32\conhost.exe``` |
 | src_process_file_product | string | The Image's file product name | ```Microsoft Windows Operating System``` |
 | src_process_file_version | string | Version of the Image file | ```10.0.16299.15 (WinBuild.160101.0800)``` |
 | src_process_granted_access | string | granted access code requested/used to open a target process | ```0x1000``` |
 | src_process_guid | string | Process global unique identifer used to identify a process across other operating systems. This can be created by group hashing values such as Process Name, Process Id, Process Start Time, Process Path and even Computer Name. Datasets such as Sysmon call this the ProcessGuid. This is similar to the output from the UUIDGEN command. | ```A98268C1-9C2E-5ACD-0000-0010396CAB00``` |
 | src_process_hash_imphash | string | IMPHASH hash of the image/binary/file | ```2505BD03D7BD285E50CE89CEC02B333B``` |
 | src_process_hash_md5 | string | MD5 hash of the image/binary/file | ```6A255BEBF3DBCD13585538ED47DBAFD7``` |
 | src_process_hash_sha1 | string | SHA1 hash of the image/binary/file | ```B0BF5AC2E81BBF597FAD5F349FEEB32CAC449FA2``` |
 | src_process_hash_sha256 | string | SHA256 hash of the image/binary/file | ```4668BB2223FFB983A5F1273B9E3D9FA2C5CE4A0F1FB18CA5C1B285762020073C``` |
 | src_process_hash_sha512 | string | SHA512 hash of the image/binary/file | ```1AD1D79F85D8F6A50EA282F63898D652661DAA0C1FD361C22647CABC98A70E8CBCE83200D579D10DD0A3D46BE9496DCDFDDF28B0C5E9709343B032A8796FBECB``` |
 | src_process_id | integer | Process unique identifier used by the current operating system to identify a process. | ```4756``` |
 | src_process_injected_address | string | The memory address where the subprocess is injected | ```0xFFFFBC6422DD9C20``` |
 | src_process_integrity_level | string | Integrity label assigned to a process | ```Medium``` |
 | src_process_is_hidden | boolean | Describes if the process is hidden. | ```True``` |
 | src_process_name | string | Name of the process derived from the Image file or executable file used to define the initial code and data mapped into the process' virtual address space. This does not contain the full patth of the Image file. | ```conhost.exe``` |
 | src_process_parent_call_trace | string | Stack trace of where open process is called | ```C:\WINDOWS\SYSTEM32\ntdll.dll+a0344 | C:\WINDOWS\System32\KERNELBASE.dll+64794| c:\windows\system32\lsm.dll+10e93| c:\windows\system32\lsm.dll+f9ea| C:\WINDOWS\System32\RPCRT4.dll+76d23| C:\WINDOWS\System32\RPCRT4.dll+d9390| C:\WINDOWS\System32\RPCRT4.dll+a81c| C:\WINDOWS\System32\RPCRT4.dll+273b4| C:\WINDOWS\System32\RPCRT4.dll+2654e| C:\WINDOWS\System32\RPCRT4.dll+26cfb| C:\WINDOWS\System32\RPCRT4.dll+3083f| C:\WINDOWS\System32\RPCRT4.dll+313a6| C:\WINDOWS\System32\RPCRT4.dll+2d12e| C:\WINDOWS\System32\RPCRT4.dll+2e853| C:\WINDOWS\System32\RPCRT4.dll+5cc68| C:\WINDOWS\SYSTEM32\ntdll.dll+365ce| C:\WINDOWS\SYSTEM32\ntdll.dll+34b46| C:\WINDOWS\System32\KERNEL32.DLL+11fe4| C:\WINDOWS\SYSTEM32\ntdll.dll+6efc1``` |
 | src_process_parent_command_line | string | Command arguments that were were executed by the process in the endpoint. | ```C:\WINDOWS\system32\conhost.exe 0xffffffff -ForceV1``` |
 | src_process_parent_company | string | Company name metadata of the Image file | ```Microsoft Corporation``` |
 | src_process_parent_current_directory | string | The full path to the current directory for the process. The string can also specify a UNC path. | ```C:\Users\Panda\Test``` |
 | src_process_parent_file_description | string | Description of the Image file | ```Console Window Host``` |
 | src_process_parent_file_name | string | Name of the Image file or executable file used to define the initial code and data mapped into the process' virtual address space. This does not contain the full patth of the Image file. | ```conhost.exe``` |
 | src_process_parent_file_path | string | The complete path and name of the Image file or executable file used to define the initial code and data mapped into the process' virtual address space. | ```C:\Windows\System32\conhost.exe``` |
 | src_process_parent_file_product | string | The Image's file product name | ```Microsoft Windows Operating System``` |
 | src_process_parent_file_version | string | Version of the Image file | ```10.0.16299.15 (WinBuild.160101.0800)``` |
 | src_process_parent_granted_access | string | granted access code requested/used to open a target process | ```0x1000``` |
 | src_process_parent_guid | string | Process global unique identifer used to identify a process across other operating systems. This can be created by group hashing values such as Process Name, Process Id, Process Start Time, Process Path and even Computer Name. Datasets such as Sysmon call this the ProcessGuid. This is similar to the output from the UUIDGEN command. | ```A98268C1-9C2E-5ACD-0000-0010396CAB00``` |
 | src_process_parent_hash_imphash | string | IMPHASH hash of the image/binary/file | ```2505BD03D7BD285E50CE89CEC02B333B``` |
 | src_process_parent_hash_md5 | string | MD5 hash of the image/binary/file | ```6A255BEBF3DBCD13585538ED47DBAFD7``` |
 | src_process_parent_hash_sha1 | string | SHA1 hash of the image/binary/file | ```B0BF5AC2E81BBF597FAD5F349FEEB32CAC449FA2``` |
 | src_process_parent_hash_sha256 | string | SHA256 hash of the image/binary/file | ```4668BB2223FFB983A5F1273B9E3D9FA2C5CE4A0F1FB18CA5C1B285762020073C``` |
 | src_process_parent_hash_sha512 | string | SHA512 hash of the image/binary/file | ```1AD1D79F85D8F6A50EA282F63898D652661DAA0C1FD361C22647CABC98A70E8CBCE83200D579D10DD0A3D46BE9496DCDFDDF28B0C5E9709343B032A8796FBECB``` |
 | src_process_parent_id | integer | Process unique identifier used by the current operating system to identify a process. | ```4756``` |
 | src_process_parent_injected_address | string | The memory address where the subprocess is injected | ```0xFFFFBC6422DD9C20``` |
 | src_process_parent_integrity_level | string | Integrity label assigned to a process | ```Medium``` |
 | src_process_parent_is_hidden | boolean | Describes if the process is hidden. | ```True``` |
 | src_process_parent_name | string | Name of the process derived from the Image file or executable file used to define the initial code and data mapped into the process' virtual address space. This does not contain the full patth of the Image file. | ```conhost.exe``` |
 | src_resource_group | string | The ID of the group to which the source device belongs in a network connection. This might be an AWS account, or an Azure subscription or Resource Group | ```DatabaseVMs``` |
 | src_resource_id | string | The resource Id of the source device in a network connection | ```/subscriptions/33333333-8888-4444-a115-aaaaaaaaaaaa/resourcegroups/shokobo/providers/microsoft.compute/virtualmachines/sysmachine2``` |
 | src_user_aadid | string | The User Azure AD ID of the identity associated with a cloud network session. It applies to source and destination entities. | ```5e8b0f4d-2cd4-4e17-9467-b0f6a5c0c4d0``` |
 | src_user_cred_type | string | types of credentials which were presented for delegation | ```%%8098``` |
 | src_user_domain | string | The domain or computer name associated to the user in a session. In active directory, this would be the name of the domain the user belongs to. | ```CONTOSO``` |
 | src_user_identity | string | User Principal Name (UPN) or another type of account identifier for which 802.1x authentication request was made. | ```host/XXXXXXXX.redmond.corp.microsoft.com``` |
 | src_user_linked_logon_id | integer | A hexadecimal value of the paired logon session. | ```0x0``` |
 | src_user_logon_authentication_lan_package_name | string | The name of the LAN Manager sub-package (NTLM-family protocol name) that was used during logon. Possible values are: NTLM V1, NTLM V2, LM. Only populated if Authentication Package = NTLM. | ```-``` |
 | src_user_logon_authentication_package_name | string | The name of the authentication package which was used for the logon authentication process. Default packages loaded on LSA startup are located in "HKLM\SYSTEM\CurrentControlSet\Control\Lsa\OSConfig" registry key. Other packages can be loaded at runtime. When a new package is loaded a "4610: An authentication package has been loaded by the Local Security Authority" (typically for NTLM) or "4622: A security package has been loaded by the Local Security Authority" (typically for Kerberos) event is logged to indicate that a new package has been loaded along with the package name. | ```Negotiate``` |
 | src_user_logon_device_claims | string | list of device claims for new logon session | ```-``` |
 | src_user_logon_elevated_token | string | a "Yes" or "No" flag. If "Yes" then the session this event represents is elevated and has administrator privileges. | ```%%1842``` |
 | src_user_logon_guid | string | a GUID that can help you correlate this event with another event that can contain the same Logon GUID, "4769(S, F): A Kerberos service ticket was requested event on a domain controller. It also can be used for correlation between a 4624 event and several other events (on the same computer) that can contain the same Logon GUID, "4648(S): A logon was attempted using explicit credentials" and "4964(S): Special groups have been assigned to a new logon." | ```{00000000-0000-0000-0000-000000000000}``` |
 | src_user_logon_id | integer | hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID | ```0x8dcdc``` |
 | src_user_logon_impersonation_level | string | Impersonation level | ```%%1833``` |
 | src_user_logon_key_length | integer | the length of NTLM Session Security key. Typically it has 128 bit or 56 bit length. This parameter is always 0 if "Authentication Package" = "Kerberos", because it is not applicable for Kerberos protocol. This field will also have "0" value if Kerberos was negotiated using Negotiate authentication package. | ```0``` |
 | src_user_logon_process_name | string | The name of the trusted logon process that was used for the logon. See event "4611: A trusted logon process has been registered with the Local Security Authority" description for more information. | ```User32``` |
 | src_user_logon_restricted_admin_mode | string | Only populated for RemoteInteractive logon type sessions. This is a Yes/No flag indicating if the credentials provided were passed using Restricted Admin mode. Restricted Admin mode was added in Win8.1/2012R2 but this flag was added to the event in Win10. If not a RemoteInteractive logon, then this will be "-" string. | ```-``` |
 | src_user_logon_transmitted_services | string | the list of transmitted services. Transmitted services are populated if the logon was a result of a S4U (Service For User) logon process. S4U is a Microsoft extension to the Kerberos Protocol to allow an application service to obtain a Kerberos service ticket on behalf of a user - most commonly done by a front-end website to access an internal resource on behalf of a user. | ```-``` |
 | src_user_logon_type | integer | the type of logon which was performed | ```2``` |
 | src_user_logon_user_claims | string | list of user claims for new logon session. This field contains user claims if user account was logged in and device claims if computer account was logged in | ```ad://ext/cn:88d2b96fdb2b4c49 <%%1818> : "dadmin" ad://ext/Department:88d16a8edaa8c66b <%%1818> : "IT"``` |
 | src_user_logon_user_linked_id | integer | A hexadecimal value of the paired logon session. If there is no other logon session associated with this logon session, then the value is "0x0". | ```0x0``` |
 | src_user_logon_virtual_account | string | a "Yes" or "No" flag, which indicates if the account is a virtual account (e.g., "Managed Service Account"), which was introduced in Windows 7 and Windows Server 2008 R2 to provide the ability to identify the account that a given Service uses, instead of just using "NetworkService". | ```%%1843``` |
 | src_user_name | string | Name of the user associated with the main event (i.e. Network session). There could be a sense of direction depending how it is used together with other entities (i.e. src_user_name or dst_user_name) | ```wardog``` |
 | src_user_network_account_domain | string | Domain for the user that will be used for outbound (network) connections. | ```-``` |
 | src_user_network_account_name | string | User name used for outbound (network) connections | ```-``` |
 | src_user_password | string | User password if seen in the request. Commonly seen in network logs and authentication proxy/logs. | ```bobspassword``` |
 | src_user_reporter_domain | string | domain name of the user that reported the main event | ```WORKGROUP``` |
 | src_user_reporter_id | integer | unique identifier of the user that reported the main event | ```0x3e7``` |
 | src_user_reporter_name | string | the name of the account that reported information about the main event | ```WIN-GG82ULGC9GO$``` |
 | src_user_reporter_sid | string | SID of account that reported information about the main event | ```S-1-5-18``` |
 | src_user_security_package | string | the name of Security Package used during an authentication event. | ```CREDSSP``` |
 | src_user_session_id | integer | ID of the session the user belongs to. | ```1``` |
 | src_user_sid | string | Security identifier of the user. Typically, the identity used to authenticate a server. | ```S-1-5-21-1377283216-344919071-3415362939-500``` |
 | src_user_sid_list | string | the list of special group SIDs, which New Logon\Security ID is a member of. | ```{S-1-5-21-3457937927-2839227994-823803824-512}``` |
 | src_user_upn | string | In Active Directory, the User Principal Name (UPN) attribute is a user identifier for logging in, separate from a Windows domain login. | ```dadmin@contoso``` |
 | src_vlan_id | integer | The Source VLAN ID if it can be determined. Most commonly if from a firewall/switch/router then it can be determined | ```100``` |
 | src_vlan_name | string | The Source VLAN Name. Most commonly if from a firewall/switch/router then it can be determined | ```management``` |
 | src_zone | string | The network zone of the source, as defined by the reporting device. | ```dmz``` |
