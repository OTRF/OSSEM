# Domain vs FQDN vs Host Name Implementation

This guide will show you how to label FQDNs, Domains, and Hostnames (for both source/destination) commonly found in logs for Endpoint, DNS, HTTP, SSL, SMB, Radius, URLs, etc...  
However, there is an incredible amount of ambiguity, in logging, regarding the values for a Domain, Hostname, and FQDN (fully qualified domain name).

Therefore, we are going to (try) to clear up this ambiguity in order to properly implement a schema.  The order of this guideline is as follows (skip to [Implementation](./domain_or_hostname_or_fqdn.md#Implementation) if you have already read the definitions and problem framing)  
1. Explain the [Common Definitions](./domain_or_hostname_or_fqdn.md#Common-Definitions), apart from this schema, for these three terms. 
2. Show some [examples](./domain_or_hostname_or_fqdn.md#Examples-of-Ambiguity) that cause ambiguity in these common definitions. 
3. Outline and guideline for how to perform the [Implementation](./domain_or_hostname_or_fqdn.md#Implementation) for this schema  

## Common Definitions
The following are the most common definitions for a Domain, Hostname, and FQDN. We will use the example value `bob-berto-pc.bigwheel.corporation.local` as the example to visualize the definitions. 
### FQDN
The absolute (entire) value of the DNS hierarchy from the lowest level to the top level domain (TLD). Consists of the Hostname and Domain. This is best defined in [this Wikipedia](https://en.wikipedia.org/w/index.php?title=Fully_qualified_domain_name&oldid=911195384#Syntax) article on FQDN.  
example FQDN value = `bob-berto-pc.bigwheel.corporation.local`
### Hostname
The name of a host, device, node, or entity that is separate from the FQDN and Domain. Think of this in the context of running the "hostname" command.  
example Hostname value = `bob-berto-pc`
### Domain
The (DNS) hierarchy that encompasses multiple hosts (ie: a Windows Active Directory environment).  
example Domain value = `bigwheel.corporation.local`

## Examples of Ambiguity
Lets use some common examples that will (hopefully) begin to illustrate the ambiguity in being able to determine what is "truly" the FQDN, Hostname, or Domain from a logging perspective.  

### Background
- Organization owns `corporation.local`
- Active Directory forest at `bigwheel.corporation.local`
- Another AD environment that is a sub domain of their AD forest, and is located at `finance-group.bigwheel.corporation.local`
- External web server at `www.corporation.local`
- Internal ISS server hosting a Wiki at `wiki.bigwheel.corporation.local`
- You have logging for both endpoint, the IIS sever, DNS, HTTP, SSL, Proxy, and other network logs.

#### Scenario 1
HTTP request for `wiki.bigwheel.corporation.local` was made by an endpoint. You now have the following log sources and their field name for this value:
1. Proxy log defining the field as `hostname`
2. Endpoint log defining the field as `DestinationDomain`
3. DNS log defining the field as `dns_query`
4. IIS web server log defining two fields, **a)** `destination_hostname` with the value `wiki` and **b)** `destination_domain` with the value `bigwheel.corporation.local`
##### Scenario 1 Problem Framing
Now, because you have 4 logs that you can (and should definitely) pivot between related to this 1 HTTP request, you set out to define these fields into a common format in order to accomplish this pivoting
- The proxy log defining the field as `hostname` is incorrect, we know that the hostname is actually `wiki`
- The endpoint log using the verbiage `DestinationDomain` is incorrect, we know that `Domain` is actually `bigwheel.corporation.local`
- The DNS log, at least took a passive stance and just labeled the value specific to the DNS application - however we are left with being able to pivot from this DNS query to the other log sources (if we don't change it) 
- The IIS log correctly labels the fields. However, this is a very critical piece that in many scenarios you may not have this level of intimate knowledge into the environment. The endpoint log that belongs to the same (AD) domain as the web server, had no knowledge of the destination's hostname or (AD) domain! Also, you may be just placing a network sensor for incident response.
#### Scenario 2
Endpoint makes an HTTP request to an external IP (Destination IP) with the HTTP Host header set via the command line in cURL of `mwi2xha9lpqn41lo`. For example, the command `curl --header "Host: mwi2xha9lpqn41lo" http://8.8.8.8/` was used. You now have the following log sources and their field name for this value:
1. Proxy log defining the field as `hostname`
2. Endpoint log defining the field as `DestinationDomain`
##### Scenario 2 Problem Framing
Now, because the connection was direct to an IP, we don't have a DNS log but we have two log sources with the same value that we would want to pivot on.
-  The value has no clear indication of whether its a FQDN, Hostname, or Domain. It is just random characters and doesn't even include any TLD. Whether this is malicious or not, is irrelevant - this sort of things happens consistently whether by mistake or malicious intent and for the purpose of this guideline - we are interested in normalizing fields into a schema..before we take the next step of determining the intent of malicious, mistake, or bad practice/hygiene.
- Also, lets say the Host header wasn't set and instead the command , and instead the command `curl http://8.8.8.8/` was used. You now have two fields with the value `8.8.8.8` (outside of the Destination IP). Again, this is definitely not a FQDN, Hostname, or Domain - and you don't want to delete the field either.

------------------------------------------------------------------------------------------------------
## Implementation
Due to the ambiguity that will happen in log sources and not being able to, always let alone the majority of the time, distinguish the FQDN vs the Domain vs the Hostname as well as the confusion caused by log source's field names - we will define definitions in order that this delineation is NOT necessary between the three. Also, provide specific examples of log sources and what to call the fields, in order to even further clear any ambiguity.

These apply to both source and destination FQDNs, Domains, and hostnames. Therefore, if you only see destination verbiage below - just replace that with source for the applicable log scenario.

### Implementation Outline
#### FQDN
This is an optional field. Because there are many scenarios (as briefly outlined above) where one can NOT determine the true FQDN, we will leave this field as defined but should only be used if the log source has intimate knowledge that this is in fact the FQDN.
#### Hostname
This field should always exist if there is some sort of domain, FQDN, or hostname in the log/event.
#### Domain
This field is optional. Because there are many scenarios (as briefly outlined above) where one can NOT determine the true domain, we will leave this field as defined but should only be used if the log source has intimate knowledge that this is in fact the domain.

#### Implementation Field Examples:
- `dst_host_name`
- `dst_domain`
- `dst_fqdn`
- `src_host_name`
- `src_domain`
- `src_fqdn`

### Implementation Examples
1. Sysmon [EventID:3 network connection event log](https://github.com/hunters-forge/OSSEM/blob/master/data_dictionaries/windows/sysmon/events/event-3.md) field for `DestinationHostName` should be set as `dst_host_name`
2. HTTP or Proxy or web server application logs (ie: IIS, Apache, NGINX, etc...), with the hostname/domain (also known as the HTTP Host header) should be set as `dst_host_name`  
this would include:
    - Zeek HTTP field `host`
    - Suricata HTTP field `hostname`
    - NGINX field `hostname`
    - IIS field `vhost`
3. TLS/SSL server name (SNI) should be set as `dst_host_name`
    - Zeek SSL field `server_name`
    - Suricata TLS field `sni`
    - NGINX field `hostname`
    - IIS field `vhost`
4. Kerberos service name should be set as `dst_host_name`
5. Sysmon [EventID:22 dns query event log](https://github.com/hunters-forge/OSSEM/blob/master/data_dictionaries/windows/sysmon/events/event-22.md) field for `QueryName` should be set as `dst_host_name`
6. DNS query name field should be set as `dst_host_name`
    - Zeek DNS field `query`
    - Suricata DNS field `rrname`
7. For events/logs with URLs or URIs and the HTTP Host header (option 2) doesn't exist, parse the hostname/domain portion out of the URL.  
For example:
    - Zeek or Suricata HTTP log, skip this because it is defined in option 2
    - PaloAlto Threat log using the field `URL/Filename` field as [outlined here](https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/monitoring/use-syslog-for-monitoring/syslog-field-descriptions.html) , after first renaming to `url.original` as defined in [URL Schema](https://github.com/hunters-forge/OSSEM/blob/master/common_information_model/entities/url.md), you would parse the domain/host out of this field and then set it as `dst_host_name`
8. RDP client/source name should be set as  `src_host_name`
9. Endpoint (ie: Windows/Linux) logs that do **NOT** apply to the following:  
    a) defined in the use cases above  
    b) already defined in [data dictionaries](https://github.com/hunters-forge/OSSEM/tree/master/data_dictionaries) (ex: [Windows Kerberos EventID:4768](https://github.com/hunters-forge/OSSEM/blob/master/data_dictionaries/windows/etw-providers/Microsoft-Windows-Security-Auditing/events/event-4768.md), [Windows Logon EventID:4624](https://github.com/hunters-forge/OSSEM/blob/master/data_dictionaries/windows/etw-providers/Microsoft-Windows-Security-Auditing/events/event-4624_v2.md))  
    c) logically fit into Target or and are NOT 
    1. FQDN and Domain values exist.
        - Set the field for the FQDN value as `dst_fqdn`  
        - Copy the value for `dst_fqdn` into the field `dst_host_name`  
        - Set the field for the Domain value as `dst_domain` 
    2. FQDN and Hostname and Domain values exist  
        - Set the field for the FQDN value as `dst_fqdn`
        - Set the field for Domain value as `dst_domain`
        - Set the field for the Hostname value as `dst_host_name`
    3. Hostname and Domain values exist
        - Set the field for the Domain value as `dst_domain`
        - Set the field for the Hostname value as `dst_host_name`
    4. Hostname value only exists
        - Set the field for the Hostname value as `dst_host_name`
    5. Domain value only exists
        - Set the field for the Domain value as `dst_domain`
        - Copy the value for `dst_domain` into the field `dst_host_name`
    6. FQDN value only exists
        - Set the field for the FQDN value as `dst_fqdn`  
        - Copy the value for `dst_fqdn` into the field `dst_host_name`