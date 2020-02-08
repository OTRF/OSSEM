# Zeek Event Logs

## Description
Zeek provides, network, metadata on over 40+ different applications and protocols. Additionally, Zeek provides a framework that enables the community to extend various functionality, protocol analzers/parsers, and or add additional (meta)data.
The data is broken up into a log for each application/protocol. For example, all DNS data is stored in dns.log and all HTTP data is stored in http.log.
Across all of the logs is over 1,000 fields that contain data ranging from common netflow (ie: bytes, packets, etc..) to application layer data (ie: HTTP headers, TLS Certificate info, etc..).
To name just a few of the log types: Connection/Flow, HTTP, SSL/TLS, DNS, RDP, SMB, Kerberos, ModBus, Intel, FTP, SSH, GQUIC, SQL, etc.. It also hashes files and can extract them too.
Zeek logs have a unique ability to pivot between logs the various logs via uid fields.
For example: an HTTP connection results in a http.log and conn.log. Also, if a file was transferred/downloaded during the connection then there would be an additional files.log.
Therefore, you not only obtain HTTP (header) fields, duration of connection, bytes sent/received, packets, hash of the file, size of the file, etc.. but you can pivot between the three logs too!
The main field to pivot across will be normalized to event_uid and all other UIDs that can be pivoted/joined across will be set in any_event_uid

## Sub Data Sets
|Data Set|Description|
|---|---|---|
|[Zeek Network Observations Event Logs](network-observations/)|Data collected about certificates, software, hosts, modbus, software, services/applications, etc.. that it has seen over time. Example, the various software seen by a host over time.|
|[Zeek Network Protocol Event Logs](network-protocols/)|Network protocol/application logs containing all the metadata it collects and records for that specific protocol. These are the most commonly used Zeek logs|
|[Zeek Miscellaneous Event Logs](miscellaneous/)|Events regarding abnormal traffic (ie: protocols that are not adhering to an RFC) and or that could commonly be used to try to evade different detections/analyzers for that protocol.|
|[Zeek Diagnostics Event Logs](diagnostics/)|None|
|[Zeek Files Event Logs](files/)|Metadata about files, certificates, and executables that is in addition to the network data.|
|[Zeek Network Control Event Logs](netcontrol/)|Zeek can connect with network devices like, for example, switches or soft- and hardware firewalls using the NetControl framework. The NetControl framework provides a flexible, unified interface for active response and hides the complexity of heterogeneous network equipment behind a simple task-oriented API, which is easily usable via Zeek scripts.|
|[Zeek Detection Event Logs](detection/)|Events related to detection or indicators as well as other things that could or would be considered an alert or something you would want to know occurs.|
