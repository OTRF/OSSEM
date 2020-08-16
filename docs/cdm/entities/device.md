# device

Events used to provide information about a network device.

## Attributes

| Name | Type | Description | Sample Value |
|:---|:---|:---|:---|
 | dvc_action | string | If reported by an intermediary device such as a firewall, the action taken by device. | ```allow``` |
 | dvc_inbound_interface | string | If reported by an intermediary device such as a firewall, the network interface used by it for the connection to the source device | ```eth0``` |
 | dvc_outbound_interface | string | If reported by an intermediary device such as a firewall, the network interface used by it for the connection to the destination device. | ```Ethernet 4``` |
