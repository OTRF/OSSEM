# Wifi_networks Table
###### Version: 4.4.2

## Description
OS X known/remembered Wi-Fi networks list.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|ssid|TEXT|SSID octets of the network|`TBD`|
|TBD|network_name|TEXT|Name of the network|`TBD`|
|TBD|security_type|TEXT|Type of security on this network|`TBD`|
|TBD|last_connected|INTEGER|Last time this netword was connected to as a unix_time|`TBD`|
|TBD|passpoint|INTEGER|1 if Passpoint is supported, 0 otherwise|`TBD`|
|TBD|possibly_hidden|INTEGER|1 if network is possibly a hidden network, 0 otherwise|`TBD`|
|TBD|roaming|INTEGER|1 if roaming is supported, 0 otherwise|`TBD`|
|TBD|roaming_profile|TEXT|Describe the roaming profile, usually one of Single, Dual  or Multi|`TBD`|
|TBD|captive_portal|INTEGER|1 if this network has a captive portal, 0 otherwise|`TBD`|
|TBD|auto_login|INTEGER|1 if auto login is enabled, 0 otherwise|`TBD`|
|TBD|temporarily_disabled|INTEGER|1 if this network is temporarily disabled, 0 otherwise|`TBD`|
|TBD|disabled|INTEGER|1 if this network is disabled, 0 otherwise|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#wifi_networks)
