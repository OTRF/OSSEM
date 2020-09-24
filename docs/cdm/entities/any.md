# any

Fields used to define metadata for a single field to include data from multiple fields with similar/same values/data.  This data is most commonly created from an ETL pipeline. Any fields below that contain a '*' indicates those are searches and not actual fields (key/values). This is because certain values are not desirable to copy/duplicate. However, because of a common schema we can still find are values for a specific common type, without duplicating or copying everything to one field!

## Attributes

| Name | Type | Description | Sample Value |
|:---|:---|:---|:---|
 | any_event_id | string | Allows searching a single field for all log IDs. All log ID fields copied/duplicated to a single field as an array. | ```````` |
 | any_hash | string | Allows searching a single field for all hashes. All hash fields copied/duplicated to a single field as an array. | ```````` |
 | any_ip_addr | ip | Allows searching a single field for all IPs. All IP fields copied/duplicated to a single field as an array. | ```````` |
 | any_ip_addr | ip | IP address assigned to the device generating the event and/or the IP address in the network packet. This could be used in the context of source, destination, device and even NAT when it is provided by an intermediary NAT device such as a firewall. | ```192.168.1.2``` |
 | any_ip_dhcp_assigned_ip_addr | ip | IP address assigned by the DHCP server. | ```192.168.1.2``` |
 | any_ip_geo.as_org | string | Allows searching a single field for all BGP AS Organization Names. All AS name fields copied/duplicated to a single field as an array. | ```````` |
 | any_ip_geo.asn | integer | Allows searching a single field for all BGP AS Numbers. All AS number fields copied/duplicated to a single field as an array. | ```````` |
 | any_ip_is_ipv6 | boolean | If IP address is IP version 6 | ```false``` |
 | any_mac_addr | string | Allows searching a single field for all MAC addresses. All MAC address fields copied/duplicated to a single field as an array. | ```````` |
 | any_user | string | Allows searching a single field for all users. All user fields copied/duplicated to a single field as an array. | ```````` |
 | any_vlan_id | integer | Allows searching a single field for all VLAN IDs. All VLAN ID fields copied/duplicated to a single field as an array. | `````` |
