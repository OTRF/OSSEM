# Common Information Model

## Description
The common information model facilitates the normalization of data sets by providing a standard way to parse security event logs. It is organized by specific entities associated with event logs and defined in more details by Data Dictionaries. The definitions of each entity and its respective field names are mostly general descriptions that could help and expedite event logs parsing procedures.

## Sub Data Sets
|entities|Description|Tags|
|---|---|---|
|[Alert Schema](entities/alert.md)|Alert fields that describe an indicator from a tool of a possible issue.||
|[Any Schema](entities/any.md)|Fields used to define metadata for a single field to include data from multiple fields with similar/same values/data.  This data is most commonly created from an ETL pipeline. Any fields below that contain a '*' indicates those are searches and not actual fields (key/values). This is because certain values are not desirable to copy/duplicate. However, because of a common schema we can still find are values for a specific common type, without duplicating or copying everything to one field!||
|[Destination Schema](entities/destination.md)|Event fields used to define the destination (server) in a network connection event.||
|[Destination NAT Schema](entities/destination_nat.md)|Event fields used to define the destination NAT (network address translation) in a network connection event.||
|[DNS Schema](entities/dns.md)|Event fields used to define metadata in DNS events. This commonly includes data in logs that contain DNS queries. Including, but not limited to, Zeek dns.log, Suricata DNS, Sysmon EventID 22, Windows DNS debug/trace logs. In the verbiage below, request is used to denote the client (or forwarded address if applicable) that is making the DNS request. This would commonly be the client/source that is looking up a domain. The response/answer, is used to denote the server that responded with the answer or responded to the request/client. It is important to remember that in DNS logs their are multiple servers that may be involved in the response. This is similar to how packets are forwarded through routers.||
|[ETL Schema](entities/etl.md)|Event fields used to define specific metadata about the event during the processing of an ETL pipeline.||
|[Event Schema](entities/event.md)|Event fields used to define specific metadata of the event itself. For example event_uid or event_creation_timestamp||
|[File Schema](entities/file.md)|Event fields used to define metadata about files either locally or over the wire.||
|[Flow Schema](entities/flow.md)|| Standard Name | Type | Description | Sample Value | |--------|---------|-------|-------|||
|[Group Schema](entities/group.md)|Event fields used to define metadata about a security group, or distribution group that is created changed or deleted.||
|[Hash Schema](entities/hash.md)|Event fields used to define metadata about hashes.||
|[Host Schema](entities/host.md)|Event fields used to define metadata about hosts where events are originally created.||
|[HTTP Schema](entities/http.md)|Event fields used to define metadata about HTTP information. This is based on information in the layer 7 (HTTP) application, however can also include HTTP information from an endpoint/server. IIS, Apache, NGINX, proxy logs, and other variances of logs that have HTTP information would go in here. Also, if the HTTP connection is from a decrypted/MITM HTTPS/TLS session then portions of that information, where applicable, would go in here.||
|[IP Schema](entities/ip.md)|Event fields used to define metadata about IP addresses in a network. It follows the standard from the Destination and Source categories.||
|[Kerberos Schema](entities/kerberos.md)|Event fields used to define Kerberos Ticket Granting Service and Kerberos Ticket Granting Tickets.<br> For certificate information within Kerberos see the ./x509_and_certificates.md||
|[Logon Schema](entities/logon.md)|Event fields used to define metadata about logon events.||
|[MAC Schema](entities/mac.md)|Event fields used to define metadata about MAC addresses in a network. It follows the standard from the Destination and Source categories.||
|[Meta Schema](entities/meta.md)|For example: <code>url_category</code> would be copied to <code>meta_url_category</code>||
|[None](entities/meta_dst_host_name.md)|None||
|[Module Schema](entities/module.md)|Event fields used to define metadata about modules in an endpoint.||
|[Network Schema](entities/network.md)|Event fields used to define metadata about network information seen in a typical OSI layer. This includes data both from an endpoint as well as a network monitoring device/application (NSM, Firewall, IPS, IDS, etc...). This differentiates from data that is specific to Source and Destination specific information such as Source or Destination bytes, packets, IP address, mac address, TCP flags.||
|[Pipe Object](entities/pipe.md)|Event fields used to define metadata about pipes being created or connected in an endpoint.||
|[Port Schema](entities/port.md)|Event fields used to define metadata about ports in a network connection.||
|[Process Schema](entities/process.md)|Event fields used to define metadata about processes in an system.||
|[Registry Key Schema](entities/registry.md)|Event fields used to define metadata about registry entries in a system.||
|[Software Schema](entities/software.md)|None||
|[Source Schema](entities/source.md)|Event fields used to define the source (client) in a network connection event.||
|[Source NAT Schema](entities/source_nat.md)|Event fields used to define the source NAT (network address translation) in a network connection event.||
|[Target](entities/target.md)|Event fields used to define entities being targeted by other entities locally in a system. This is different from a network connection event. It is more related to events that involve relationships defined locally by entities such as files, processes,users, etc.||
|[TLS Schema](entities/tls.md)|Event fields used to define metadata about a TLS(SSL) record.<br> This document is a work in progress, but is a foundational start there is included. Specifically the main foundations of TLS info is already in here||
|[URL Schema](entities/url.md)|Event fields used to define metadata about a URL/URI. There is a lot of ambiguity from the community on the difference URL vs URI. Granted, URL would normally include the domain, port (if applicable), user, password, query, fragment, and URI. However, there are many scenarios from log sources where one could not distinguish whether it was the full URL or just the URI.<br> URL data can be seen in various log sources as defined in http.md as well as other applications such as SIP. URLs, especially in HTTP, have a best practice implementation however it is not necessary to adhere for connections/data to be established.||
|[User Shema](entities/user.md)|Event fields used to define metadata about users in an network environment.||
|[User Agent Schema](entities/user_agent.md)|This document is a work in progress, but is a foundational start there is included.||
|[X509 and Certificates Schema](entities/x509_and_certificates.md)|This document is a work in progress, but is a foundational start there is included. Specifically the main foundations of certificate information is already in here.||
