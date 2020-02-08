# Zeek Network Observations Event Logs

## Description
Data collected about certificates, software, hosts, modbus, software, services/applications, etc.. that it has seen over time.
Example, the various software seen by a host over time.

## Sub Data Sets
|events|Description|Tags|
|---|---|---|
|[known_certs](events/known_certs.md)|None||
|[known_hosts](events/known_hosts.md)|None||
|[known_modbus](events/known_modbus.md)|None||
|[known_services](events/known_services.md)|None||
|[software](events/software.md)|None||

## References
* [Network Observation Logs](https://docs.zeek.org/en/stable/script-reference/log-files.html#network-observations)
* [Known Certificates Observation Framework](https://docs.zeek.org/en/stable/scripts/policy/protocols/ssl/known-certs.zeek.html#policy-protocols-ssl-known-certs-zeek)
* [Known Hosts Observation Framework](https://docs.zeek.org/en/stable/scripts/policy/protocols/conn/known-hosts.zeek.html#policy-protocols-conn-known-hosts-zeek)
* [Known Services Observation Framework](https://docs.zeek.org/en/stable/scripts/policy/protocols/conn/known-services.zeek.html#policy-protocols-conn-known-services-zeek)
* [Software Observation Framework](https://docs.zeek.org/en/stable/scripts/base/frameworks/software/main.zeek.html#base-frameworks-software-main-zeek)