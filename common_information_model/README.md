# Common Information Model

## Description
The common information model facilitates the normalization of data sets by providing a standard way to parse events and other data found in logs. It is organized by specific entities associated with event logs and defined in more details by [Data Dictionaries](../data_dictionaries). The definitions of each entity and its respective field names are mostly general descriptions that could help and expedite event logs parsing procedures. Also, this helps with the understanding of relationships between events and similarities amongst itself.

The word attribute may also be known, to some, as "field" or "data".
## Sub Data Sets
|entities|Description|Tags|
|---|---|---|
|[Alert](entities/alert.md)|Alert attributes from an event. Most commonly found in an IDS,IPS, AV, event.||
|[Any](entities/any.md)|Added Attributes for a single field to include data from multiple fields with similar values.  This data is most commonly created from an ETL pipeline. Any fields below that contain a '*' indicates those are searches and not actual fields (key/values). This is because certain values are not desirable to copy/duplicate. However, because of a common schema we can still find are values for a specific common type, without duplicating or copying everything to one field!||
|[Destination](entities/destination.md)|Destination (server) attributes in a network connection event.||
|[Destination NAT](entities/destination_nat.md)|Destination NAT (network address translation) attributes in a network connection event.||
|[DNS](entities/dns.md)|DNS attributes. This commonly includes data in logs that contain DNS queries and answers. Including, but not limited to, Zeek dns.log, Suricata DNS, Sysmon EventID 22, Windows DNS debug/trace logs. In the verbiage below, request is used to denote the client (or forwarded address if applicable) that is making the DNS request. This would commonly be the client/source that is looking up a domain. The response/answer, is used to denote the server that responded with the answer or responded to the request/client. It is important to remember that in DNS logs their are multiple servers that may be involved in the response. This is similar to how packets are forwarded through routers.||
|[ETL](entities/etl.md)|Attributes for the event during the processing of an ETL (Extract, Transform, Load) pipeline and or the path an event took (for example: if an event was passed along multiple syslog hosts).||
|[Event](entities/event.md)|Attributes about how the event was collected. This would include, the even creation timestamp, log IDs, what (type) of device/system it came from, and more...||
|[File](entities/file.md)|File attributes including but not limited to, hashes, file names, directories, etc.. These files could be from any types of systems or collection methods (ie: passive network or PCAP extraction).||
|[Group](entities/group.md)|Group attributes for a user, computer, security, distribution, and or other group - that is created, accessed, modified, and or deleted.||
|[Hash](entities/hash.md)|Attributes for hashes. Some examples of hashes would be: the MD5, SHA1, SHA256, SHA512 of a file. Also, custom hashes such as ImpHash or JA3, and TLS,SSL,X509 certificate hash information||
|[Host](entities/host.md)|Host (endpoint, container, VM) attributes where events were originally created.||
|[HTTP](entities/http.md)|HTTP connection attributes from a session, proxy, and or webserver. This is based on information in the layer 7 (HTTP) application, however can also include HTTP information from an endpoint/server. IIS, Apache, NGINX, proxy logs, and other variances of logs that have HTTP information would go in here. Also, if the HTTP connection is from a decrypted/MITM HTTPS/TLS session then portions of that information, where applicable, would go in here.||
|[IP](entities/ip.md)|IP address attributes. This could be both from an endpoint, network monitoring, flow, etc.. It follows the standard from the Destination and Source entities.||
|[Kerberos](entities/kerberos.md)|Kerberos attributes for Kerberos Ticket Granting Service and Kerberos Ticket Granting Tickets.<br> For certificate information within Kerberos see the ./x509_and_certificates.md||
|[Logon](entities/logon.md)|Logon attributes events and information about exisiting logins.||
|[MAC](entities/mac.md)|MAC address attributes. It follows the standard from the Destination and Source categories.||
|[Meta and Fingerprint](entities/meta_and_fingerprint.md)|Added attributes that are derived from an event's data/fields after it is has been logged or stored and more specifically could change based on future information. In the simplest form, this would include enrichment's of the data.||
|[Module](entities/module.md)|Attributes for modules in an endpoint.||
|[Network](entities/network.md)|Network attributes seen in a typical OSI layer. This includes data both from an endpoint as well as a network monitoring device/application (NSM, Firewall, IPS, IDS, etc...). This differentiates from data that is specific to Source and Destination specific information such as Source or Destination bytes, packets, IP address, mac address, TCP flags.||
|[Pipe Object](entities/pipe.md)|Attributes for (named) pipes being created or connected in an endpoint.||
|[Port](entities/port.md)|Port attributes mostly commonly associated with a network connection or a firewall policy modification/creation.||
|[Process](entities/process.md)|Process attributes that are associated with a process created, accessed, exited, etc.. on a system.||
|[Registry Key](entities/registry.md)|Attributes for the (Windows) registry.||
|[Software and Device](entities/software_and_device.md)|Attributes for software or a (build) device and operating system. There are many similar information between and device and operating system and software that these will be kept in one general schema.||
|[Source](entities/source.md)|The source (client) attributes in a network connection.||
|[Source NAT](entities/source_nat.md)|The source NAT (network address translation) attributes in a network connection.||
|[Target](entities/target.md)|Attributes related to when one entity performs an action (ie: modification, creation, etc..) on another entity. This is different from a network connection. It is more related to events that involve relationships defined locally by entities such as files, processes,users, etc.||
|[TLS](entities/tls.md)|TLS (aka SSL) attributes. Most commonly associated with an HTTPS connection.||
|[URL](entities/url.md)|URL/URI attributes. This is most commonly associated with HTTP or proxy/web connections. There is a lot of ambiguity from the community on the difference URL vs URI. Granted, URL would normally include the domain, port (if applicable), user, password, query, fragment, and URI. However, there are many scenarios from log sources where one could not distinguish whether it was the full URL or just the URI.<br> URL data can be seen in various log sources as defined in http.md as well as other applications such as SIP. URLs, especially in HTTP, have a best practice implementation however it is not necessary to adhere for connections/data to be established.||
|[User](entities/user.md)|User attributes including but not limited to: user name, domain, logon ID, etc...||
|[User Agent](entities/user_agent.md)|Attributes for a User Agent. Most commonly found in an HTTP request but can also be found in a protocol like SIP, QUIC, etc..||
|[X509 and Certificates](entities/x509_and_certificates.md)|Certificate attributes from SSL, TLS, X50, Kerberos, etc.. These certificates can be passed via an HTTPs connection, file signing certificate, kerberos, etc..||
