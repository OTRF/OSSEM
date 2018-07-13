# Firewall Schema

Low Level Event fields used to define metadata about firewall connections in a network. 

## Data Fields

| Standard Name | Type | Description | Sample Value |
|--------|---------|-------|-------|
| fwl_conn_id | integer | Connection ID used to track individual network sessions through a firewall | 1124863 |
| fwl_interface | string | Firewall Interface a network session is seen on | outside |
| fwl_policy_name | string | Firewall Access-List or Policy name a network session applies to | inside-all |
| fwl_conn_flags | string | Flags for the network session | PSH ACK |
| fwl_conn_count | integer | Session Connection counts for various status messages (created sessions, dropped sessions, etc) | 6527 |
| fwl_action | string | Action taken on a session (Accept, Deny, etc) | Denied |
| fwl_direction | string | Direction for a network session (inbound/outbound) | Inbound |
| fwl_conn_duration | string | Duration of a network session | 0:02:48 |
| fwl_conn_bytes | integer | Number of bytes transferred in a network session | 52 |
| src_interface | string | Source Interface for a network session | inside |
| dst_interface | string | Destination Interface for a network session | outside |
| dst_nat_ip | ip | NAT IP address for a network session | 8.8.8.8 |
| dst_nat_port | integer | NAT Network port used for a network session | 32123 |
