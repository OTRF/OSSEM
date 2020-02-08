# Data Dictionaries

## Description
This part of the OSSEM project contains specific information about several security event logs organized by operating system and their respective data sets. Each dictionary describes a single event log and its corresponding event field names. The difference between the ../common_information_model/ folder and the data dictionaries is that in the CIM the field definitions are more general whereas in a data dictionary, each field name definition is unique to the specific event log.

## Sub Data Sets
|Data Set|Description|
|---|---|---|
|[macOS](macos/)|Data dictionaries for macOS based events.|
|[Linux](linux/)|Data dictionaries for Linux based events.|
|[Zeek Event Logs](zeek/)|Zeek provides, network, metadata on over 40+ different applications and protocols. Additionally, Zeek provides a framework that enables the community to extend various functionality, protocol analzers/parsers, and or add additional (meta)data. The data is broken up into a log for each application/protocol. For example, all DNS data is stored in dns.log and all HTTP data is stored in http.log. Across all of the logs is over 1,000 fields that contain data ranging from common netflow (ie: bytes, packets, etc..) to application layer data (ie: HTTP headers, TLS Certificate info, etc..). To name just a few of the log types: Connection/Flow, HTTP, SSL/TLS, DNS, RDP, SMB, Kerberos, ModBus, Intel, FTP, SSH, GQUIC, SQL, etc.. It also hashes files and can extract them too. Zeek logs have a unique ability to pivot between logs the various logs via uid fields. For example: an HTTP connection results in a http.log and conn.log. Also, if a file was transferred/downloaded during the connection then there would be an additional files.log. Therefore, you not only obtain HTTP (header) fields, duration of connection, bytes sent/received, packets, hash of the file, size of the file, etc.. but you can pivot between the three logs too! The main field to pivot across will be normalized to event_uid and all other UIDs that can be pivoted/joined across will be set in any_event_uid|
|[Windows](windows/)|Data dictionaries for Windows based events.|
