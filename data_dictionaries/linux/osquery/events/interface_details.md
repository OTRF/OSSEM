# Interface_details Table

## Description
Detailed information and stats of network interfaces.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|interface|TEXT|Interface name|`TBD`|
|TBD|mac|TEXT|MAC of interface (optional)|`TBD`|
|TBD|type|INTEGER|Interface type (includes virtual)|`TBD`|
|TBD|mtu|INTEGER|Network MTU|`TBD`|
|TBD|metric|INTEGER|Metric based on the speed of the interface|`TBD`|
|TBD|flags|INTEGER|Flags (netdevice) for the device|`TBD`|
|TBD|ipackets|BIGINT|Input packets|`TBD`|
|TBD|opackets|BIGINT|Output packets|`TBD`|
|TBD|ibytes|BIGINT|Input bytes|`TBD`|
|TBD|obytes|BIGINT|Output bytes|`TBD`|
|TBD|ierrors|BIGINT|Input errors|`TBD`|
|TBD|oerrors|BIGINT|Output errors|`TBD`|
|TBD|idrops|BIGINT|Input drops|`TBD`|
|TBD|odrops|BIGINT|Output drops|`TBD`|
|TBD|collisions|BIGINT|Packet Collisions detected|`TBD`|
|TBD|last_change|BIGINT|Time of last device modification (optional)|`TBD`|
|TBD|link_speed|BIGINT|Interface speed in Mb/s [POSIX]|`TBD`|
|TBD|pci_slot|TEXT|PCI slot number [LINUX]|`TBD`|
|TBD|friendly_name|TEXT|The friendly display name of the interface. [WINDOWS]|`TBD`|
|TBD|description|TEXT|Short description of the object a one-line string. [WINDOWS]|`TBD`|
|TBD|manufacturer|TEXT|Name of the network adapter's manufacturer. [WINDOWS]|`TBD`|
|TBD|connection_id|TEXT|Name of the network connection as it appears in the Network Connections Control Panel program. [WINDOWS]|`TBD`|
|TBD|connection_status|TEXT|State of the network adapter connection to the network. [WINDOWS]|`TBD`|
|TBD|enabled|INTEGER|Indicates whether the adapter is enabled or not. [WINDOWS]|`TBD`|
|TBD|physical_adapter|INTEGER|Indicates whether the adapter is a physical or a logical adapter. [WINDOWS]|`TBD`|
|TBD|speed|INTEGER|Estimate of the current bandwidth in bits per second. [WINDOWS]|`TBD`|
|TBD|service|TEXT|The name of the service the network adapter uses. [WINDOWS]|`TBD`|
|TBD|dhcp_enabled|INTEGER|If TRUE, the dynamic host configuration protocol (DHCP) server automatically assigns an IP address to the computer system when establishing a network connection. [WINDOWS]|`TBD`|
|TBD|dhcp_lease_expires|TEXT|Expiration date and time for a leased IP address that was assigned to the computer by the dynamic host configuration protocol (DHCP) server. [WINDOWS]|`TBD`|
|TBD|dhcp_lease_obtained|TEXT|Date and time the lease was obtained for the IP address assigned to the computer by the dynamic host configuration protocol (DHCP) server. [WINDOWS]|`TBD`|
|TBD|dhcp_server|TEXT|IP address of the dynamic host configuration protocol (DHCP) server. [WINDOWS]|`TBD`|
|TBD|dns_domain|TEXT|Organization name followed by a period and an extension that indicates the type of organization, such as 'microsoft.com'. [WINDOWS]|`TBD`|
|TBD|dns_domain_suffix_search_order|TEXT|Array of DNS domain suffixes to be appended to the end of host names during name resolution. [WINDOWS]|`TBD`|
|TBD|dns_host_name|TEXT|Host name used to identify the local computer for authentication by some utilities. [WINDOWS]|`TBD`|
|TBD|dns_server_search_order|TEXT|Array of server IP addresses to be used in querying for DNS servers. [WINDOWS]|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#interface_details)

## Tags
* version_4.4.2