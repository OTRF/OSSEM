# Software Log

## Description
None

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|@timestamp|ts|date_time|The time at which the software was detected|````|
|TBD|version_addl|string|Additional version string (e.g. "beta42").|`Windows`|
|TBD|host|ip|The IP address detected running the software|````|
|TBD|host_p|integer|The port on which the software is running. Only sensible for server software|````|
|TBD|version_major|integer|Major version number.|`16`|
|TBD|version_minor|integer|Minor version number.|`1`|
|TBD|version_minor2|integer|Minor subversion number.|`3497`|
|TBD|version_minor3|integer|Minor updates number.|`110`|
|TBD|name|string|Name of the software (e.g. Apache).|`Microsoft-CryptoAPI`|
|TBD|unparsed_version|string|The full unparsed version string found because the version parsing does not always work reliably in all cases and this acts as a fallback in the logs.|`Microsoft-HTTPAPI/2.0`|
|TBD|software_type|string|The type of software detected (e.g. HTTP::SERVER).|`HTTP::BROWSER`|
|TBD|url|string|present if policy/protocols/http/detect-webapps.bro is loaded Most root URL where the software was discovered.|````|
|TBD|version_|json_object|Version of the software|````|
