# HTTP Schema

Event fields used to define metadata about HTTP information. This is based on information in the layer 7 (HTTP) application, however can also include HTTP information from an endpoint/server.
IIS, Apache, NGINX, proxy logs, and other variances of logs that have HTTP information would go in here.
Also, if the HTTP connection is from a decrypted/MITM HTTPS/TLS session then portions of that information, where applicable, would go in here.

## Data Fields

| Standard Name | Type | Description | Sample Value |
|--------|---------|-------|-------|
| http_request_header_names | string | List of any additional (or all) HTTP headers. Because a client can use any HTTP header they want and there are already hundreds of (common HTTP headers)[https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers] it would be impossible to define a specfic field for each one. | "X-Forwarded-For" |
| http_response_header_names | string | List of any additional (or all) HTTP headers. Because a server can use any HTTP header they want and there are already hundreds of (common HTTP headers)[https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers] it would be impossible to define a specfic field for each one. | "X-Forwarded-For" |
