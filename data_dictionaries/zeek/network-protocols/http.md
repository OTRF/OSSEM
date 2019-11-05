# HTTP Log

## Description

## Event JSON

```json
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|#TODO:NewFieldName|@stream|string||
|#TODO:NewFieldName|ts|date_time||
|#TODO:NewFieldName|id.orig_h|ip||
|#TODO:NewFieldName|id.orig_p|integer||
|#TODO:NewFieldName|id.resp_h|ip||
|#TODO:NewFieldName|id.resp_p|integer||
|#TODO:NewFieldName|uid|string|Unique ID for the connection.|
|#TODO:NewFieldName|orig_fuids|array_string|"(present if base/protocols/http/entities.bro is loaded) An ordered vector of file unique IDs."|
|#TODO:NewFieldName|username|string|Username if basic-auth is performed for the request.|
|#TODO:NewFieldName|password|string|Password if basic-auth is performed for the request.|
|#TODO:NewFieldName|resp_fuids|array_string|"(present if base/protocols/http/entities.bro is loaded) An ordered vector of file unique IDs."|
|#TODO:NewFieldName|host|string|Value of the HOST header.|
|#TODO:NewFieldName|cookie_vars|array_string|"(present if policy/protocols/http/var-extraction-cookies.bro is loaded) Variable names extracted from all cookies."|nflx-rgn, nfvdid, memclid, NetflixId;
|#TODO:NewFieldName|client_header_names|array_string|"(present if policy/protocols/http/header-names.bro is loaded) The vector of HTTP header names sent by the client. No header values are included here, just the header names."|
|#TODO:NewFieldName|info_code|integer|Last seen 1xx informational reply code returned by the server.|101;103;102
|#TODO:NewFieldName|info_msg|string|Last seen 1xx informational reply message returned by the server.|Switching Protocols;Continue
|#TODO:NewFieldName|method|string|Verb used in the HTTP request (GET, POST, HEAD, etc.).|GET;POST;HEAD;OPTION
|#TODO:NewFieldName|orig_filenames|string|"(present if base/protocols/http/entities.bro is loaded) An ordered vector of filenames from the client."|
|#TODO:NewFieldName|orig_mime_types|array_string|"(present if base/protocols/http/entities.bro is loaded) An ordered vector of mime types."|"[""text/plain"",""application/pdf""]"
|#TODO:NewFieldName|origin|string|Value of the Origin header from the client.|
|#TODO:NewFieldName|proxied|array_string|"All of the headers that may indicate if the request was proxied. example: ""FORWARDED"";""X-FORWARDED-FOR"";""X-FORWARDED-FROM"";""CLIENT-IP"";""VIA"";""XROXY-CONNECTION"";""PROXY-CONNECTION"","|X-FORWARDED-FOR -> 85.90.222.196, 10.48.100.11
|#TODO:NewFieldName|referrer|string|Value of the “referer” header. The comment is deliberately misspelled like the standard declares, but the name used here is “referrer” spelled correctly.|
|#TODO:NewFieldName|request_body_len|integer|Actual uncompressed content size of the data transferred from the client.|
|#TODO:NewFieldName|response_body_len|integer|Actual uncompressed content size of the data transferred from the server.|
|#TODO:NewFieldName|server_header_names|array_string|"(present if policy/protocols/http/header-names.bro is loaded) The vector of HTTP header names sent by the server. No header values are included here, just the header names."|
|#TODO:NewFieldName|resp_mime_types|array_string|"(present if base/protocols/http/entities.bro is loaded) An ordered vector of mime types."|"[""text/plain"",""application/pdf""]"
|#TODO:NewFieldName|omniture|boolean|"(present if policy/protocols/http/software-browser-plugins.bro is loaded) Indicates if the server is an omniture advertising server."|
|#TODO:NewFieldName|status_code|integer|Status code returned by the server.|
|#TODO:NewFieldName|status_msg|string|Status message returned by the server.|
|#TODO:NewFieldName|trans_depth|integer|Represents the pipelined depth into the connection of this request/response transaction.|
|#TODO:NewFieldName|version|string|Value of the version portion of the request.|1.0;1.1;1.2
|#TODO:NewFieldName|resp_filenames|array_string|"(present if base/protocols/http/entities.bro is loaded) An ordered vector of filenames from the server."|
|#TODO:NewFieldName|flash_version|string|"(present if policy/protocols/http/software-browser-plugins.bro is loaded) The unparsed Flash version, if detected."|
|#TODO:NewFieldName|tags|array_string|A set of indicators of various attributes discovered and related to a particular request/response pair.|
|#TODO:NewFieldName|uri|string|URI used in the request.|
|#TODO:NewFieldName|uri_vars|array_string|"(present if policy/protocols/http/var-extraction-uri.bro is loaded) Variable names from the URI."|
|#TODO:NewFieldName|user_agent|string|Value of the User-Agent header from the client.|