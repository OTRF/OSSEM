# RDP Log

## Description

## Event JSON

```json
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|#TODO:NewFieldName|@stream|string|||
|#TODO:NewFieldName|ts|date_time|||
|#TODO:NewFieldName|id.orig_h|ip|||
|#TODO:NewFieldName|id.orig_p|integer|||
|#TODO:NewFieldName|id.resp_h|ip|||
|#TODO:NewFieldName|id.resp_p|integer|||
|#TODO:NewFieldName|uid|string|Unique ID for the connection.||
|#TODO:NewFieldName|cert_count|integer|The number of certs seen. X.509 can transfer an entire certificate chain.||0;4;2;1
|#TODO:NewFieldName|cert_permanent|boolean|Indicates if the provided certificate or certificate chain is permanent or temporary.||true;false
|#TODO:NewFieldName|cert_type|string|If the connection is being encrypted with native RDP encryption, this is the type of cert being used.||RSA;X.509
|#TODO:NewFieldName|client_build|string|RDP client version used by the client machine.||client_build-14393;RDP 5.1;RDP 8.1;client_build-15063;RDP 6.0;RDP 6.1
|#TODO:NewFieldName|client_dig_product_id|string|Product ID of the client machine.||ededcf3e-aa01-4651-5012-f33137f
|#TODO:NewFieldName|client_name|string|Name of the client machine.||SOMECOMPUTERNAME
|#TODO:NewFieldName|cookie|string|Cookie value used by the client machine. This is typically a username.||Administr
|#TODO:NewFieldName|desktop_height|integer|Desktop height of the client machine.||1080
|#TODO:NewFieldName|desktop_width|integer|Desktop width of the client machine.||1920
|#TODO:NewFieldName|encryption_level|string|Encryption level of the connection.||High;Client compatible;Low;FIPS
|#TODO:NewFieldName|encryption_method|string|Encryption method of the connection.||128bit;256bit;encryption_method-16
|#TODO:NewFieldName|keyboard_layout|string|Keyboard layout (language) of the client machine.||English - United States
|#TODO:NewFieldName|requested_color_depth|string|The color depth requested by the client in the high_color_depth field.||32bit;16bit;8bit
|#TODO:NewFieldName|result|string|Status result for the connection. It’s a mix between RDP negotation failure messages and GCC server create response messages.||SSL_NOT_ALLOWED_BY_SERVER;Success;HYBRID_REQUIRED_BY_SERVER;encrypted;SSL_REQUIRED_BY_SERVER;SSL_CERT_NOT_ON_SERVER
|#TODO:NewFieldName|security_protocol|string|Security protocol chosen by the server.||HYBRID;HYBRID_EX;SSL;RDP
|#TODO:NewFieldName|ssl|boolean|"(present if policy/protocols/rdp/indicate_ssl.bro is loaded) Flag the connection if it was seen over SSL."||true;false