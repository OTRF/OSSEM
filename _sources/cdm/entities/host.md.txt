# host

Event fields used to define metadata about a host or device.

## Attributes

| Name | Type | Description | Sample Value |
|:---|:---|:---|:---|
 | host_domain | string | Name of the domain the host is part of or joined. | ```hunt.wardog.com``` |
 | host_fqdn | string | The fully qualified domain name of the host | ```WKHR001.hunt.wardog.com``` |
 | host_interface_guid | string | GUID of the network interface which was used for authentication request | ```{2BB33827-6BB6-48DB-8DE6-DB9E0B9F9C9B}``` |
 | host_interface_name | string | the name (description) of the network interface that was used for authentication request. You can get the list of all available network adapters using "ipconfig /all" command | ```Microsoft Hyper-V Network Adapter``` |
 | host_local_mac | string | local interface's MAC-address | ```18:64:72:F3:33:91``` |
 | host_model | string | The model of the source device | ```Samsung Galaxy Note 10``` |
 | host_name | string | The name of a host, device, node, or entity that is separate from the FQDN and Domain. | ```WKHR001``` |
 | host_os | string | The OS of the source device | ```iOS``` |
 | host_peer_mac | string | peer's (typically - access point) MAC-address | ```02:1A:C5:14:59:C9``` |
 | host_type | string | The type of the source device | ```mobile``` |
