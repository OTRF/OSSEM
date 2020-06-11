# Elastic Load Balancing(ELB) Access Event Schema

## Description

ELB Access Log format common schema.

## Data Dictionary

|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|timestamp|datetime|The time when the load balancer received the request from the client, in ISO 8601 format.|`2015-05-13T23:39:43.945958Z`|
|TBD|elb|string|The name of the load balancer|`my-loadbalancer`|
|TBD|client:port|string|The IP address and port of the requesting client.|`192.168.131.39:2817`|
|TBD|backend:port|string|The IP address and port of the registered instance that processed this request. <br> If the load balancer can't send the request to a registered instance, or if the instance closes the connection before a response can be sent, this value is set to -. <br> This value can also be set to - if the registered instance does not respond before the idle timeout.c|`10.0.0.1:80`|
|TBD|request_processing_time|string|[HTTP listener] The total time elapsed, in seconds, from the time the load balancer received the request until the time it sent it to a registered instance. <br> [TCP listener] The total time elapsed, in seconds, from the time the load balancer accepted a TCP/SSL connection from a client to the time the load balancer sends the first byte of data to a registered instance. <br> This value is set to -1 if the load balancer can't dispatch the request to a registered instance. This can happen if the registered instance closes the connection before the idle timeout or if the client sends a malformed request. Additionally, for TCP listeners, this can happen if the client establishes a connection with the load balancer but does not send any data. <br> This value can also be set to -1 if the registered instance does not respond before the idle timeout.|`0.000073`|
|TBD|backend_processing_time|string|[HTTP listener] The total time elapsed, in seconds, from the time the load balancer sent the request to a registered instance until the instance started to send the response headers. <br> [TCP listener] The total time elapsed, in seconds, for the load balancer to successfully establish a connection to a registered instance. <br> This value is set to -1 if the load balancer can't dispatch the request to a registered instance. This can happen if the registered instance closes the connection before the idle timeout or if the client sends a malformed request. <br> This value can also be set to -1 if the registered instance does not respond before the idle timeout.| `0.001048`|
|TBD|response_processing_time|string|[HTTP listener] The total time elapsed (in seconds) from the time the load balancer received the response header from the registered instance until it started to send the response to the client. This includes both the queuing time at the load balancer and the connection acquisition time from the load balancer to the client. <br> [TCP listener] The total time elapsed, in seconds, from the time the load balancer received the first byte from the registered instance until it started to send the response to the client. <br> This value is set to -1 if the load balancer can't dispatch the request to a registered instance. This can happen if the registered instance closes the connection before the idle timeout or if the client sends a malformed request. <br> This value can also be set to -1 if the registered instance does not respond before the idle timeout.|`0.000057`|
|TBD|elb_status_code|string|[HTTP listener] The status code of the response from the load balancer.|`200`|
|TBD|backend_status_code|string|[HTTP listener] The status code of the response from the registered instance.|`200`|
|TBD|received_bytes|string|The size of the request, in bytes, received from the client (requester). <br> [HTTP listener] The value includes the request body but not the headers. <br> [TCP listener] The value includes the request body and the headers.|`0`|
|TBD|sent_bytes|string|The size of the response, in bytes, sent to the client (requester). <br> [HTTP listener] The value includes the response body but not the headers. <br> [TCP listener] The value includes the request body and the headers.|`29`|
|TBD|request|string|The request line from the client enclosed in double quotes and logged in the following format: HTTP Method + Protocol://Host header:port + Path + HTTP version. The load balancer preserves the URL sent by the client, as is, when recording the request URI. It does not set the content type for the access log file. When you process this field, consider how the client sent the URL. <br> [TCP listener] The URL is three dashes, each separated by a space, and ending with a space ("- - - ").|`"GET http://www.example.com:80/ HTTP/1.1"`|
|TBD|user_agent|string|[HTTP/HTTPS listener] A User-Agent string that identifies the client that originated the request. The string consists of one or more product identifiers, product[/version]. If the string is longer than 8 KB, it is truncated.|`"curl/7.38.0"`|
|TBD|ssl_cipher|string|[HTTPS/SSL listener] The SSL cipher. This value is recorded only if the incoming SSL/TLS connection was established after a successful negotiation. Otherwise, the value is set to -.|`-`|
|TBD|ssl_protocol|string|[HTTPS/SSL listener] The SSL protocol. This value is recorded only if the incoming SSL/TLS connection was established after a successful negotiation. Otherwise, the value is set to -.|`-`|

## References

- https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/access-log-collection.html
- https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-access-logs.html
