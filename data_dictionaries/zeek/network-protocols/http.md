# HTTP Log

## Description

## Event JSON

```json
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|     @timestamp     |     ts               |     date_time     |        Timestamp of the beginning of the event in epoch format     |     `1300475167.096535`  |
|     src_ip_addr     |     id.orig_h     |     ip     |     The originating/source IP address     |     `10.1.1.1`     |
|     src_port     |     id.orig_p          |     integer     |       The originating/source port        |     `37682`     |
|     dst_ip_addr     |     id.resp_h     |     ip     |     The responding/destination IP address     |     `10.2.2.2`     |
|     dst_port     |     id.resp_p          |     integer     |       The responding/destination port        |     `80`     |
|     event_uid     |     uid     |     string     |     Unique ID for the connection.     |     `CHhAvVGS1DHFjwGM9`     |
|     TBD     |     orig_fuids     |     array_string     |          present if base/protocols/http/entities.bro is loaded An ordered vector of file unique IDs.     |     ``     |
|     TBD     |     username     |     string     |     Username if basic-auth is performed for the request     |     ``     |
|     TBD     |     password     |     string     |     Password if basic-auth is performed for the request     |     ``     |
|     TBD     |     resp_fuids     |     array_string     |          present if base/protocols/http/entities.bro is loaded An ordered vector of file unique IDs.     |     ``     |
|     TBD     |     host     |     string     |     Value of the HOST header     |     ``     |
|     TBD     |     cookie_vars     |     array_string     |          present if policy/protocols/http/var-extraction-cookies.bro is loaded Variable names extracted from all cookies." |   `[ "nflx-rgn", "nfvdid", "memclid", "NetflixId" ]`
|     TBD     |     client_header_names     |     array_string     |          present if policy/protocols/http/header-names.bro is loaded The vector of HTTP header names sent by the client. No header values are included here, just the header names.     |     ``     |
|     TBD     |     info_code     |     integer     |     Last seen 1xx informational reply code returned by the server.    |   `101`   |
|     TBD     |     info_msg     |     string     |     Last seen 1xx informational reply message returned by the server.   |  `Switching Protocols`   |
|     TBD     |     method     |     string     |     Verb used in the HTTP request (GET, POST, HEAD, etc.).    |   `GET`   |
|     TBD     |     orig_filenames     |     string     |          present if base/protocols/http/entities.bro is loaded An ordered vector of filenames from the client.   |   ``  |
|     TBD     |     orig_mime_types     |     array_string     |          present if base/protocols/http/entities.bro is loaded An ordered vector of mime types.    |   `["text/plain" , "application/pdf" ]`   |
|     TBD     |     origin     |     string     |     Value of the Origin header from the client     |     ``     |
|     TBD     |     proxied     |     array_string     |     All of the headers that may indicate if the request was proxied. example: `FORWARDED`;`X-FORWARDED-FOR`;`X-FORWARDED-FROM`;`CLIENT-IP`;`VIA`;`XROXY-CONNECTION`;`PROXY-CONNECTION`    |   `X-FORWARDED-FOR -> 1.1.1.1, 10.48.100.11`    |
|     TBD     |     referrer     |     string     |     Value of the "referer" header. The comment is deliberately misspelled like the standard declares, but the name used here is “referrer” spelled correctly     |     ``     |
|     TBD     |     request_body_len     |     integer     |     Actual uncompressed content size of the data transferred from the client     |     `100`     |
|     TBD     |     response_body_len     |     integer     |     Actual uncompressed content size of the data transferred from the server     |     `10000`     |
|     TBD     |     server_header_names     |     array_string     |          present if policy/protocols/http/header-names.bro is loaded The vector of HTTP header names sent by the server. No header values are included here, just the header names.   |   ``  |
|     TBD     |     resp_mime_types     |     array_string     |          present if base/protocols/http/entities.bro is loaded An ordered vector of mime types.    |   `["text/plain" , "application/pdf" ]`   |
|     TBD     |     omniture     |     boolean     |          present if policy/protocols/http/software-browser-plugins.bro is loaded Indicates if the server is an omniture advertising server.   |   ``  |
|     TBD     |     status_code     |     integer     |     Status code returned by the server     |     `200`     |
|     TBD     |     status_msg     |     string     |     Status message returned by the server     |     `OK`     |
|     TBD     |     trans_depth     |     integer     |     Represents the pipelined depth into the connection of this request/response transaction     |     `34`     |
|     TBD     |     version     |     string     |     Value of the version portion of the request.   |    `1.2`   |
|     TBD     |     resp_filenames     |     array_string     |          present if base/protocols/http/entities.bro is loaded An ordered vector of filenames from the server.   |   ``  |
|     TBD     |     flash_version     |     string     |          present if policy/protocols/http/software-browser-plugins.bro is loaded The unparsed Flash version, if detected.   |   ``  |
|     TBD     |     tags     |     array_string     |     A set of indicators of various attributes discovered and related to a particular request/response pair     |     ``     |
|     TBD     |     uri     |     string     |     URI used in the request     |     `/bobs/big/wheel/superawesome.exe`     |
|     TBD     |     uri_vars     |     array_string     |          present if policy/protocols/http/var-extraction-uri.bro is loaded Variable names from the URI.   |   ``  |
|     TBD     |     user_agent     |     string     |     Value of the User-Agent header from the client     |     ``     |