# Notice Log

## Description

## Event JSON

```json
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|#TODO:NewFieldName|@stream|string||
|#TODO:NewFieldName|ts|date_time|An absolute time indicating when the notice occurred, defaults to the current network time.|
|#TODO:NewFieldName|uid|||
|#TODO:NewFieldName|fuid|string|A file unique ID if this notice is related to a file. If the f field is provided, this will be automatically filled out.|
|#TODO:NewFieldName|file_desc|string|Frequently files can be “described” to give a bit more context. This field will typically be automatically filled out from an fa_file record. For example, if a notice was related to a file over HTTP, the URL of the request would be shown.|
|#TODO:NewFieldName|file_mime_type|string|A mime type if the notice is related to a file. If the f field is provided, this will be automatically filled out.|
|#TODO:NewFieldName|src|ip|"Source address, we don't have a ""conn_id"""|
|#TODO:NewFieldName|proto|string|The transport protocol. Filled automatically when either conn, iconn or p is specified.|
|#TODO:NewFieldName|actions|array_string|The actions which have been applied to this notice.|"""Notice::ACTION_LOG"""
|#TODO:NewFieldName|dropped|boolean|"(present if base/frameworks/notice/actions/drop.bro is loaded) Indicate if the $src IP address was dropped and denied network access."|
|#TODO:NewFieldName|email_body_sections|array_string|By adding chunks of text into this element, other scripts can expand on notices that are being emailed. The normal way to add text is to extend the vector by handling the Notice::notice event and modifying the notice in place.|
|#TODO:NewFieldName|msg|string|The human readable message for the notice.|"""8.8.8.8 scanned at least 27 unique hosts on port 8181/tcp in 4m55s"";8.8.8.8;scanned at least 27 unique hosts on port 52869/tcp in 4m39s"";""An HTTP stalling victim was discovered!;8.8.8.8 seems to be running traceroute using udp"";""SSL certificate validation failed with (unable to get local issuer certificate)"";""SSL certificate validation failed with (certificate has expired)"";""SSL certificate validation failed with (self signed certificate in certificate chain)"";""SSL certificate validation failed with (self signed certificate)"";""1.12.10.62 seems to be running traceroute using icmp"";""174.64.50.36 scanned at least 27 unique hosts on port 443/tcp in 2m14s"";""1.64.10.1 seems to be running traceroute using udp"""
|#TODO:NewFieldName|note|string|The Notice::Type of the notice.|"""SSL::Certificate_Expires_Soon"";""Scan::Address_Scan"";""HTTPStalling::Victim"";""Scan::Port_Scan"";""SSL::Invalid_Server_Cert"";""CaptureLoss::Too_Much_Loss"";""Traceroute::Detected"";""SSH::Password_Guessing"";""PacketFilter::Dropped_Packets"""
|#TODO:NewFieldName|n|integer|Associated count, or perhaps a status code.|
|#TODO:NewFieldName|peer_descr|string|Textual description for the peer that raised this notice, including name, host address and port.|ens192-7
|#TODO:NewFieldName|sub|string|The human readable sub-message.|"""remote"";""Sampled servers: 1.213.145.151, 1.213.145.151, 1.213.145.151, 1.213.145.151, 1.213.145.151"";""local"";""C=US,ST=MN,OU=TEST,O=Code42,CN=50220124"";""CN=*.somedomain.local,OU=Some OU"";""CN=lm.serving-sys.com"""
|#TODO:NewFieldName|subpress_for|integer|This field indicates the length of time that this unique notice should be suppressed.|3600
|#TODO:NewFieldName|dst|ip|Destination address.|
|#TODO:NewFieldName|p|integer|"Associated port, if we don’t have a ""conn_id""."|
|#TODO:NewFieldName|remote_location.|json_object|"(present if policy/protocols/ssh/geo-data.bro is loaded) Add geographic data related to the “remote” host of the connection."|
|#TODO:NewFieldName|remote_location.country_code|string|The country code.|
|#TODO:NewFieldName|remote_location.region|string|The region.|
|#TODO:NewFieldName|remote_location.city|string|The city.|
|#TODO:NewFieldName|remote_location.latitude|double|Latitude.|
|#TODO:NewFieldName|remote_location.longitude|double|Longitude.|