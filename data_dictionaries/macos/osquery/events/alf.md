# Alf Table

## Description
OS X application layer firewall (ALF) service details.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|allow_signed_enabled|INTEGER|1 If allow signed mode is enabled else 0|`TBD`|
|TBD|firewall_unload|INTEGER|1 If firewall unloading enabled else 0|`TBD`|
|TBD|global_state|INTEGER|1 If the firewall is enabled with exceptions, 2 if the firewall is configured to block all incoming connections, else 0|`TBD`|
|TBD|logging_enabled|INTEGER|1 If logging mode is enabled else 0|`TBD`|
|TBD|logging_option|INTEGER|Firewall logging option|`TBD`|
|TBD|stealth_enabled|INTEGER|1 If stealth mode is enabled else 0|`TBD`|
|TBD|version|TEXT|Application Layer Firewall version|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#alf)

## Tags
* version_4.4.2