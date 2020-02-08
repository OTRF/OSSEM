# Destination Schema
Event fields used to define the destination (server) in a network connection event.

## Data Fields
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|dst_bytes||integer|network bytes sent by the dst_ip_addr|100|
|dst_domain||string|If there is a clear distinction of the domain VS hostname VS FQDN this is the domain field. More often than not this should NOT be used and should be defined in the ./target.md, ./host.md, or ./user.md. However, you may follow the recommendations additional-guidelines/domain_or_hostname_or_fqdn.md if there is a clear example for this|bigwheel.corporation.local|
|dst_file_extension||string|The file extension of a file (.txt, .exe, etc)|exe|
|dst_file_name||string|name of a file without its full path|a.exe|
|dst_file_path||string|full path of a file including the name of the file|C:\users\wardog\z.exe|
|dst_fqdn||string|If there is a clear distinction of the domain VS hostname VS FQDN this is the FQDN field. More often than not this should NOT be used and should be defined in the ./target.md, ./host.md, or ./user.md. However, you may follow the recommendations additional-guidelines/domain_or_hostname_or_fqdn.md if there is a clear example for this|bob-berto-pc.bigwheel.corporation.local|
|dst_host_name||string|The destination server, host, hostname, domain, or domain name. Some examples, would include the TLS server name, HTTP Host, DNS Query Name, etc. For information on how to define and use this field refer to the documentation additional-guidelines/domain_or_hostname_or_fqdn.md|www.google.com|
|dst_ip_addr||ip|Destination IP address|8.8.8.8|
|dst_ip_bytes||integer|network IP (header) bytes sent by the dst_ip_addr|104|
|dst_is_ipv6||boolean|If dst_ip_addr is IP version 6|false|
|dst_mac||string|Destination MAC address|a9:68:82:28:c4:6d|
|dst_mime_type||string|Destination MIME type as seen in (layer 7) application layer details or as defined by an application scanner such as an anti-virus/EDR. For HTTP this is usually from the server's "Content-Type" header. https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Complete_list_of_MIME_types|application/pdf|
|dst_packets||integer|Network packets sent|5|
|dst_port||integer|Destination port number|138|
|dst_port_name||string|Destination port name. This is usually determined by IANA common port assignment. Therefore, this means its a guess and NOT the actual the application used|netbios-dgm|
|dst_vlan_id||integer|The destination VLAN ID if it can be determined. Most commonly if from a firewall/switch/router then it can be determined|1000|
|dst_vlan_name||string|The destination VLAN Name. Most commonly if from a firewall/switch/router then it can be determined|untrust-dmz|

## References
* [Examples of MIME types](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Complete_list_of_MIME_types)
