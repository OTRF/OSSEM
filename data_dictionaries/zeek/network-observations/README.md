# Zeek Network Observations Event Logs

Data collected about certificates, software, hosts, modbus, software, services/applications, etc.. that it has seen over time.  
Example, the various software seen by a host over time.

## Data Dictionaries

- [known_certs.log](./known_certs.md)
- [known_hosts.log](./known_hosts.md)
- [known_modbus.log](./known_modbus.md)
- [known_services.log](./known_services.md)
- [software.log](./software.md)

## Data Dictionary
The following are fields added to each event, for the rest of the fields see its corresponding log 

|	        Standard Name       	|	     Sample Value           	|       	    Type            	|   	    Description          	
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
| event_type                     | observations             | string | The zeek category of logs |

## Resources

* [Network Observation Logs](https://docs.zeek.org/en/stable/script-reference/log-files.html#network-observations)
* [Known Certificates Observation Framework](https://docs.zeek.org/en/stable/scripts/policy/protocols/ssl/known-certs.zeek.html#policy-protocols-ssl-known-certs-zeek)
* [Known Hosts Observation Framework](https://docs.zeek.org/en/stable/scripts/policy/protocols/conn/known-hosts.zeek.html#policy-protocols-conn-known-hosts-zeek)
* [Known Services Observation Framework](https://docs.zeek.org/en/stable/scripts/policy/protocols/conn/known-services.zeek.html#policy-protocols-conn-known-services-zeek)
* [Software Observation Framework](https://docs.zeek.org/en/stable/scripts/base/frameworks/software/main.zeek.html#base-frameworks-software-main-zeek)
