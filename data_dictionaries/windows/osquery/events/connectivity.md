# Connectivity Table

## Description
Provides the overall system's network state.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|disconnected|INTEGER|True if the all interfaces are not connected to any network|`TBD`|
|TBD|ipv4_no_traffic|INTEGER|True if any interface is connected via IPv4, but has seen no traffic|`TBD`|
|TBD|ipv6_no_traffic|INTEGER|True if any interface is connected via IPv6, but has seen no traffic|`TBD`|
|TBD|ipv4_subnet|INTEGER|True if any interface is connected to the local subnet via IPv4|`TBD`|
|TBD|ipv4_local_network|INTEGER|True if any interface is connected to a routed network via IPv4|`TBD`|
|TBD|ipv4_internet|INTEGER|True if any interface is connected to the Internet via IPv4|`TBD`|
|TBD|ipv6_subnet|INTEGER|True if any interface is connected to the local subnet via IPv6|`TBD`|
|TBD|ipv6_local_network|INTEGER|True if any interface is connected to a routed network via IPv6|`TBD`|
|TBD|ipv6_internet|INTEGER|True if any interface is connected to the Internet via IPv6|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#connectivity)

## Tags
* version_4.4.2