# Software Log

## Description

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
| @timestamp                  | ts               | date_time   | The time at which the software was detected                                                                                                                                                                    | `` |
| host_ip_addr                | host             | ip          | The IP address detected running the software                                                                                                                                                                   | `` |
| dst_port                    | host_p           | integer     | The port on which the software is running. Only sensible for server software                                                                                                                                   | `` |
| zeek_software_name          | name             | string      | Name of the software (e.g. Apache).                                                                                                                                                                            | `` |
| zeek_software_type          | software_type    | string      | The type of software detected (e.g. HTTP::SERVER).                                                                                                                                                             | `` |
| software_name_original      | unparsed_version | string      | The full unparsed version string found because the version parsing does not always work reliably in all cases and this acts as a fallback in the logs.                                                         | `` |
| url_original                | url              | string      | Most root URL where the software was discovered. present if [policy/protocols/http/detect-webapps.zeek](https://github.com/zeek/zeek/blob/master/scripts/policy/protocols/http/detect-webapps.zeek) is loaded. | `` |
| software_version_additional | version_addl     | string      | Additional version string (e.g. “beta42”).                                                                                                                                                                     | `` |
| software_version_major      | version_major    | integer     | Major version number.                                                                                                                                                                                          | `` |
| software_version_minor1     | version_minor    | integer     | Minor version number.                                                                                                                                                                                          | `` |
| software_version_minor2     | version_minor2   | integer     | Minor subversion number.                                                                                                                                                                                       | `` |
| software_version_minor3     | version_minor3   | integer     | Minor updates number.                                                                                                                                                                                          | `` |
| dst_ip_addr                 | z_Enrichment     | ip          | Enrichment copied from `host_ip_addr`                                                                                                                                                                          | `` |

## Event JSON

```json
```