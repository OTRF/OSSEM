# destination

Event fields used to define/normalize the destination (server) in a network connection event.

## Attributes

| Name | Type | Description | Sample Value |
|:---|:---|:---|:---|
 | dst_bytes | integer | The number of bytes sent from the destination to the source for the connection or session. | ```100``` |
 | dst_certificate_hash_imphash | string | IMPHASH hash of the image/binary/file | ```2505BD03D7BD285E50CE89CEC02B333B``` |
 | dst_certificate_hash_md5 | string | MD5 hash of the image/binary/file | ```6A255BEBF3DBCD13585538ED47DBAFD7``` |
 | dst_certificate_hash_sha1 | string | SHA1 hash of the image/binary/file | ```B0BF5AC2E81BBF597FAD5F349FEEB32CAC449FA2``` |
 | dst_certificate_hash_sha256 | string | SHA256 hash of the image/binary/file | ```4668BB2223FFB983A5F1273B9E3D9FA2C5CE4A0F1FB18CA5C1B285762020073C``` |
 | dst_certificate_hash_sha512 | string | SHA512 hash of the image/binary/file | ```1AD1D79F85D8F6A50EA282F63898D652661DAA0C1FD361C22647CABC98A70E8CBCE83200D579D10DD0A3D46BE9496DCDFDDF28B0C5E9709343B032A8796FBECB``` |
 | dst_certificate_issuer | string | Information about the CA that issued the certificate | ```CN=neu5ron.local,OU=Admin``` |
 | dst_certificate_serial_number | string | Serial number, this is chosen by the CA (certificate authority) which issued the certificate. Therefore this can relatively be arbritary if the CA does not follow a standard or is malicious. | ```5157550``` |
 | dst_certificate_subject | string | Information about the CA that issued the certificate | ```CN=natetoken,OU=Admin,DC=neu5ron,DC=local``` |
 | dst_domain_hostname | string | The destination server, host, hostname, domain, domain name or what people commonly might refer to as a domain or website when someone is browsing the Internet. Some examples, would include the TLS server name, HTTP Host, DNS Query Name, etc. For information on how to define and use this field refer to the documentation [here](https://ossemproject.com/cdm/guidelines/domain_or_hostname_or_fqdn.html) | ```www.google.com``` |
 | dst_dvc_action | string | If reported by an intermediary device such as a firewall, the action taken by device. | ```allow``` |
 | dst_dvc_domain | string | Name of the domain the device is part of. | ```hunt.wardog.com``` |
 | dst_dvc_fqdn | string | The fully qualified domain name of the host | ```WKHR001.hunt.wardog.com``` |
 | dst_dvc_hostname | string | The host name from which the event/log came from. There may be multiple host names in an event (i.e. syslog could have forwarder host name), this field is to be the most true log host name (i.e. NOT the forwarders name). | ```bobs.uncle-pc``` |
 | dst_dvc_inbound_interface | string | If reported by an intermediary device such as a firewall, the network interface used by it for the connection to the source device | ```eth0``` |
 | dst_dvc_interface_guid | string | GUID of the network interface which was used for authentication request | ```{2BB33827-6BB6-48DB-8DE6-DB9E0B9F9C9B}``` |
 | dst_dvc_interface_name | string | the name (description) of the network interface that was used for authentication request. You can get the list of all available network adapters using "ipconfig /all" command | ```Microsoft Hyper-V Network Adapter``` |
 | dst_dvc_ip_addr | ip | IP address assigned to the device generating the event and/or the IP address in the network packet. This could be used in the context of source, destination, device and even NAT when it is provided by an intermediary NAT device such as a firewall. | ```192.168.1.2``` |
 | dst_dvc_ip_dhcp_assigned_ip_addr | ip | IP address assigned by the DHCP server. | ```192.168.1.2``` |
 | dst_dvc_ip_is_ipv6 | boolean | If IP address is IP version 6 | ```false``` |
 | dst_dvc_mac_addr | string | MAC address of the device where the event was generated or network interface where a connection starts or ends. | ```00:11:22:33:44:55``` |
 | dst_dvc_model_name | string | The model name of the device | ```Samsung Galaxy Note``` |
 | dst_dvc_model_number | string | The model number of the device | ```10``` |
 | dst_dvc_os | string | The OS of the device | ```iOS``` |
 | dst_dvc_outbound_interface | string | If reported by an intermediary device such as a firewall, the network interface used by it for the connection to the destination device. | ```Ethernet 4``` |
 | dst_dvc_type | string | The type of the device | ```mobile``` |
 | dst_file_accessed_time | date | When the file was last accessed . Also known as `atime` | ```2016-11-25 18:21:47``` |
 | dst_file_changed_time | date | When the file was last changed. Also known as `ctime` | ```2016-11-25 18:21:47``` |
 | dst_file_company | string | Company name a file belongs to | ```Microsoft Corporation``` |
 | dst_file_creation_time | date | When the file was created. Also known as `crtime` | ```2016-11-25 18:21:47``` |
 | dst_file_description | string | Description of a file | ```Console Window Host``` |
 | dst_file_directory | string | Directory of file(s). It does not include the file name | ```C:\users\wardog\``` |
 | dst_file_extension | string | The extension name or type of the file. | ```exe``` |
 | dst_file_hard_links | integer | Number of hard links | ```3``` |
 | dst_file_hash_imphash | string | IMPHASH hash of the image/binary/file | ```2505BD03D7BD285E50CE89CEC02B333B``` |
 | dst_file_hash_md5 | string | MD5 hash of the image/binary/file | ```6A255BEBF3DBCD13585538ED47DBAFD7``` |
 | dst_file_hash_sha1 | string | SHA1 hash of the image/binary/file | ```B0BF5AC2E81BBF597FAD5F349FEEB32CAC449FA2``` |
 | dst_file_hash_sha256 | string | SHA256 hash of the image/binary/file | ```4668BB2223FFB983A5F1273B9E3D9FA2C5CE4A0F1FB18CA5C1B285762020073C``` |
 | dst_file_hash_sha512 | string | SHA512 hash of the image/binary/file | ```1AD1D79F85D8F6A50EA282F63898D652661DAA0C1FD361C22647CABC98A70E8CBCE83200D579D10DD0A3D46BE9496DCDFDDF28B0C5E9709343B032A8796FBECB``` |
 | dst_file_inode | integer | Filesystem inode number | `````` |
 | dst_file_link_name | string | path of the hard link | ```C:\Docs\My.exe``` |
 | dst_file_mime_type | string | MIME type name specified for the file | ```application/msword``` |
 | dst_file_modified_time | date | When the file was last modified. Also known as `mtime` | ```2016-11-25 18:21:47``` |
 | dst_file_name | string | name of the file without its full path. This could be a local file or one transmitted over the network. | ```a.exe``` |
 | dst_file_path | string | full path of a file including the name of the file. This could be a local file or one transmitted over the network. | ```C:\users\wardog\z.exe``` |
 | dst_file_previous_accessed_time | date | When the file was previously accessed | ```2016-11-25 18:21:47``` |
 | dst_file_previous_changed_time | date | When the file was previously changed | ```2016-11-25 18:21:47``` |
 | dst_file_previous_creation_time | date | When the file was previously created | ```2016-11-25 18:21:47``` |
 | dst_file_previous_modified_time | date | When the file was previously modified | ```2016-11-25 18:21:47``` |
 | dst_file_previous_name | string | The file's previous name | ```cmd.exe``` |
 | dst_file_previous_path | string | The file's previous path | ```C:\\Windows\system32\cmd.exe``` |
 | dst_file_product | string | The file's product name | ```Microsoft® Windows® Operating System``` |
 | dst_file_size | integer | Size of the file, in bytes. | ```45``` |
 | dst_file_symlink | integer | 1 if the path is a symlink, otherwise 0 | ```0``` |
 | dst_file_symlink_name | string | path of the symlink | ```C:\Docs\My.exe``` |
 | dst_file_system_block_size | integer | Block size of filesystem | `````` |
 | dst_file_system_type | string | The file system type, ex:  fat32, ntfs, vmfs, ext3, ext4, xfs | ```ntfs``` |
 | dst_file_version | string | file version. i.e. image loaded version | ```10.0.16299.15 (WinBuild.160101.0800)``` |
 | dst_geo_city | string | The city associated to the IP address in the network session. | ```San Miguel``` |
 | dst_geo_continent | string | The continent associated with the IP address in the network session. | ```South America``` |
 | dst_geo_country | string | The country associated with the IP address in the network session. | ```Peru``` |
 | dst_geo_country_capital | string | The capital of the country associated with the IP address in the network session. | ```Lima``` |
 | dst_geo_country_code | string | 51 | ```Country code``` |
 | dst_geo_latitude | string | The latitude of the geographical coordinate associated with the IP address in the network session. | ```38.8951``` |
 | dst_geo_longitude | string | The longitude of the geographical coordinate associated with the IP address in the network session. | ```-77.0364``` |
 | dst_geo_region | string | The region within a country associated with the IP address in the network session. | ```East US``` |
 | dst_interface_guid | string | GUID of the network interface which was used for authentication request (if applicable). Most of the time you would use the interface_name field for the uid. | ```7C202E90-2FBE-4275-AB0E-9BF67E04BEDF``` |
 | dst_interface_name | string | The network interface used for the connection or session by the destination device. | ```eth02``` |
 | dst_ip_addr | ip | IP address assigned to the device generating the event and/or the IP address in the network packet. This could be used in the context of source, destination, device and even NAT when it is provided by an intermediary NAT device such as a firewall. | ```192.168.1.2``` |
 | dst_ip_dhcp_assigned_ip_addr | ip | IP address assigned by the DHCP server. | ```192.168.1.2``` |
 | dst_ip_is_ipv6 | boolean | If IP address is IP version 6 | ```false``` |
 | dst_mac_addr | string | MAC address of the device where the event was generated or network interface where a connection starts or ends. | ```00:11:22:33:44:55``` |
 | dst_meta_dst_host_name_category | string | The defined grouping of a URL (or could be just based on the domain in the URL) related to what it is (ie adult, news, advertising, parked domains, etc) | ```Search Engines``` |
 | dst_mime_type | string | Destination MIME type as seen in (layer 7) application layer details or as defined by an application scanner such as an anti-virus/EDR. For HTTP this is usually from the server's "Content-Type" header. https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Complete_list_of_MIME_types | ```application/pdf``` |
 | dst_original_value | string | original value of a destination before any ETL modifications. For example, if wanting to cleanup a network share and keep the IP - this field would be used to keep the original value | ```8.8.8.8``` |
 | dst_packets | integer | The number of packets sent from the destination to the source for the connection or session (Reply). The meaning of a packet is defined by the reporting device. | ```5``` |
 | dst_port_name | string | Name of the port used in a network connection. This is usually determined by IANA common port assignment. Therefore, this means its a guess and NOT actually what the application/ is what the actually. | ```netbios-dgm``` |
 | dst_port_number | integer | Port number used in a network connection. This could be used in the context of source, destination and even NAT when it is provided by an intermediary NAT device such as a firewall. | ```138``` |
 | dst_resource_group | string | The ID of the group to which the destination device belongs in a network connection. This might be an AWS account, or an Azure subscription or Resource Group | ```DatabaseVMs``` |
 | dst_resource_id | string | The resource Id of the destination device in a network connection | ```/subscriptions/33333333-8888-4444-a115-aaaaaaaaaaaa/resourcegroups/shokobo/providers/microsoft.compute/virtualmachines/sysmachine2``` |
 | dst_user_aadid | string | The User Azure AD ID of the identity associated with a cloud network session. It applies to source and destination entities. | ```5e8b0f4d-2cd4-4e17-9467-b0f6a5c0c4d0``` |
 | dst_user_cred_type | string | types of credentials which were presented for delegation | ```%%8098``` |
 | dst_user_domain | string | The domain or computer name associated to the user in a session. In active directory, this would be the name of the domain the user belongs to. | ```CONTOSO``` |
 | dst_user_identity | string | User Principal Name (UPN) or another type of account identifier for which 802.1x authentication request was made. | ```host/XXXXXXXX.redmond.corp.microsoft.com``` |
 | dst_user_linked_logon_id | integer | A hexadecimal value of the paired logon session. | ```0x0``` |
 | dst_user_logon_authentication_lan_package_name | string | The name of the LAN Manager sub-package (NTLM-family protocol name) that was used during logon. Possible values are: NTLM V1, NTLM V2, LM. Only populated if Authentication Package = NTLM. | ```-``` |
 | dst_user_logon_authentication_package_name | string | The name of the authentication package which was used for the logon authentication process. Default packages loaded on LSA startup are located in "HKLM\SYSTEM\CurrentControlSet\Control\Lsa\OSConfig" registry key. Other packages can be loaded at runtime. When a new package is loaded a "4610: An authentication package has been loaded by the Local Security Authority" (typically for NTLM) or "4622: A security package has been loaded by the Local Security Authority" (typically for Kerberos) event is logged to indicate that a new package has been loaded along with the package name. | ```Negotiate``` |
 | dst_user_logon_device_claims | string | list of device claims for new logon session | ```-``` |
 | dst_user_logon_elevated_token | string | a "Yes" or "No" flag. If "Yes" then the session this event represents is elevated and has administrator privileges. | ```%%1842``` |
 | dst_user_logon_guid | string | a GUID that can help you correlate this event with another event that can contain the same Logon GUID, "4769(S, F): A Kerberos service ticket was requested event on a domain controller. It also can be used for correlation between a 4624 event and several other events (on the same computer) that can contain the same Logon GUID, "4648(S): A logon was attempted using explicit credentials" and "4964(S): Special groups have been assigned to a new logon." | ```{00000000-0000-0000-0000-000000000000}``` |
 | dst_user_logon_id | integer | hexadecimal value that can help you correlate this event with recent events that might contain the same Logon ID | ```0x8dcdc``` |
 | dst_user_logon_impersonation_level | string | Impersonation level | ```%%1833``` |
 | dst_user_logon_key_length | integer | the length of NTLM Session Security key. Typically it has 128 bit or 56 bit length. This parameter is always 0 if "Authentication Package" = "Kerberos", because it is not applicable for Kerberos protocol. This field will also have "0" value if Kerberos was negotiated using Negotiate authentication package. | ```0``` |
 | dst_user_logon_process_name | string | The name of the trusted logon process that was used for the logon. See event "4611: A trusted logon process has been registered with the Local Security Authority" description for more information. | ```User32``` |
 | dst_user_logon_restricted_admin_mode | string | Only populated for RemoteInteractive logon type sessions. This is a Yes/No flag indicating if the credentials provided were passed using Restricted Admin mode. Restricted Admin mode was added in Win8.1/2012R2 but this flag was added to the event in Win10. If not a RemoteInteractive logon, then this will be "-" string. | ```-``` |
 | dst_user_logon_transmitted_services | string | the list of transmitted services. Transmitted services are populated if the logon was a result of a S4U (Service For User) logon process. S4U is a Microsoft extension to the Kerberos Protocol to allow an application service to obtain a Kerberos service ticket on behalf of a user - most commonly done by a front-end website to access an internal resource on behalf of a user. | ```-``` |
 | dst_user_logon_type | integer | the type of logon which was performed | ```2``` |
 | dst_user_logon_user_claims | string | list of user claims for new logon session. This field contains user claims if user account was logged in and device claims if computer account was logged in | ```ad://ext/cn:88d2b96fdb2b4c49 <%%1818> : "dadmin" ad://ext/Department:88d16a8edaa8c66b <%%1818> : "IT"``` |
 | dst_user_logon_user_linked_id | integer | A hexadecimal value of the paired logon session. If there is no other logon session associated with this logon session, then the value is "0x0". | ```0x0``` |
 | dst_user_logon_virtual_account | string | a "Yes" or "No" flag, which indicates if the account is a virtual account (e.g., "Managed Service Account"), which was introduced in Windows 7 and Windows Server 2008 R2 to provide the ability to identify the account that a given Service uses, instead of just using "NetworkService". | ```%%1843``` |
 | dst_user_name | string | Name of the user associated with the main event (i.e. Network session). There could be a sense of direction depending how it is used together with other entities (i.e. src_user_name or dst_user_name) | ```wardog``` |
 | dst_user_network_account_domain | string | Domain for the user that will be used for outbound (network) connections. | ```-``` |
 | dst_user_network_account_name | string | User name used for outbound (network) connections | ```-``` |
 | dst_user_password | string | User password if seen in the request. Commonly seen in network logs and authentication proxy/logs. | ```bobspassword``` |
 | dst_user_reporter_domain | string | domain name of the user that reported the main event | ```WORKGROUP``` |
 | dst_user_reporter_id | integer | unique identifier of the user that reported the main event | ```0x3e7``` |
 | dst_user_reporter_name | string | the name of the account that reported information about the main event | ```WIN-GG82ULGC9GO$``` |
 | dst_user_reporter_sid | string | SID of account that reported information about the main event | ```S-1-5-18``` |
 | dst_user_security_package | string | the name of Security Package used during an authentication event. | ```CREDSSP``` |
 | dst_user_session_id | integer | ID of the session the user belongs to. | ```1``` |
 | dst_user_sid | string | Security identifier of the user. Typically, the identity used to authenticate a server. | ```S-1-5-21-1377283216-344919071-3415362939-500``` |
 | dst_user_sid_list | string | the list of special group SIDs, which New Logon\Security ID is a member of. | ```{S-1-5-21-3457937927-2839227994-823803824-512}``` |
 | dst_user_upn | string | In Active Directory, the User Principal Name (UPN) attribute is a user identifier for logging in, separate from a Windows domain login. | ```dadmin@contoso``` |
 | dst_vlan_id | integer | The destination VLAN ID if it can be determined. Most commonly if from a firewall/switch/router then it can be determined | ```1000``` |
 | dst_vlan_name | string | The destination VLAN Name. Most commonly if from a firewall/switch/router then it can be determined | ```untrust-dmz``` |
 | dst_zone | string | The network zone of the destination, as defined by the reporting device. | ```dmz``` |
