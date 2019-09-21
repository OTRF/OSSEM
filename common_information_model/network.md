# Network Schema

Event fields used to define metadata about network information seen in a typical OSI layer. This includes data both from an endpoint as well as a network monitoring device/application (NSM, Firewall, IPS, IDS, etc...). This differentiates from data that is specific to Source and Destination specific information such as Source or Destination bytes, packets, IP address, mac address, TCP flags.

## Data Fields

| Standard Name | Type | Description | Sample Value |
|--------|---------|-------|-------|
| network_bytes | long | Total bytes for the session. If this field does not exist in the log source, then its possible in your ETL pipeline to combine the source and destination bytes | 102034 |
| fingerprint_network_community_id | string | Network community ID as outlined by the standard from https://github.com/corelight/community-id-spec. Standardized hashing of network tuple. The combination, most commonly, of Source IP, Source Port, Destination IP, Destination Port, and IP Protocol allows pivoting between multiple log types | 1:EeVyZ07VGj1n0rld+xCLFdM+u8M= |
| network_initiated | boolean | Whether the session was initiated or received. Most commonly used in relation to an endpoint/device. False = the endpoint did not initiate the session (ie: was scanned or RDP connection made to it) | True |
| network_ip_bytes | long | Total IP bytes, according to ip headers, for the session. If this field does not exist in the log source, then its possible in your ETL pipeline to combine the source and destination IP bytes | 14564 |
| network_missed_bytes | long | bytes that a network sensor or other system/application may have missed | 5 |
| network_packets | long | Total packets for the session. If this field does not exist in the log source, then its possible in your ETL pipeline to combine the source and destination packets | 143 |
| network_application | string | Layer 7 (application) in the OSI model. Ex: HTTP,SMB,FTP,SSH, etc | HTTP |
| network_protocol | string | Transport layer in the OSI model. Also known as, IP Protocol. Ex: TCP,UDP,ICMP,ICMP-v6, etc. Convert to lowercase | tcp |
