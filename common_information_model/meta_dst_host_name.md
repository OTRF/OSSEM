##### Benefits
1. Single field to query the domains in HTTP, TLS, Kerberos, DNS, etc.
1. Additional/enriched fields that aide in (data) analysis. The additional fields allow more granular outlier detection, statistical scores, etc...
1. Detect IDN or Punycode(emoji) domains
1. Detect Domains that would not be a valid IP or Domain (ie: a domain not containing a dot/period is probably illegitimate)
1. Detect Domains that are an IP Address in SSL or HTTP (ie: its rare that an application such as TLS has a hard coded IP)
1. Detect typosquatting  
Example of a, similar, real world implementation to detect typo squatting:  
https://blog.neu5ron.com/2018/04/typosquatting-detection-with-elk-bro-nsm.html

This document is a work in progress, but is a foundational start is here to be included.