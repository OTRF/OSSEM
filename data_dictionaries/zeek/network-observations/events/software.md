# Software Log

## Description
None

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|@timestamp|ts|TBD|date_time|The time at which the software was detected|``|
|TBD|version_addl|TBD|string|Additional version string (e.g. "beta42").|Windows|
|TBD|host|TBD|ip|The IP address detected running the software|``|
|TBD|host_p|TBD|integer|The port on which the software is running. Only sensible for server software|``|
|TBD|version_major|TBD|integer|Major version number.|16|
|TBD|version_minor|TBD|integer|Minor version number.|1|
|TBD|version_minor2|TBD|integer|Minor subversion number.|3497|
|TBD|version_minor3|TBD|integer|Minor updates number.|110|
|TBD|name|TBD|string|Name of the software (e.g. Apache).|Microsoft-CryptoAPI|
|TBD|unparsed_version|TBD|string|The full unparsed version string found because the version parsing does not always work reliably in all cases and this acts as a fallback in the logs.|Microsoft-HTTPAPI/2.0|
|TBD|software_type|TBD|string|The type of software detected (e.g. HTTP::SERVER).|HTTP::BROWSER|
|TBD|url|TBD|string|present if policy/protocols/http/detect-webapps.bro is loaded Most root URL where the software was discovered.|``|
|TBD|version_|TBD|json_object|Version of the software|``|
