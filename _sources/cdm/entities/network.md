# network

Event fields used to define metadata about network information seen in a typical OSI layer. This includes data both from an endpoint as well as a network monitoring device/application (NSM, Firewall, IPS, IDS, etc...). This differentiates from data that is specific to Source and Destination specific information such as Source or Destination bytes, packets, IP address, mac address, TCP flags.

## Attributes

| Name | Type | Description | Sample Value |
|:---|:---|:---|:---|
 | network_application_name | string | Layer 7 (application) name specific to service/name/software as provided by a device or user | ```google-drive``` |
 | network_application_protocol | string | Layer 7 (application) in the OSI model. Ex: HTTP,SMB,FTP,SSH, etc. | ```HTTP``` |
 | network_bytes | long | Total bytes for the session. If this field does not exist in the log source, then its possible in your ETL pipeline to combine the source and destination bytes | ```102034``` |
 | network_code | integer | For an ICMP message, ICMP message type numeric value (RFC 2780 or RFC 4443). | ```34``` |
 | network_connection_history | string | TCP Flags and other potential IP header info | `````` |
 | network_connection_history_detailed | string | Detailed description of the information in connection_history | `````` |
 | network_connection_state | string | The end state of the session/connection as defined in short abbreviation | `````` |
 | network_connection_state_detailed | string | Detailed description of the information in network_connection_state | `````` |
 | network_direction | string | User/Device defined name of the direction of the connection | ```outbound``` |
 | network_duration | integer | The amount of time, in millisecond, for the completion of the network session or connection. | ```1500``` |
 | network_fingerprint_network_community_id | string | Network community ID as outlined by the standard from https://github.com/corelight/community-id-spec. Standardized hashing of network tuple. The combination, most commonly, of Source IP, Source Port, Destination IP, Destination Port, and IP Protocol allows pivoting between multiple log types | ```1:EeVyZ07VGj1n0rld+xCLFdM+u8M=``` |
 | network_initiated | boolean | Whether the session was initiated or received. Most commonly used in relation to an endpoint/device. False = the endpoint did not initiate the session (ie: was scanned or RDP connection made to it) | ```TRUE``` |
 | network_inner_vlan_id | integer | Normally the VLAN can not be determined as source/destination and VLANs are stacked/wrapped. This is the VLAN "inside" | ```150``` |
 | network_ip_bytes | long | Total IP bytes, according to ip headers, for the session. If this field does not exist in the log source, then its possible in your ETL pipeline to combine the source and destination bytes | ```14564``` |
 | network_missed_bytes | long | bytes that a network sensor or other system/application may have missed | ```5``` |
 | network_outer_vlan_id | integer | Normally the VLAN can not be determined as source/destination and VLANs are stacked/wrapped. This is the VLAN on the "outside" | ```160``` |
 | network_packets | long | Total packets for the session. If this field does not exist in the log source, then its possible in your ETL pipeline to combine the source and destination packets | ```143``` |
 | network_protocol | string | Transport layer in the OSI model. Also known as, IP Protocol. Ex: TCP,UDP,ICMP,ICMP-v6, etc. Convert to lowercase | ```tcp``` |
 | network_session_id | string | The session identifier as reported by the network sensor device. Typically, not available for connections. | ```S198_13_1_27_12321_D205_13_1_27_443_0012``` |
 | network_type | string | For an ICMP message, ICMP message type text representation (RFC 2780 or RFC 4443) | ```Destination Unreachable``` |
