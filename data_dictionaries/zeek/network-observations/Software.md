# Software Log

## Description

## Event JSON

```json
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|#TODO:NewFieldName|@stream|string||
|#TODO:NewFieldName|ts|date_time|The time at which the software was detected.|
|#TODO:NewFieldName|version_addl|string|Additional version string (e.g. “beta42”).|Windows;SecureFX;b01;Linux;e;MID/
|#TODO:NewFieldName|host|ip|The IP address detected running the software.|
|#TODO:NewFieldName|host_p|integer|The port on which the software is running. Only sensible for server software.|
|#TODO:NewFieldName|version_major|integer|Major version number.|16;69
|#TODO:NewFieldName|version_minor|integer|Minor version number.|0;1
|#TODO:NewFieldName|version_minor2|integer|Minor subversion number.|3497
|#TODO:NewFieldName|version_minor3|integer|Minor updates number.|110;100
|#TODO:NewFieldName|name|string|Name of the software (e.g. Apache).|C;Microsoft-CryptoAPI;Chrome;, X–ä5u#ÿ±'¤žV È´Ydiffie-hellman-group;ccmhttp;Microsoft-CryptoAPI;Firefox;WS_FTP;Axway_Desktop_Validator;OC;InstallRoot;<unknown browser>
|#TODO:NewFieldName|unparsed_version|string|The full unparsed version string found because the version parsing doesn’t always work reliably in all cases and this acts as a fallback in the logs.|Microsoft-HTTPAPI/2.0
|#TODO:NewFieldName|software_type|string|The type of software detected (e.g. HTTP::SERVER).|SMTP::WEBMAIL_SERVER;FTP::CLIENT;OS::WINDOWS;HTTP::BROWSER_PLUGIN;Software::UNKNOWN;HTTP::BROWSER;HTTP::SERVER;SSH::CLIENT;SMTP::MAIL_CLIENT;SSH::SERVER;HTTP:APPSERVER
|#TODO:NewFieldName|url|string|"(present if policy/protocols/http/detect-webapps.bro is loaded) Most root URL where the software was discovered."|
|#TODO:NewFieldName|version_|json_object|Version of the software.|