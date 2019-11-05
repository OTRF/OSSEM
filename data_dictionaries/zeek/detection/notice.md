# Notice Log

## Description

## Event JSON

```json
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|     @timestamp     |     ts   |   date_time   |   An absolute time indicating when the notice occurred, defaults to the current network time in epoch     |     `1300475167.096535`     |
|     event_uid     |     uid     |     string     |     Unique ID for the connection.     |     `CHhAvVGS1DHFjwGM9`     |
|     TBD     |     fuid     |     string     |     A file unique ID if this notice is related to a file. If the f field is provided, this will be automatically filled out     |     ``     |
|     TBD     |     file_desc     |     string     |     Frequently files can be “described” to give a bit more context. This field will typically be automatically filled out from an fa_file record. For example, if a notice was related to a file over HTTP, the URL of the request would be shown     |     ``     |
|     TBD     |     file_mime_type     |     string     |     A mime type if the notice is related to a file. If the f field is provided, this will be automatically filled out     |     ``     |
|     TBD     |     src     |     ip     |     Source IP address |     `10.1.1.1`     |
|     network_protocol     |     proto     |     string     |     The transport protocol. Filled automatically when either conn, iconn or p is specified     |     `tcp`     |
|     TBD     |     actions     |     array_string     |     The actions which have been applied to this notice.   |    `Notice::ACTION_LOG`    |
|     TBD     |     dropped     |     boolean     |          present if base/frameworks/notice/actions/drop.bro is loaded Indicate if the $src IP address was dropped and denied network access.   |   `false`  |
|     TBD     |     email_body_sections     |     array_string     |     By adding chunks of text into this element, other scripts can expand on notices that are being emailed. The normal way to add text is to extend the vector by handling the Notice::notice event and modifying the notice in place     |     ``     |
|     TBD     |     msg     |     string     |     The human readable message for the notice.   |   `8.8.8.8 scanned at least 27 unique hosts on port 8181/tcp in 4m55s`    |
|     TBD     |     note     |     string     |     The Notice::Type of the notice.   | `SSL::Certificate_Expires_Soon` |
|     TBD     |     n     |     integer     |     Associated count, or perhaps a status code     |     ``     |
|     TBD     |     peer_descr     |     string     |     Textual description for the peer that raised this notice, including name, host address and port.   |  `ens192-7`  |
|     TBD     |     sub     |     string     |     The human readable sub-message.   |  `Sampled servers: 1.213.145.151, 1.213.145.151, 1.213.145.151, 1.213.145.151, 1.213.145.151`    |
|     TBD     |     subpress_for     |     integer     |     This field indicates the length of time that this unique notice should be suppressed.   |  `3600`  |
|     TBD     |     dst     |     ip     |     Destination address     |     ``     |
|     TBD     |     p     |     integer     |     "Associated port, if we don’t have a ""conn_id"".   |   ``  |
|     TBD     |     remote_location.country_code     |     string     |     The country code     |     ``     |
|     TBD     |     remote_location.region     |     string     |     The region     |     ``     |
|     TBD     |     remote_location.city     |     string     |     The city     |     ``     |
|     TBD     |     remote_location.latitude|double|Latitude     |     ``     |
|     TBD     |     remote_location.longitude|double|Longitude     |     ``     |