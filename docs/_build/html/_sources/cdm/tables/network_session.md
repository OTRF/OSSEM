# network_session

Event fields used to define network sessions.

## Attributes

| Entity | Name | Type | Description | Sample Value |
|:---|:---|:---|:---|:---|
 | cloud | cloud_app_id | string | Unique identifier for an application provided by a cloud service. | 124 |
 | cloud | cloud_app_name | string | The name of an application provided by a cloud service. | AppOne |
 | cloud | cloud_app_risk_level | string | The risk level associated with an application provided by a cloud service | 3 |
 | cloud | cloud_operation | string | Operation performed by an application provided by a cloud service. | DELETE |
 | destination | dst_bytes | integer | network bytes sent by the dst_ip_addr. | 100 |
 | destination | dst_geo_city | string | name of the city | San Miguel |
 | destination | dst_geo_country | string | name of the country | Peru |
 | destination | dst_geo_latitude | string | Latitude is a measurement on a globe or map of location north or south of the Equator. | 38.8951 |
 | destination | dst_geo_longitude | string | Longitude is a measurement of location east or west of the prime meridian at Greenwich, the specially designated imaginary north-south line that passes through both geographic poles and Greenwich, London. | -77.0364 |
 | destination | dst_geo_region | string | name of region | East US |
 | destination | dst_host_name | string | The destination server, host, hostname, domain, or domain name. Some examples, would include the TLS server name, HTTP Host, DNS Query Name, etc. For information on how to define and use this field refer to the documentation [here](https://ossemproject.com/cdm/guidelines/domain_or_hostname_or_fqdn.html) | www.google.com |
 | destination | dst_interface_guid | string | GUID of the network interface which was used for authentication request (if applicable). Most of the time you would use the interface_name field for the uid. | 7C202E90-2FBE-4275-AB0E-9BF67E04BEDF |
 | destination | dst_interface_name | string | The network interface used for the connection or session by the destination device. | eth02 |
 | destination | dst_ip_addr | ip | IP address captured in a network connection. This could be used in the context of source, destination and even NAT when it is provided by an intermediary NAT device such as a firewall. | 192.168.1.2 |
 | destination | dst_mac_addr | string | MAC address of an endpoint or network interface where a connection starts or ends. | 00:11:22:33:44:55 |
 | destination_nat | dst_nat_ip_addr | ip | IP address captured in a network connection. This could be used in the context of source, destination and even NAT when it is provided by an intermediary NAT device such as a firewall. | 192.168.1.2 |
 | destination_nat | dst_nat_port | integer | Port number used in a network connection. This could be used in the context of source, destination and even NAT when it is provided by an intermediary NAT device such as a firewall. | 138 |
 | destination | dst_packets | integer | Network packets sent by the destination (Reply) | 5 |
 | destination | dst_port | integer | Port number used in a network connection. This could be used in the context of source, destination and even NAT when it is provided by an intermediary NAT device such as a firewall. | 138 |
 | destination | dst_resource_group | string | The ID of the group to which the destination device belongs in a network connection. This might be an AWS account, or an Azure subscription or Resource Group | DatabaseVMs |
 | destination | dst_resource_id | string | The resource Id of the destination device in a network connection | /subscriptions/33333333-8888-4444-a115-aaaaaaaaaaaa/resourcegroups/shokobo/providers/microsoft.compute/virtualmachines/sysmachine2 |
 | destination | dst_user_domain | string | subject's domain or computer name of the account that performed the main action in the event | WIN-GG82ULGC9GO |
 | destination | dst_user_name | string | Name of the account that performed the main action in the event. (i.e. user_name authenticated to the box x or user_name spawned a process) | DESKTOP-WARDOG\wardog |
 | destination | dst_user_sid | string | Security identifier of the account that performed the main action in the event | S-1-5-21-1377283216-344919071-3415362939-500 |
 | destination | dst_user_upn | string | UPN of the account for which delegation was requested. | dadmin@contoso |
 | destination | dst_zone | string | The network zone of the destination, as defined by the reporting device. | dmz |
 | device | dvc_action | string | If reported by an intermediary device such as a firewall, the action taken by device. | allow |
 | device | dvc_domain | string | Name of the domain the host is part of or joined. | hunt.wardog.com |
 | device | dvc_fqdn | string | The fully qualified domain name of the host | WKHR001.hunt.wardog.com |
 | device | dvc_host_name | string | The host name from which the event/log came from. There may be multiple host names in an event (i.e. syslog could have forwarder host name), this field is to be the most true log host name (i.e. NOT the forwarders name). | bobs.uncle-pc |
 | device | dvc_inbound_interface | string | If reported by an intermediary device such as a firewall, the network interface used by it for the connection to the source device | eth0 |
 | device | dvc_interface_guid | string | GUID of the network interface which was used for authentication request | {2BB33827-6BB6-48DB-8DE6-DB9E0B9F9C9B} |
 | device | dvc_interface_name | string | the name (description) of the network interface that was used for authentication request. You can get the list of all available network adapters using "ipconfig /all" command | Microsoft Hyper-V Network Adapter |
 | device | dvc_ip_addr | ip | IP address captured in a network connection. This could be used in the context of source, destination and even NAT when it is provided by an intermediary NAT device such as a firewall. | 192.168.1.2 |
 | device | dvc_outbound_interface | string | If reported by an intermediary device such as a firewall, the network interface used by it for the connection to the destination device. | Ethernet 4 |
 | event | event_count | integer | The number of aggregated events, if applicable | 10 |
 | event | event_end_time | datetime | The time in which the event ended | 2017-04-12 12:00:00 |
 | event | event_message | string | A general message or description, either included in, or generated from the record | TCP access denied |
 | event | event_original_uid | string | Original unique ID specific to the log/event as recorded from the source. | CMzY3i4YoNZ3mT5yu5 |
 | event | event_product | string | The product generating the event. Vendor and product might be the same for some data sources. | Windows |
 | event | event_product_version | string | The version of the product generating the event | 10 |
 | event | event_report_url | string | url of the full analysis report, if applicable | https://192.168.1.1/reports/ade-123-afa.log |
 | event | event_resource_group | string | The resource group to which the device generating the record belongs. This might be an AWS account, or an Azure subscription or Resource Group | DBVM |
 | event | event_resource_id | string | The resource ID of the device generating the message. | /subscriptions/aaabbbcc-dddd-eeee-1234-1234567890ab/resourcegroups/shokobo/providers/microsoft.compute/virtualmachines/sysmachine |
 | event | event_schema_version | string | Azure Sentinel Schema Version | 0.1 |
 | event | event_severity | string | The severity of the event as defined manually or usually via the original log, commonly this would be syslog severity. The number codes should be converted to their corresponding string value. | high |
 | event | event_start_time | datetime | The time in which the event stated | 2017-01-21 09:12:34 |
 | event | event_time_ingested | datetime | The time the event was ingested to SIEM or data pipeline. | 2157-01-21 09:12:34 |
 | event | event_uid | string | Original unique ID specific to the log/event assigned to the event (not original). | CMzY3i4YoNZ3mT5yu5 |
 | event | event_vendor | string | The vendor of the product generating the event | Microsoft |
 | file | file_extension | string | The file extension of a file (.txt, .exe, etc) | exe |
 | file | file_hash_md5 | string | MD5 hash of the image/binary/file | 6A255BEBF3DBCD13585538ED47DBAFD7 |
 | file | file_hash_sha1 | string | SHA1 hash of the image/binary/file | B0BF5AC2E81BBF597FAD5F349FEEB32CAC449FA2 |
 | file | file_hash_sha256 | string | SHA256 hash of the image/binary/file | 4668BB2223FFB983A5F1273B9E3D9FA2C5CE4A0F1FB18CA5C1B285762020073C |
 | file | file_hash_sha512 | string | SHA512 hash of the image/binary/file | 1AD1D79F85D8F6A50EA282F63898D652661DAA0C1FD361C22647CABC98A70E8CBCE83200D579D10DD0A3D46BE9496DCDFDDF28B0C5E9709343B032A8796FBECB |
 | file | file_mime_type | string | Specifies the MIME type name specified for a file | application/msword |
 | file | file_name | string | name of a file without its full path. This could be a local file or transmitted over the network. | a.exe |
 | file | file_path | string | full path of a file including the name of the file. | C:\users\wardog\z.exe |
 | file | file_size | string | Specifies the size of a file, in bytes | 45 |
 | http | http_content_type | string | The HTTP Response content type header for HTTP/HTTPS network sessions. |  |
 | http | http_referrer_original | string | HTTP header "Referer". The HTTP referer header for HTTP/HTTPS network sessions. | https://sub.domain.tld/path/a/b/JavaScript |
 | http | http_request_method | string | Type of HTTP request that was made. Other examples could be (anything) PUT, POST, HEAD, DELETE | GET |
 | http | http_request_time | integer | The amount of time in milliseconds it took to send the request to the server, if applicable. | 700 |
 | http | http_response_time | inte | The amount of time in milliseconds it took to receive a response in the server, if applicable. | 800 |
 | http | http_status_code | integer | HTTP Server reply code | 200 |
 | http | http_version | string | HTTP version | 1.1 |
 | http | http_xff | string | The HTTP X-Forwarded-For header for HTTP/HTTPS network sessions. | 203.0.113.195 |
 | network | network_application_protocol | string | Layer 7 (application) in the OSI model. Ex: HTTP,SMB,FTP,SSH, etc. | HTTP |
 | network | network_bytes | long | Total bytes for the session. If this field does not exist in the log source, then its possible in your ETL pipeline to combine the source and destination bytes | 102034 |
 | network | network_direction | string | User/Device defined name of the direction of the connection | outbound |
 | network | network_duration | integer | The amount of time, in millisecond, for the completion of the network session or connection. | 1500 |
 | network | network_packets | long | Total packets for the session. If this field does not exist in the log source, then its possible in your ETL pipeline to combine the source and destination packets | 143 |
 | network | network_protocol | string | Transport layer in the OSI model. Also known as, IP Protocol. Ex: TCP,UDP,ICMP,ICMP-v6, etc. Convert to lowercase | tcp |
 | network | network_session_id | string | The session identifier as reported by the network sensor device. Typically, not available for connections. | S198_13_1_27_12321_D205_13_1_27_443_0012 |
 | operation | op_name | string | The activity associated with the record. Possible specific values are determined by the relevant schema. | Traffic |
 | result | result_reason_type | string | Reason for the result reported in ResultType. | Traffic |
 | result | result_type | string | The result reported for the activity. Empty value when not applicable. | Success |
 | source | src_bytes | integer | network bytes sent by the src_ip_addr | 100 |
 | source | src_geo_city | string | name of the city | San Miguel |
 | source | src_geo_country | string | name of the country | Peru |
 | source | src_geo_latitude | string | Latitude is a measurement on a globe or map of location north or south of the Equator. | 38.8951 |
 | source | src_geo_longitude | string | Longitude is a measurement of location east or west of the prime meridian at Greenwich, the specially designated imaginary north-south line that passes through both geographic poles and Greenwich, London. | -77.0364 |
 | source | src_geo_region | string | name of region | East US |
 | source | src_host_name | string | The source server, host, hostname, domain, or domain name. Some examples, would include the TLS server name, HTTP Host, DNS Query Name, etc. For information on how to define and use this field refer to the documentation [here](https://ossemproject.com/cdm/guidelines/domain_or_hostname_or_fqdn.html) | www.google.com |
 | source | src_interface_guid | string | GUID of the network interface which was used for authentication request (if applicable). Most of the time you would use the interface_name field for the uid. | 7C202E90-2FBE-4275-AB0E-9BF67E04BEDF |
 | source | src_interface_name | string | The network interface used for the connection or session by the source device. | eth02 |
 | source | src_ip_addr | ip | IP address captured in a network connection. This could be used in the context of source, destination and even NAT when it is provided by an intermediary NAT device such as a firewall. | 192.168.1.2 |
 | source | src_mac_addr | string | MAC address of an endpoint or network interface where a connection starts or ends. | 00:11:22:33:44:55 |
 | source_nat | src_nat_ip_addr | ip | IP address captured in a network connection. This could be used in the context of source, destination and even NAT when it is provided by an intermediary NAT device such as a firewall. | 192.168.1.2 |
 | source_nat | src_nat_port | integer | Port number used in a network connection. This could be used in the context of source, destination and even NAT when it is provided by an intermediary NAT device such as a firewall. | 138 |
 | source | src_packets | integer | Network packets sent by the source | 5 |
 | source | src_port | integer | Port number used in a network connection. This could be used in the context of source, destination and even NAT when it is provided by an intermediary NAT device such as a firewall. | 138 |
 | source | src_resource_group | string | The ID of the group to which the source device belongs in a network connection. This might be an AWS account, or an Azure subscription or Resource Group | DatabaseVMs |
 | source | src_resource_id | string | The resource Id of the source device in a network connection | /subscriptions/33333333-8888-4444-a115-aaaaaaaaaaaa/resourcegroups/shokobo/providers/microsoft.compute/virtualmachines/sysmachine2 |
 | source | src_user_domain | string | subject's domain or computer name of the account that performed the main action in the event | WIN-GG82ULGC9GO |
 | source | src_user_name | string | Name of the account that performed the main action in the event. (i.e. user_name authenticated to the box x or user_name spawned a process) | DESKTOP-WARDOG\wardog |
 | source | src_user_sid | string | Security identifier of the account that performed the main action in the event | S-1-5-21-1377283216-344919071-3415362939-500 |
 | source | src_user_upn | string | UPN of the account for which delegation was requested. | dadmin@contoso |
 | source | src_zone | string | The network zone of the source, as defined by the reporting device. | dmz |
 | threat | threat_category | string | The category of a threat identified by a security system such as Web Security Gateway of an IPS and is associated with this network session. | Trojan |
 | threat | threat_id | string | The ID of a threat identified by a security system such as Web Security Gateway of an IPS and is associated with this network session. | tr.076 |
 | threat | threat_name | string | The name of the threat or malware identified | Win32.Small.ahif(90603579) |
 | url | url_category | string | The defined grouping of a URL (or could be just based on the domain in the URL) related to what it is (ie: adult, news, advertising, parked domains, etc) | Search Engines |
 | url | url_host_name | string | The domain/host/hostname of the URL. This could be an IP address or any variation of a value but is more than likely a domain/hostname | google.com |
 | url | url_original | string | The entirety of the URL combined together and or the URL in the truest form from the log source. Some log sources will already parse out portions of the URL into their respective fields. Other logs will even parse out the portions of the URL into their respective field but also include the "original" URL. Always try to include this field, because HTTP/URLs never truly have to conform to any RFC/implementation and thus any parsing/logging implementation could have any number of assumptions/mistakes - therefore it is best to keep a original value | ftp://BigwheelPassword:BigwheelBobUser@google.com:8088/common/Current/client/search/greatsearch.php?hash=215696fc36392ca70f89228b98060afb%20processname=example.exe#gid=l1k4h |
 | user_agent | user_agent_original | string | The User agent seen in an HTTP request | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36 |
