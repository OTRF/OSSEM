# Notice Log

## Description
None

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|@timestamp|ts|TBD|date_time|An absolute time indicating when the notice occurred, defaults to the current network time in epoch|1300475167.096535|
|event_uid|uid|TBD|string|Unique ID for the connection.|CHhAvVGS1DHFjwGM9|
|TBD|fuid|TBD|string|A file unique ID if this notice is related to a file. If the f field is provided, this will be automatically filled out|``|
|TBD|file_desc|TBD|string|Frequently files can be "described" to give a bit more context. This field will typically be automatically filled out from an fa_file record. For example, if a notice was related to a file over HTTP, the URL of the request would be shown|``|
|TBD|file_mime_type|TBD|string|A mime type if the notice is related to a file. If the f field is provided, this will be automatically filled out|``|
|TBD|src|TBD|ip|Source IP address|10.1.1.1|
|network_protocol|proto|TBD|string|The transport protocol. Filled automatically when either conn, iconn or p is specified|tcp|
|TBD|actions|TBD|array_string|The actions which have been applied to this notice.|Notice::ACTION_LOG|
|TBD|dropped|TBD|boolean|present if base/frameworks/notice/actions/drop.bro is loaded Indicate if the $src IP address was dropped and denied network access.|false|
|TBD|email_body_sections|TBD|array_string|By adding chunks of text into this element, other scripts can expand on notices that are being emailed. The normal way to add text is to extend the vector by handling the Notice::notice event and modifying the notice in place|``|
|TBD|msg|TBD|string|The human readable message for the notice.|8.8.8.8 scanned at least 27 unique hosts on port 8181/tcp in 4m55s|
|TBD|note|TBD|string|The Notice::Type of the notice.|SSL::Certificate_Expires_Soon|
|TBD|n|TBD|integer|Associated count, or perhaps a status code|``|
|TBD|peer_descr|TBD|string|Textual description for the peer that raised this notice, including name, host address and port.|ens192-7|
|TBD|sub|TBD|string|The human readable sub-message.|Sampled servers: 1.213.145.151, 1.213.145.151, 1.213.145.151, 1.213.145.151, 1.213.145.151|
|TBD|subpress_for|TBD|integer|This field indicates the length of time that this unique notice should be suppressed.|3600|
|TBD|dst|TBD|ip|Destination address|``|
|TBD|p|TBD|integer|"Associated port, if we don't have a ""conn_id"".|``|
|TBD|remote_location.country_code|TBD|string|The country code|``|
|TBD|remote_location.region|TBD|string|The region|``|
|TBD|remote_location.city|TBD|string|The city|``|
|TBD|remote_location.latitude|TBD|double|Latitude|``|
|TBD|remote_location.longitude|TBD|double|Longitude|``|
