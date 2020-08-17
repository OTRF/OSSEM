# S3 Server Access Logs
###### Version: 0

## Description
S3 Server Access Log format common schema.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|Bucket Owner|string|The canonical user ID of the source bucket. 
For more information, see [AWS Account Identifiers](https://docs.aws.amazon.com/general/latest/gr/acct-identifiers.html) 
and [Finding Your Account Canonical UserID](https://docs.aws.amazon.com/general/latest/gr/acct-identifiers.html#FindingCanonicalId)
|`79a59df900b949e55d96a1e698fbacedfd6e09d98eacf8f8d5218e7cd47ef2be`|
|TBD|Bucket|string|The name of the bucket that the request was processed against.|`awsexamplebucket`|
|TBD|Time|datetime|The time at which the request was received in UTC format.[%d/%b/%Y:%H:%M:%S %z]|`[06/Feb/2019:00:00:38 +0000]`|
|TBD|Remote IP|string|The apparent internet address of the requester. Intermediate proxies and firewalls might obscure 
the actual address of the machine making the request.
|`192.0.2.3`|
|TBD|Requester|string|The canonical user ID of the requester,or a - for unauthenticated requests.|`79a59df900b949e55d96a1e698fbacedfd6e09d98eacf8f8d5218e7cd47ef2be`|
|TBD|RequestID|string|A string generated by Amazon S3 to uniquely identify each request.|`3E57427F33A59F07`|
|TBD|Operation|string|The operation listed here is declared as SOAP operation, REST.HTTP_method.resource_type,WEBSITE.HTTP_method.resource_type, 
or BATCH.DELETE.OBJECT, or S3.action.resource_type 
for [Lifecycle actions](https://docs.aws.amazon.com/AmazonS3/latest/dev/lifecycle-and-other-bucket-config.html#lifecycle-general-considerations-logging)
|`REST.PUT.OBJECT`|
|TBD|Key|string|The "key" part of the request, URL encoded, or "-" if the operation does not take a key parameter.|`/photos/2019/08/puppy.jpg`|
|TBD|Request-URI|string|The Request-URI part of the HTTP request message.|`"GET /awsexamplebucket/photos/2019/08/puppy.jpg?x-foo=bar HTTP/1.1"`|
|TBD|HTTP status|string|The numeric HTTP status code of the response.|`200`|
|TBD|Error Code|string|The Amazon S3 [Error Code](https://docs.aws.amazon.com/AmazonS3/latest/dev/ErrorCode.html), or "-" if no error occurred.|`NoSuchBucket`|
|TBD|Bytes Sent|string|The number of response bytes sent, excluding HTTP protocol overhead, or "-" if zero.|`2662992`|
|TBD|Object Size|string|The total size of the object in question.|`3462992`|
|TBD|Total Time|string|The number of milliseconds the request was in flight from the server's perspective. 
This value is measured from the time your request is received to the time that the last byte of the response is sent. 
Measurements made from the client's perspective might be longer due to network latency.
|`70`|
|TBD|Turn-Around Time|string|The number of milliseconds that Amazon S3 spent processing your request. 
This value is measured from the time the last byte of your request was received until the time the first byte of the response was sent.
|`10`|
|TBD|Referer|string|The value of the HTTP Referer header, if present. 
HTTP user-agents (for example, browsers) typically set this header to the URL of the linking or embedding page when making a request.
|`"http://www.amazon.com/webservices"`|
|TBD|User-Agent|string|The value of the HTTP User-Agent header.|`"curl/7.15.1"`|
|TBD|Version Id|string|The version ID in the request, or "-" if the operation does not take a versionId parameter.|`3HL4kqtJvjVBH40Nrjfkd`|
|TBD|Host Id|string|The x-amz-id-2 or Amazon S3 extended request ID.|`s9lzHYrFp76ZVxRcpX9+5cjAnEH2ROuNkd2BHfIa6UkFVdtjf5mKR3/eTPFvsiP/XV/VLi31234=`|
|TBD|Signature Version|string|The signature version, SigV2 or SigV4, that was used to authenticate the request or a - for unauthenticated requests.|`SigV2`|
|TBD|Cipher Suite|string|The Secure Sockets Layer (SSL) cipher that was negotiated for HTTPS request or a - for HTTP.|`ECDHE-RSA-AES128-GCM-SHA256`|
|TBD|Authentication Type|string|The type of request authentication used, AuthHeader for authentication headers, QueryString for query string (pre-signed URL) 
or a - for unauthenticated requests.
|`AuthHeader`|
|TBD|Host Header|string|The endpoint used to connect to Amazon S3.Some older Regions support legacy endpoints. 
You may see these endpoints in your server access logs or CloudTrail logs. 
For more information, see [Legacy Endpoints](https://docs.aws.amazon.com/AmazonS3/latest/dev/VirtualHosting.html#s3-legacy-endpoints). 
For a complete list of Amazon S3 Regions and endpoints, 
see [Amazon S3 Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/s3.html) in the AWS General Reference.
|`s3.us-west-2.amazonaws.com`|
|TBD|TLS version|string|"The Transport Layer Security (TLS) version negotiated by the client. 
The value is one of following: TLSv1, TLSv1.1, TLSv1.2; or - if TLS wasn't used."
|`TLSv1.2`|

## References
* [How Do I Enable Server Access Logging for an S3 Bucket?](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/server-access-logging.html)
* [Amazon S3 Server Access Log Format](https://docs.aws.amazon.com/AmazonS3/latest/dev/LogFormat.html)

## Tags
* 2006-03-01