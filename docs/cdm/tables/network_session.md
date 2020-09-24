# network_session

Event fields used to normalize data related to network sessions.

## Attributes

| Entity | Name | Type | Description | Sample Value |
|:---|:---|:---|:---|:---|
 | cloud | cloud_app_id | string | The ID of the application for an HTTP application as identified by a proxy. This value is usually specific to the proxy used. | 124 |
 | cloud | cloud_app_name | string | The name of an application provided by a cloud service. | AppOne |
 | cloud | cloud_app_operation | string | The operation the user performed in the context of the application for an HTTP application as identified by a proxy. This value is usually specific to the proxy used. | DELETE |
 | cloud | cloud_app_risk_level | string | The risk level associated with an HTTP application as identified by a proxy. This value is usually specific to the proxy used. | 3 |
 | destination | dst_bytes | integer | The number of bytes sent from the destination to the source for the connection or session. | 100 |
 | destination | dst_domain_hostname | string | The destination server, host, hostname, domain, domain name or what people commonly might refer to as a domain or website when someone is browsing the Internet. Some examples, would include the TLS server name, HTTP Host, DNS Query Name, etc. For information on how to define and use this field refer to the documentation [here](https://ossemproject.com/cdm/guidelines/domain_or_hostname_or_fqdn.html) | www.google.com |
 | destination | dst_dvc_domain | string | Name of the domain the device is part of. | hunt.wardog.com |
 | destination | dst_dvc_fqdn | string | The fully qualified domain name of the host | WKHR001.hunt.wardog.com |
 | destination | dst_dvc_hostname | string | The host name from which the event/log came from. There may be multiple host names in an event (i.e. syslog could have forwarder host name), this field is to be the most true log host name (i.e. NOT the forwarders name). | bobs.uncle-pc |
 | destination | dst_dvc_ip_addr | ip | IP address assigned to the device generating the event and/or the IP address in the network packet. This could be used in the context of source, destination, device and even NAT when it is provided by an intermediary NAT device such as a firewall. | 192.168.1.2 |
 | destination | dst_dvc_mac_addr | string | MAC address of the device where the event was generated or network interface where a connection starts or ends. | 00:11:22:33:44:55 |
 | destination | dst_geo_city | string | The city associated to the IP address in the network session. | San Miguel |
 | destination | dst_geo_country | string | The country associated with the IP address in the network session. | Peru |
 | destination | dst_geo_latitude | string | The latitude of the geographical coordinate associated with the IP address in the network session. | 38.8951 |
 | destination | dst_geo_longitude | string | The longitude of the geographical coordinate associated with the IP address in the network session. | -77.0364 |
 | destination | dst_geo_region | string | The region within a country associated with the IP address in the network session. | East US |
 | destination | dst_interface_guid | string | GUID of the network interface which was used for authentication request (if applicable). Most of the time you would use the interface_name field for the uid. | 7C202E90-2FBE-4275-AB0E-9BF67E04BEDF |
 | destination | dst_interface_name | string | The network interface used for the connection or session by the destination device. | eth02 |
 | destination | dst_ip_addr | ip | IP address assigned to the device generating the event and/or the IP address in the network packet. This could be used in the context of source, destination, device and even NAT when it is provided by an intermediary NAT device such as a firewall. | 192.168.1.2 |
 | destination | dst_mac_addr | string | MAC address of the device where the event was generated or network interface where a connection starts or ends. | 00:11:22:33:44:55 |
 | destination_nat | dst_nat_ip_addr | ip | IP address assigned to the device generating the event and/or the IP address in the network packet. This could be used in the context of source, destination, device and even NAT when it is provided by an intermediary NAT device such as a firewall. | 192.168.1.2 |
 | destination_nat | dst_nat_port_number | integer | Port number used in a network connection. This could be used in the context of source, destination and even NAT when it is provided by an intermediary NAT device such as a firewall. | 138 |
 | destination | dst_packets | integer | The number of packets sent from the destination to the source for the connection or session (Reply). The meaning of a packet is defined by the reporting device. | 5 |
 | destination | dst_port_number | integer | Port number used in a network connection. This could be used in the context of source, destination and even NAT when it is provided by an intermediary NAT device such as a firewall. | 138 |
 | destination | dst_resource_id | string | The resource Id of the destination device in a network connection | /subscriptions/33333333-8888-4444-a115-aaaaaaaaaaaa/resourcegroups/shokobo/providers/microsoft.compute/virtualmachines/sysmachine2 |
 | destination | dst_user_aadid | string | The User Azure AD ID of the identity associated with a cloud network session. It applies to source and destination entities. | 5e8b0f4d-2cd4-4e17-9467-b0f6a5c0c4d0 |
 | destination | dst_user_domain | string | The domain or computer name associated to the user in a session. In active directory, this would be the name of the domain the user belongs to. | CONTOSO |
 | destination | dst_user_name | string | Name of the user associated with the main event (i.e. Network session). There could be a sense of direction depending how it is used together with other entities (i.e. src_user_name or dst_user_name) | wardog |
 | destination | dst_user_sid | string | Security identifier of the user. Typically, the identity used to authenticate a server. | S-1-5-21-1377283216-344919071-3415362939-500 |
 | destination | dst_user_upn | string | In Active Directory, the User Principal Name (UPN) attribute is a user identifier for logging in, separate from a Windows domain login. | dadmin@contoso |
 | destination | dst_zone | string | The network zone of the destination, as defined by the reporting device. | dmz |
 | device | dvc_action | string | If reported by an intermediary device such as a firewall, the action taken by device. | allow |
 | device | dvc_domain | string | Name of the domain the device is part of. | hunt.wardog.com |
 | device | dvc_fqdn | string | The fully qualified domain name of the host | WKHR001.hunt.wardog.com |
 | device | dvc_hostname | string | The host name from which the event/log came from. There may be multiple host names in an event (i.e. syslog could have forwarder host name), this field is to be the most true log host name (i.e. NOT the forwarders name). | bobs.uncle-pc |
 | device | dvc_inbound_interface | string | If reported by an intermediary device such as a firewall, the network interface used by it for the connection to the source device | eth0 |
 | device | dvc_interface_guid | string | GUID of the network interface which was used for authentication request | {2BB33827-6BB6-48DB-8DE6-DB9E0B9F9C9B} |
 | device | dvc_interface_name | string | the name (description) of the network interface that was used for authentication request. You can get the list of all available network adapters using "ipconfig /all" command | Microsoft Hyper-V Network Adapter |
 | device | dvc_ip_addr | ip | IP address assigned to the device generating the event and/or the IP address in the network packet. This could be used in the context of source, destination, device and even NAT when it is provided by an intermediary NAT device such as a firewall. | 192.168.1.2 |
 | device | dvc_mac_addr | string | MAC address of the device where the event was generated or network interface where a connection starts or ends. | 00:11:22:33:44:55 |
 | device | dvc_outbound_interface | string | If reported by an intermediary device such as a firewall, the network interface used by it for the connection to the destination device. | Ethernet 4 |
 | event | event_count | integer | The number of aggregated events, if applicable | 10 |
 | event | event_end_time | datetime | The time in which the event ended | 2017-04-12 12:00:00 |
 | event | event_message | string | A general message or description, either included in, or generated from the record | TCP access denied |
 | event | event_original_uid | string | Original unique ID specific to the log/event as recorded from the source. | CMzY3i4YoNZ3mT5yu5 |
 | event | event_product | string | The product generating the event. Vendor and product might be the same for some data sources. | Windows |
 | event | event_product_version | string | The version of the product generating the event | 10 |
 | event | event_report_url | string | url of the full analysis report, if applicable | https://192.168.1.1/reports/ade-123-afa.log |
 | event | event_resource_id | string | The resource ID of the device generating the message. | /subscriptions/aaabbbcc-dddd-eeee-1234-1234567890ab/resourcegroups/shokobo/providers/microsoft.compute/virtualmachines/sysmachine |
 | event | event_result | string | The result reported for the activity. Empty value when not applicable | success |
 | event | event_result_details | string | Reason or details for the result reported in event_result | Wrong Password |
 | event | event_schema_version | string | Azure Sentinel Schema Version | 0.1 |
 | event | event_severity | string | The severity of the event as defined manually or usually via the original log, commonly this would be syslog severity. The number codes should be converted to their corresponding string value. | high |
 | event | event_start_time | datetime | The time in which the event stated | 2017-01-21 09:12:34 |
 | event | event_sub_type | string | If there are subsets of an event log type, this field carries the next level value. i.e For windows, it would be the Security channel. | Security |
 | event | event_time_ingested | datetime | The time the event was ingested to SIEM or data pipeline. | 2157-01-21 09:12:34 |
 | event | event_type | string | Type of event being collected. i.e For Windows it would be the Event Provider (Microsoft-Windows-Security-Auditing). I.e. Paloalto, it would be the type of event such as Traffic or Threat. I.e. Zeek Logs, one example could be the conn.log. | Microsoft-Windows-Security-Auditing |
 | event | event_uid | string | Original unique ID specific to the log/event assigned to the event (not original). | 516a64e3-8360-4f1e-a67c-d96b3d52df54 |
 | event | event_vendor | string | The vendor of the product generating the event | Microsoft |
 | file | file_extension | string | The extension name or type of the file. | exe |
 | file | file_hash_md5 | string | MD5 hash of the image/binary/file | 6A255BEBF3DBCD13585538ED47DBAFD7 |
 | file | file_hash_sha1 | string | SHA1 hash of the image/binary/file | B0BF5AC2E81BBF597FAD5F349FEEB32CAC449FA2 |
 | file | file_hash_sha256 | string | SHA256 hash of the image/binary/file | 4668BB2223FFB983A5F1273B9E3D9FA2C5CE4A0F1FB18CA5C1B285762020073C |
 | file | file_hash_sha512 | string | SHA512 hash of the image/binary/file | 1AD1D79F85D8F6A50EA282F63898D652661DAA0C1FD361C22647CABC98A70E8CBCE83200D579D10DD0A3D46BE9496DCDFDDF28B0C5E9709343B032A8796FBECB |
 | file | file_mime_type | string | MIME type name specified for the file | application/msword |
 | file | file_name | string | name of the file without its full path. This could be a local file or one transmitted over the network. | a.exe |
 | file | file_path | string | full path of a file including the name of the file. This could be a local file or one transmitted over the network. | C:\users\wardog\z.exe |
 | file | file_size | integer | Size of the file, in bytes. | 45 |
 | http | http_content_type | string | The HTTP Response content type header for HTTP/HTTPS network sessions. |  |
 | http | http_referrer_original | string | HTTP header "Referer". The HTTP referer header for HTTP/HTTPS network sessions. | https://sub.domain.tld/path/a/b/JavaScript |
 | http | http_request_method | string | Type of HTTP request that was made. Other examples could be (anything) PUT, POST, HEAD, DELETE | GET |
 | http | http_request_time | integer | The amount of time in milliseconds it took to send the request to the server, if applicable. | 700 |
 | http | http_request_xff | string | The HTTP X-Forwarded-For header for HTTP/HTTPS network sessions. | 203.0.113.195 |
 | http | http_response_time | inte | The amount of time in milliseconds it took to receive a response in the server, if applicable. | 800 |
 | http | http_status_code | integer | HTTP Server reply code | 200 |
 | http | http_user_agent_original | string | The User agent seen in the HTTP request. | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36 |
 | http | http_version | string | HTTP request version | 1.1 |
 | network | network_application_protocol | string | Layer 7 (application) in the OSI model. Ex: HTTP,SMB,FTP,SSH, etc. | HTTP |
 | network | network_bytes | integer | Total bytes for the session. If this field does not exist in the log source, then its possible in your ETL pipeline to combine the source and destination bytes. | 102034 |
 | network | network_direction | string | User/Device defined name of the direction of the connection or session (Inbound or Outbound). | outbound |
 | network | network_duration | integer | The amount of time, in millisecond, for the completion of the network session or connection. | 1500 |
 | network | network_icmp_code | integer | For an ICMP message, ICMP message type numeric value (RFC 2780 or RFC 4443). | 34 |
 | network | network_icmp_type | string | For an ICMP message, ICMP message type text representation (RFC 2780 or RFC 4443) | Destination Unreachable |
 | network | network_packets | long | Total packets for the session. If this field does not exist in the log source, then its possible in your ETL pipeline to combine the source and destination packets | 143 |
 | network | network_protocol | string | Transport layer in the OSI model. Also known as, IP Protocol. Ex: TCP,UDP,ICMP,ICMP-v6, etc. Convert to lowercase | tcp |
 | network | network_rule_name | string | The name or ID of the rule by which DeviceAction was decided upon | AnyAnyDrop |
 | network | network_rule_number | integer | Matched rule number | 23 |
 | network | network_session_id | string | The session identifier as reported by the network sensor device. Typically, not available for connections. | S198_13_1_27_12321_D205_13_1_27_443_0012 |
 | source | src_bytes | integer | The number of bytes sent from the source to the destination for the connection or session. | 100 |
 | source | src_dvc_domain | string | Name of the domain the device is part of. | hunt.wardog.com |
 | source | src_dvc_fqdn | string | The fully qualified domain name of the host | WKHR001.hunt.wardog.com |
 | source | src_dvc_hostname | string | The host name from which the event/log came from. There may be multiple host names in an event (i.e. syslog could have forwarder host name), this field is to be the most true log host name (i.e. NOT the forwarders name). | bobs.uncle-pc |
 | source | src_dvc_ip_addr | ip | IP address assigned to the device generating the event and/or the IP address in the network packet. This could be used in the context of source, destination, device and even NAT when it is provided by an intermediary NAT device such as a firewall. | 192.168.1.2 |
 | source | src_dvc_mac_addr | string | MAC address of the device where the event was generated or network interface where a connection starts or ends. | 00:11:22:33:44:55 |
 | source | src_dvc_model_name | string | The model name of the device | Samsung Galaxy Note |
 | source | src_dvc_model_number | string | The model number of the device | 10 |
 | source | src_dvc_os | string | The OS of the device | iOS |
 | source | src_dvc_type | string | The type of the device | mobile |
 | source | src_geo_city | string | The city associated to the IP address in the network session. | San Miguel |
 | source | src_geo_country | string | The country associated with the IP address in the network session. | Peru |
 | source | src_geo_latitude | string | The latitude of the geographical coordinate associated with the IP address in the network session. | 38.8951 |
 | source | src_geo_longitude | string | The longitude of the geographical coordinate associated with the IP address in the network session. | -77.0364 |
 | source | src_geo_region | string | The region within a country associated with the IP address in the network session. | East US |
 | source | src_interface_guid | string | GUID of the network interface which was used for authentication request (if applicable). Most of the time you would use the interface_name field for the uid. | 7C202E90-2FBE-4275-AB0E-9BF67E04BEDF |
 | source | src_interface_name | string | The network interface used for the connection or session by the source device. | eth02 |
 | source | src_ip_addr | ip | IP address assigned to the device generating the event and/or the IP address in the network packet. This could be used in the context of source, destination, device and even NAT when it is provided by an intermediary NAT device such as a firewall. | 192.168.1.2 |
 | source | src_mac_addr | string | MAC address of the device where the event was generated or network interface where a connection starts or ends. | 00:11:22:33:44:55 |
 | source_nat | src_nat_ip_addr | ip | IP address assigned to the device generating the event and/or the IP address in the network packet. This could be used in the context of source, destination, device and even NAT when it is provided by an intermediary NAT device such as a firewall. | 192.168.1.2 |
 | source_nat | src_nat_port_number | integer | Port number used in a network connection. This could be used in the context of source, destination and even NAT when it is provided by an intermediary NAT device such as a firewall. | 138 |
 | source | src_packets | integer | The number of packets sent from the source to the destination for the connection or session. The meaning of a packet is defined by the reporting device. | 5 |
 | source | src_port_number | integer | Port number used in a network connection. This could be used in the context of source, destination and even NAT when it is provided by an intermediary NAT device such as a firewall. | 138 |
 | source | src_resource_id | string | The resource Id of the source device in a network connection | /subscriptions/33333333-8888-4444-a115-aaaaaaaaaaaa/resourcegroups/shokobo/providers/microsoft.compute/virtualmachines/sysmachine2 |
 | source | src_user_aadid | string | The User Azure AD ID of the identity associated with a cloud network session. It applies to source and destination entities. | 5e8b0f4d-2cd4-4e17-9467-b0f6a5c0c4d0 |
 | source | src_user_domain | string | The domain or computer name associated to the user in a session. In active directory, this would be the name of the domain the user belongs to. | CONTOSO |
 | source | src_user_name | string | Name of the user associated with the main event (i.e. Network session). There could be a sense of direction depending how it is used together with other entities (i.e. src_user_name or dst_user_name) | wardog |
 | source | src_user_sid | string | Security identifier of the user. Typically, the identity used to authenticate a server. | S-1-5-21-1377283216-344919071-3415362939-500 |
 | source | src_user_upn | string | In Active Directory, the User Principal Name (UPN) attribute is a user identifier for logging in, separate from a Windows domain login. | dadmin@contoso |
 | source | src_zone | string | The network zone of the source, as defined by the reporting device. | dmz |
 | threat | threat_category | string | Trojan The category of a threat identified by a security system such as Web Security Gateway of an IPS and is associated with this network session. | Trojan |
 | threat | threat_id | string | The ID of a threat identified by a security system such as Web Security Gateway of an IPS and is associated with this network session. | Tr.124 |
 | threat | threat_name | string | The name of the threat or malware identified | EICAR Test File |
 | url | url_category | string | The defined grouping of a URL (or could be just based on the domain in the URL) related to what it is (ie: adult, news, advertising, parked domains, etc) | Search Engines |
 | url | url_hostname | string | The domain/host/hostname of the URL. This could be an IP address or any variation of a value but is more than likely a domain/hostname | google.com |
 | url | url_original | string | The entirety of the URL combined together and or the URL in the truest form from the log source. Some log sources will already parse out portions of the URL into their respective fields. Other logs will even parse out the portions of the URL into their respective field but also include the "original" URL. Always try to include this field, because HTTP/URLs never truly have to conform to any RFC/implementation and thus any parsing/logging implementation could have any number of assumptions/mistakes - therefore it is best to keep a original value | ftp://BigwheelPassword:BigwheelBobUser@google.com:8088/common/Current/client/search/greatsearch.php?hash=215696fc36392ca70f89228b98060afb%20processname=example.exe#gid=l1k4h |
