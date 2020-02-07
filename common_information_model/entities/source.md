# Source Schema
Event fields used to define the source (client) in a network connection event.

## Data Fields
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|src_bytes||integer|network bytes sent by the src_ip_addr|100|
|src_domain||string|If there is a clear distinction of the domain VS hostname VS FQDN this is the domain field. More often than not this should NOT be used and should be defined in the ./target.md, ./host.md, or ./user.md. However, you may follow the recommendations additional-guidelines/domain_or_hostname_or_fqdn.md if there is a clear example for this|bigwheel.corporation.local|
|src_file_extension||string|The file extension of a file (.txt, .exe, etc)|exe|
|src_file_name||string|name of a file without its full path|a.exe|
|src_file_path||string|full path of a file including the name of the file|C:\users\wardog\z.exe|
|src_fqdn||string|If there is a clear distinction of the domain VS hostname VS FQDN this is the FQDN field. More often than not this should NOT be used and should be defined in the ./target.md, ./host.md, or ./user.md. However, you may follow the recommendations additional-guidelines/domain_or_hostname_or_fqdn.md if there is a clear example for this|bob-berto-pc.bigwheel.corporation.local|
|src_host_name||string|The Source server, host, hostname, domain, or domain name. Some examples, would include the TLS server name, HTTP Host, DNS Query Name, etc. For information on how to define and use this field refer to the documentation additional-guidelines/domain_or_hostname_or_fqdn.md|www.google.com|
|src_ip_addr||ip|Source IP address|10.10.10.10|
|src_ip_bytes||integer|network IP (header) bytes sent by the src_ip_addr|100|
|src_is_ipv6||boolean|If src_ip_addr is IP version 6|false|
|src_mac||string|Source MAC address|a9:68:82:28:c4:6d|
|src_mime_type||string|Source MIME type as seen in (layer 7) application layer details or as defined by an application scanner such as an anti-virus/EDR. For HTTP this is usually from the server's "Content-Type" header. https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Complete_list_of_MIME_types|application/pdf|
|src_packets||integer|Network packets sent|5|
|src_port||integer|Source port number|138|
|src_port_name||string|Source port name. This is usually determined by IANA common port assignment. Therefore, this means its a guess and NOT the actual the application used|netbios-dgm|
|src_vlan_id||integer|The Source VLAN ID if it can be determined. Most commonly if from a firewall/switch/router then it can be determined|100|
|src_vlan_name||string|The Source VLAN Name. Most commonly if from a firewall/switch/router then it can be determined|management|

## Resources
* [Examples of MIME types](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Complete_list_of_MIME_types)
