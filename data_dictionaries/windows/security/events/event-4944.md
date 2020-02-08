# Event ID 4944: The following policy was active when the Windows Firewall started.

## Description
This event generates every time Windows Firewall service starts.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|group_policy_applied|GroupPolicyApplied|string|it always has "No" value for this event. This field should show information about: was Group Policy applied for Windows Firewall when it starts or not.|`No`|
|profile|Profile|string|shows the active profile name for the moment Windows Firewall service starts.|`Public`|
|operation_mode|OperationMode|string|On - if "Firewall state:" setting was set to "On" for "Public" profile. Off - if "Firewall state:" setting was set to "Off" for "Public" profile.|`Off`|
|remote_admin_enabled|RemoteAdminEnabled|string|looks like this setting is connected to "Windows Firewall: Allow remote administration exception" Group Policy setting, but it is always Disabled, no matter which option is set for "Windows Firewall: Allow remote administration exception" Group Policy.|`Disabled`|
|multicast_flows_enabled|MulticastFlowsEnabled|string|Enabled - if "Allow unicast response:" Settings configuration was set to "Yes" for "Public" profile. Disabled - if "Allow unicast response:" Settings configuration was set to "No" for "Public" profile.|`Enabled`|
|log_dropped_packets_enabled|LogDroppedPacketsEnabled|string|Enabled - if "Log dropped packets:" Logging configuration was set to "Yes" for "Public" profile. Disabled - if "Log dropped packets:" Logging configuration was set to "No" for "Public" profile.|`Disabled`|
|log_successful_connections_enabled|LogSuccessfulConnectionsEnabled|string|Enabled - if "Log successful connections:" Logging configuration was set to "Yes" for "Public" profile. Disabled - if "Log dropped packets:" Logging configuration was set to "No" for "Public" profile.|`Disabled`|

## References
* [MS Source](https://github.com/MicrosoftDocs/windows-itpro-docs/blob/public/windows/security/threat-protection/auditing/event-4944.md)
* [MS Security Auditing Category - Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings#policy-change)
* [MS Security Auditing Sub-category - Audit MPSSVC Rule-Level Policy Change](https://github.com/MicrosoftDocs/windows-itpro-docs/tree/master/windows/security/threat-protection/auditing/audit-mpssvc-rule-level-policy-change.md)

## Tags
* Policy Change
* Audit MPSSVC Rule-Level Policy Change