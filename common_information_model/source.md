# Source Schema

Event fields used to define the source (client) in a network connection event.

## Data Fields

| Standard Name | Type | Description | Sample Value |
|--------|---------|-------|-------|
| src_bytes | integer | network bytes sent by the src_ip_addr | 100 |
| src_host_name | string | Source/Subject host name | WKHR001 |
| src_ip_addr | ip | Source IP address | 8.8.8.8 |
| src_ip_bytes | integer | network IP (header) bytes sent by the src_ip_addr | 100 |
| src_mac | mac | Source MAC address | a9:68:82:28:c4:6d |
| src_mime_type | string | Source MIME type as seen in (layer 7) application layer details or as defined by a application scanner such as an anti-virus/EDR. For HTTP this is usually from the client's "Content-Type" header. For some examples of MIME types, check out: https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Complete_list_of_MIME_types | application/pdf |
| src_packets | integer | network packets sent by the src_ip_addr | 5 |
| src_port | integer | Source port number | 41572 |
| src_port_name | string | Source port name. This is usually determined by IANA common port assignment. Therefore, this means its a guess and NOT the actual the application used | netbios-dgm |