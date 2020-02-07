# RDP Log

## Description
None

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|@timestamp|ts|TBD|date_time|Timestamp of the beginning of the event in epoch format|1300475167.096535|
|src_ip_addr|id.orig_h|TBD|ip|The originating/source IP address|10.1.1.1|
|src_port|id.orig_p|TBD|integer|The originating/source port|37682|
|dst_ip_addr|id.resp_h|TBD|ip|The responding/destination IP address|10.2.2.2|
|dst_port|id.resp_p|TBD|integer|The responding/destination port|3389|
|event_uid|uid|TBD|string|Unique ID for the connection.|CHhAvVGS1DHFjwGM9|
|TBD|cert_count|TBD|integer|The number of certs seen. X.509 can transfer an entire certificate chain.|4|
|TBD|cert_permanent|TBD|boolean|Indicates if the provided certificate or certificate chain is permanent or temporary.|true|
|TBD|cert_type|TBD|string|If the connection is being encrypted with native RDP encryption, this is the type of cert being used.|RSA|
|TBD|client_build|TBD|string|RDP client version used by the client machine.|client_build-14393|
|TBD|client_dig_product_id|TBD|string|Product ID of the client machine.|bdedcf4e-aa02-4441-5013-f32139f|
|TBD|client_name|TBD|string|Name of the client machine.|SOMECOMPUTERNAME|
|TBD|cookie|TBD|string|Cookie value used by the client machine. This is typically a username. Even during encrypted sessions, this will contain the first few characters.|Administr|
|TBD|desktop_height|TBD|integer|Desktop height of the client machine.|1080|
|TBD|desktop_width|TBD|integer|Desktop width of the client machine.|1920|
|TBD|encryption_level|TBD|string|Encryption level of the connection.|High|
|TBD|encryption_method|TBD|string|Encryption method of the connection.|encryption_method-16|
|TBD|keyboard_layout|TBD|string|Keyboard layout (language) of the client machine.|English - United States|
|TBD|requested_color_depth|TBD|string|The color depth requested by the client in the high_color_depth field.|32bit|
|TBD|result|TBD|string|Status result for the connection. It's a mix between RDP negotation failure messages and GCC server create response messages.|HYBRID_REQUIRED_BY_SERVER|
|TBD|security_protocol|TBD|string|Security protocol chosen by the server.|HYBRID_EX|
|TBD|ssl|TBD|boolean|present if policy/protocols/rdp/indicate_ssl.bro is loaded Flag the connection if it was seen over SSL.|true|
