# HTTP Log

## Description
None

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|@timestamp|ts|TBD|date_time|Timestamp of the beginning of the event in epoch format|1230820619|
|src_ip_addr|id.orig_h|TBD|ip|The originating/source IP address|117.195.143.198|
|src_port|id.orig_p|TBD|integer|The originating/source port|2308|
|dst_ip_addr|id.resp_h|TBD|ip|The responding/destination IP address|208.106.128.136|
|dst_port|id.resp_p|TBD|integer|The responding/destination port|80|
|event_uid|uid|TBD|string|Unique ID for the connection.|CZHkS53IZOwi2WQ1Sj|
|zeek_uid_orig_fuids|orig_fuids|TBD|array_string|present if base/protocols/http/entities.bro is loaded An ordered vector of file unique IDs.|``|
|url_user_name|username|TBD|string|Username if basic-auth is performed for the request|bobsyauncle|
|url_user_password|password|TBD|string|Password if basic-auth is performed for the request|bobspassword|
|zeek_uid_resp_fuids|resp_fuids|TBD|array_string|present if base/protocols/http/entities.bro is loaded An ordered vector of file unique IDs.|["FE7s2f1ljAxbVlbasi"]|
|url_host_name|host|TBD|string|Value of the HOST header|www.activewebsoftwares.com|
|http_cookie_variables|cookie_vars|TBD|array_string|present if policy/protocols/http/var-extraction-cookies.bro is loaded Variable names extracted from all cookies."|[ "nflx-rgn", "nfvdid", "memclid", "NetflixId" ]|
|http_request_header_names|client_header_names|TBD|array_string|present if policy/protocols/http/header-names.bro is loaded The vector of HTTP header names sent by the client. No header values are included here, just the header names.|["USER-AGENT", "ACCEPT", "ACCEPT-LANGUAGE", "ACCEPT-ENCODING", "ACCEPT-CHARSET", "KEEP-ALIVE", "CONNECTION", "DATE", "SERVER", "MICROSOFTOFFICEWEBSERVER", "X-POWERED-BY", "CONTENT-LENGTH", "CONTENT-TYPE", "SET-COOKIE", "CACHE-CONTROL"]|
|http_informational_code|info_code|TBD|integer|Last seen 1xx informational reply code returned by the server.|``|
|http_informational_message|info_msg|TBD|string|Last seen 1xx informational reply message returned by the server.|``|
|http_request_method|method|TBD|string|Verb used in the HTTP request (GET, POST, HEAD, etc.).|GET|
|src_file_path|orig_filenames|TBD|string|present if base/protocols/http/entities.bro is loaded An ordered vector of filenames from the client.|``|
|src_mime_type|orig_mime_types|TBD|array_string|present if base/protocols/http/entities.bro is loaded An ordered vector of mime types.|["text/html"]|
|http_header_origin|origin|TBD|string|Value of the Origin header from the client|``|
|http_response_body_original|post_body|TBD|string|Content from the source/client inside the HTTP request body.|{"pkg_utime":"0","conf_utime":"1555582468054"}|
|TBD|proxied|TBD|array_string|All of the headers that may indicate if the request was proxied. example: FORWARDED;X-FORWARDED-FOR;X-FORWARDED-FROM;CLIENT-IP;VIA;XROXY-CONNECTION;PROXY-CONNECTION|``|
|httpreferrer original|referrer|TBD|string|Value of the "referer" header. The comment is deliberately misspelled like the standard declares, but the name used here is "referrer" spelled correctly|http://localcontrol.netflix.com/js/boot.js|
|http_request_body_bytes|request_body_len|TBD|integer|Actual uncompressed content size of the data transferred from the client|0|
|http_response_body_bytes|response_body_len|TBD|integer|Actual uncompressed content size of the data transferred from the server|4951|
|http_response_header_names|server_header_names|TBD|array_string|present if policy/protocols/http/header-names.bro is loaded The vector of HTTP header names sent by the server. No header values are included here, just the header names.|["HOST", "USER-AGENT", "ACCEPT", "ACCEPT-LANGUAGE", "ACCEPT-ENCODING", "ACCEPT-CHARSET", "KEEP-ALIVE", "CONNECTION", "DATE", "SERVER", "MICROSOFTOFFICEWEBSERVER", "X-POWERED-BY", "CONTENT-LENGTH", "CONTENT-TYPE", "SET-COOKIE", "CACHE-CONTROL"]|
|dst_mime_type|resp_mime_types|TBD|array_string|present if base/protocols/http/entities.bro is loaded An ordered vector of mime types.|["text/plain", "application/pdf" ]|
|TBD|omniture|TBD|boolean|present if policy/protocols/http/software-browser-plugins.bro is loaded Indicates if the server is an omniture advertising server.|``|
|http_status_code|status_code|TBD|integer|Status code returned by the server|500|
|http_status_message|status_msg|TBD|string|Status message returned by the server|Internal Server Error|
|TBD|trans_depth|TBD|integer|Represents the pipelined depth into the connection of this request/response transaction|1|
|http_version|version|TBD|string|Value of the version portion of the request.|1.2|
|dst_file_path|resp_filenames|TBD|array_string|present if base/protocols/http/entities.bro is loaded An ordered vector of filenames from the server.|UserHistorySheetNew.xls|
|TBD|flash_version|TBD|string|present if policy/protocols/http/software-browser-plugins.bro is loaded The unparsed Flash version, if detected.|``|
|TBD|tags|TBD|array_string|A set of indicators of various attributes discovered and related to a particular request/response pair|["HTTP::URI_SQLI"]|
|url_original|uri|TBD|string|URI used in the request|/demoactivebusinessdirectory/default.asp?catid=0+and+1=0|
|TBD|uri_vars|TBD|array_string|present if policy/protocols/http/var-extraction-uri.bro is loaded Variable names from the URI.|``|
|user_agent_original|user_agent|TBD|string|Value of the User-Agent header from the client|Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.5) Gecko/2008120122 Firefox/3.0.5|
