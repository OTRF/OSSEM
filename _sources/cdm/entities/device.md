# device

Events used to provide information about a network device.

## Attributes

| Name | Type | Description | Sample Value |
|:---|:---|:---|:---|
 | dvc_action | string | If reported by an intermediary device such as a firewall, the action taken by device. | ```allow``` |
 | dvc_domain | string | Name of the domain the host is part of or joined. | ```hunt.wardog.com``` |
 | dvc_fqdn | string | The fully qualified domain name of the host | ```WKHR001.hunt.wardog.com``` |
 | dvc_host_name | string | The host name from which the event/log came from. There may be multiple host names in an event (i.e. syslog could have forwarder host name), this field is to be the most true log host name (i.e. NOT the forwarders name). | ```bobs.uncle-pc``` |
 | dvc_inbound_interface | string | If reported by an intermediary device such as a firewall, the network interface used by it for the connection to the source device | ```eth0``` |
 | dvc_interface_guid | string | GUID of the network interface which was used for authentication request | ```{2BB33827-6BB6-48DB-8DE6-DB9E0B9F9C9B}``` |
 | dvc_interface_name | string | the name (description) of the network interface that was used for authentication request. You can get the list of all available network adapters using "ipconfig /all" command | ```Microsoft Hyper-V Network Adapter``` |
 | dvc_ip_addr | ip | IP address captured in a network connection. This could be used in the context of source, destination and even NAT when it is provided by an intermediary NAT device such as a firewall. | ```192.168.1.2``` |
 | dvc_ip_dhcp_assigned_ip_addr | ip | IP address assigned by the DHCP server. | ```192.168.1.2``` |
 | dvc_ip_is_ipv6 | boolean | If source or destination IP address is IP version 6 | ```false``` |
 | dvc_mac_addr | string | MAC address of an endpoint or network interface where a connection starts or ends. | ```00:11:22:33:44:55``` |
 | dvc_model_name | string | The model name of the device | ```Samsung Galaxy Note``` |
 | dvc_model_number | string | The model number of the device | ```10``` |
 | dvc_os | string | The OS of the source device | ```iOS``` |
 | dvc_outbound_interface | string | If reported by an intermediary device such as a firewall, the network interface used by it for the connection to the destination device. | ```Ethernet 4``` |
 | dvc_type | string | The type of the source device | ```mobile``` |
