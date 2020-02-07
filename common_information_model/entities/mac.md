# MAC Schema
Event fields used to define metadata about MAC addresses in a network. It follows the standard from the Destination and Source categories.

## Data Fields
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|mac_address||mac|MAC address of the endpoint where the log was created|00:11:22:33:44:55|
|dst_mac||ip|destination MAC in a network connection|00:11:22:33:44:55|
|dst_nat_mac||ip|destination NAT MAC in a network connection|00:11:22:33:44:55|
|src_mac||ip|source MAC in a network connection|00:11:22:33:44:55|
|src_nat_mac||ip|source NAT MAC in a network connection|00:11:22:33:44:55|