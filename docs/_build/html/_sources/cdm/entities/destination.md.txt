# destination

Event fields used to define the destination (server) in a network connection event.

## Attributes

| Name | Type | Description | Sample Value |
|:---|:---|:---|:---|
 | dst_bytes | integer | network bytes sent by the dst_ip_addr. Another field can also be provided after extending the IP entity. We can also define the dst_ip_bytes field. | ```100``` |
 | dst_certificate_hash_imphash | string | IMPHASH hash of the image/binary/file | ```2505BD03D7BD285E50CE89CEC02B333B``` |
 | dst_certificate_hash_imphash | string | IMPHASH hash of the image/binary/file | ```2505BD03D7BD285E50CE89CEC02B333B``` |
 | dst_certificate_hash_md5 | string | MD5 hash of the image/binary/file | ```6A255BEBF3DBCD13585538ED47DBAFD7``` |
 | dst_certificate_hash_md5 | string | MD5 hash of the image/binary/file | ```6A255BEBF3DBCD13585538ED47DBAFD7``` |
 | dst_certificate_hash_sha1 | string | SHA1 hash of the image/binary/file | ```B0BF5AC2E81BBF597FAD5F349FEEB32CAC449FA2``` |
 | dst_certificate_hash_sha1 | string | SHA1 hash of the image/binary/file | ```B0BF5AC2E81BBF597FAD5F349FEEB32CAC449FA2``` |
 | dst_certificate_hash_sha256 | string | SHA256 hash of the image/binary/file | ```4668BB2223FFB983A5F1273B9E3D9FA2C5CE4A0F1FB18CA5C1B285762020073C``` |
 | dst_certificate_hash_sha256 | string | SHA256 hash of the image/binary/file | ```4668BB2223FFB983A5F1273B9E3D9FA2C5CE4A0F1FB18CA5C1B285762020073C``` |
 | dst_certificate_hash_sha512 | string | SHA512 hash of the image/binary/file | ```1AD1D79F85D8F6A50EA282F63898D652661DAA0C1FD361C22647CABC98A70E8CBCE83200D579D10DD0A3D46BE9496DCDFDDF28B0C5E9709343B032A8796FBECB``` |
 | dst_certificate_hash_sha512 | string | SHA512 hash of the image/binary/file | ```1AD1D79F85D8F6A50EA282F63898D652661DAA0C1FD361C22647CABC98A70E8CBCE83200D579D10DD0A3D46BE9496DCDFDDF28B0C5E9709343B032A8796FBECB``` |
 | dst_certificate_issuer | string | Information about the CA that issued the certificate | ```CN=neu5ron.local,OU=Admin``` |
 | dst_certificate_serial_number | string | Serial number, this is chosen by the CA (certificate authority) which issued the certificate. Therefore this can relatively be arbritary if the CA does not follow a standard or is malicious. | ```5157550``` |
 | dst_certificate_subject | string | Information about the CA that issued the certificate | ```CN=natetoken,OU=Admin,DC=neu5ron,DC=local``` |
 | dst_city | string | The city associated with the destination IP address | ```Burlington``` |
 | dst_country | country | The country associated with the destination IP address | ```USA``` |
 | dst_domain | string | The (DNS) hierarchy that encompasses multiple hosts (i.e a Windows Active Directory environment). | ```bigwheel.corporation.local``` |
 | dst_file_accessed_time | date | When the file was last accessed . Also known as `atime` | ```2016-11-25 18:21:47``` |
 | dst_file_changed_time | date | When the file was last changed. Also known as `ctime` | ```2016-11-25 18:21:47``` |
 | dst_file_creation_time | date | When the file was created. Also known as `crtime` | ```2016-11-25 18:21:47``` |
 | dst_file_directory | string | Directory of file(s). It does not include the file name | ```C:\users\wardog\``` |
 | dst_file_extension | string | The file extension of a file (.txt, .exe, etc) | ```exe``` |
 | dst_file_hard_links | integer | Number of hard links | ```3``` |
 | dst_file_hash_imphash | string | IMPHASH hash of the image/binary/file | ```2505BD03D7BD285E50CE89CEC02B333B``` |
 | dst_file_hash_md5 | string | MD5 hash of the image/binary/file | ```6A255BEBF3DBCD13585538ED47DBAFD7``` |
 | dst_file_hash_sha1 | string | SHA1 hash of the image/binary/file | ```B0BF5AC2E81BBF597FAD5F349FEEB32CAC449FA2``` |
 | dst_file_hash_sha256 | string | SHA256 hash of the image/binary/file | ```4668BB2223FFB983A5F1273B9E3D9FA2C5CE4A0F1FB18CA5C1B285762020073C``` |
 | dst_file_hash_sha512 | string | SHA512 hash of the image/binary/file | ```1AD1D79F85D8F6A50EA282F63898D652661DAA0C1FD361C22647CABC98A70E8CBCE83200D579D10DD0A3D46BE9496DCDFDDF28B0C5E9709343B032A8796FBECB``` |
 | dst_file_inode | integer | Filesystem inode number | `````` |
 | dst_file_link_name | string | path of the hard link | ```C:\Docs\My.exe``` |
 | dst_file_mime_type | string | Specifies the MIME type name specified for a file | ```application/msword``` |
 | dst_file_modified_time | date | When the file was last modified. Also known as `mtime` | ```2016-11-25 18:21:47``` |
 | dst_file_name | string | name of a file without its full path. This could be a local file or transmitted over the network. | ```a.exe``` |
 | dst_file_path | string | full path of a file including the name of the file. | ```C:\users\wardog\z.exe``` |
 | dst_file_previous_name | string | The file's previous name | ```C:\\Windows\system32\cmd.exe``` |
 | dst_file_size | string | Specifies the size of a file, in bytes | ```45``` |
 | dst_file_symlink | integer | 1 if the path is a symlink, otherwise 0 | ```0``` |
 | dst_file_symlink_name | string | path of the symlink | ```C:\Docs\My.exe``` |
 | dst_file_system_block_size | integer | Block size of filesystem | `````` |
 | dst_file_system_type | string | The file system type, ex:  fat32, ntfs, vmfs, ext3, ext4, xfs | ```ntfs``` |
 | dst_fqdn | string | The absolute (entire) value of the DNS hierarchy from the lowest level to the top level domain (TLD). Consists of the Hostname and Domain. This is best defined in [this Wikipedia](https://en.wikipedia.org/w/index.php?title=Fully_qualified_domain_name&oldid=911195384#Syntax) article on FQDN. | ```bob-berto-pc.bigwheel.corporation.local``` |
 | dst_host_domain | string | Name of the domain the host is part of or joined. | ```hunt.wardog.com``` |
 | dst_host_fqdn | string | The fully qualified domain name of the host | ```WKHR001.hunt.wardog.com``` |
 | dst_host_interface_guid | string | GUID of the network interface which was used for authentication request | ```{2BB33827-6BB6-48DB-8DE6-DB9E0B9F9C9B}``` |
 | dst_host_interface_name | string | the name (description) of the network interface that was used for authentication request. You can get the list of all available network adapters using "ipconfig /all" command | ```Microsoft Hyper-V Network Adapter``` |
 | dst_host_local_mac | string | local interface's MAC-address | ```18:64:72:F3:33:91``` |
 | dst_host_model | string | The model of the source device | ```Samsung Galaxy Note 10``` |
 | dst_host_name | string | The name of a host, device, node, or entity that is separate from the FQDN and Domain. | ```WKHR001``` |
 | dst_host_os | string | The OS of the source device | ```iOS``` |
 | dst_host_peer_mac | string | peer's (typically - access point) MAC-address | ```02:1A:C5:14:59:C9``` |
 | dst_host_type | string | The type of the source device | ```mobile``` |
 | dst_interface_guid | string | GUID of the network interface which was used for authentication request. | ```7C202E90-2FBE-4275-AB0E-9BF67E04BEDF``` |
 | dst_interface_name | string | The network interface used for the connection or session by the destination device. | ```eth02``` |
 | dst_ip_addr | ip | IP address captured in a network connection. This could be used in the context of source, destination and even NAT when it is provided by an intermediary NAT device such as a firewall. | ```192.168.1.2``` |
 | dst_ip_bytes | integer | network IP (header) bytes sent by the either the source or destination ip address | ```100``` |
 | dst_ip_dhcp_assigned_ip_addr | ip | IP address assigned by the DHCP server. | ```192.168.1.2``` |
 | dst_ip_is_ipv6 | boolean | If source or destination IP address is IP version 6 | ```false``` |
 | dst_latitude | real | The latitude of the geographical coordinate associated with the destination IP address | ```44.475833``` |
 | dst_longitude | real | The longitude of the geographical coordinate associated with the destination IP address | ```-73.211944``` |
 | dst_mac_address | mac | MAC address of an endpoint or network interface where a connection starts or ends. | ```00:11:22:33:44:55``` |
 | dst_mime_type | string | Destination MIME type as seen in (layer 7) application layer details or as defined by an application scanner such as an anti-virus/EDR. For HTTP this is usually from the server's "Content-Type" header. https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Complete_list_of_MIME_types | ```application/pdf``` |
 | dst_packets | integer | Network packets sent by the destination (Reply) | ```5``` |
 | dst_port_name | string | Name of the port used in a network connection. This is usually determined by IANA common port assignment. Therefore, this means its a guess and NOT actually what the application/ is what the actually. | ```netbios-dgm``` |
 | dst_port_number | integer | Port number used in a network connection. This could be used in the context of source, destination and even NAT when it is provided by an intermediary NAT device such as a firewall. | ```138``` |
 | dst_region | string | The region within a country associated with the destination IP address | ```Vermont``` |
 | dst_resource_group | string | The ID of the group to which the destination device belongs in a network connection. This might be an AWS account, or an Azure subscription or Resource Group | ```DatabaseVMs``` |
 | dst_resource_id | string | The resource Id of the destination device in a network connection | ```/subscriptions/33333333-8888-4444-a115-aaaaaaaaaaaa/resourcegroups/shokobo/providers/microsoft.compute/virtualmachines/sysmachine2``` |
 | dst_vlan_id | integer | The destination VLAN ID if it can be determined. Most commonly if from a firewall/switch/router then it can be determined | ```1000``` |
 | dst_vlan_name | string | The destination VLAN Name. Most commonly if from a firewall/switch/router then it can be determined | ```untrust-dmz``` |
 | dst_zone | string | The network zone of the destination, as defined by the reporting device. | ```dmz``` |
