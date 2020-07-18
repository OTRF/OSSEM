# HTTP Schema
Event fields used to define metadata about HTTP information. This is based on information in the layer 7 (HTTP) application, however can also include HTTP information from an endpoint/server.
IIS, Apache, NGINX, proxy logs, and other variances of logs that have HTTP information would go in here.
Also, if the HTTP connection is from a decrypted/MITM HTTPS/TLS session then portions of that information, where applicable, would go in here.

## Data Fields
|Standard Name|Type|Description|Sample Value|
|---|---|---|---|
|http_cookie_variables|string|The values of (HTTP) cookies|T1NTRU0K|
|http_informational_code|integer|integer response code of 100-199|101|
|http_informational_message|string|message/text of the integer response code that was 100-199|Switching Protocols|
| http_proxied_headers|string|All of the headers that may indicate if the request was proxied. example: `FORWARDED`;`X-FORWARDED-FOR`;`X-FORWARDED-FROM`;`CLIENT-IP`;`VIA`;`XROXY-CONNECTION`;`PROXY-CONNECTION`|Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36|
| http_referrer_original|string|HTTP header "Referer"|https://google.com|
|http_request_body_bytes|integer|Amount of bytes that the source/client sent|2|
| http_request_header_host|string|Value of the HOST header from the client. This should be copied to `dst_host_name`|www.activewebsoftwares.com|
| http_request_header_names|string|List of any additional (or all) HTTP headers. Because a client can use any HTTP header they want and there are already hundreds of [common HTTP headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers) it would be impossible to define a specific field for each one.|X-Forwarded-For|
| http_request_header_origin|origin|Value of the Origin header from the client||
| http_request_header_values|string|Values for the `http_request_header_names` parameters|10.1.1.1|
|http_request_method|string|Type of HTTP request that was made. Other examples could be (anything) PUT, POST, HEAD, DELETE|GET|
|http_response_body_bytes|integer|Amount of bytes that the destination/server returned|87|
|http_response_body_original|string|The raw HTTP (response) body|<html> <header><title>This is title</title></header> <body> Hello world </body> </html>|
| http_response_header_names|string|List of any additional (or all) HTTP headers. Because a server can use any HTTP header they want and there are already hundreds of [common HTTP headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers) it would be impossible to define a specific field for each one.|X-Forwarded-For|
| http_response_header_values|string|Values for the `http_response_header_names` parameters|10.1.1.1|
|http_status_code|integer|HTTP Server reply code|200|
|http_status_message|string|HTTP server reply message|OK|
|http_version|string|HTTP version|1.1|
|user_agent_original|string|The User agent seen in an HTTP request|Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36|

## References
* [common HTTP headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)
