# Lldp_neighbors Table
###### Version: 4.4.2

## Description
LLDP neighbors of interfaces.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|interface|TEXT|Interface name|`TBD`|
|TBD|rid|INTEGER|Neighbor chassis index|`TBD`|
|TBD|chassis_id_type|TEXT|Neighbor chassis ID type|`TBD`|
|TBD|chassis_id|TEXT|Neighbor chassis ID value|`TBD`|
|TBD|chassis_sysname|TEXT|CPU brand string, contains vendor and model|`TBD`|
|TBD|chassis_sys_description|INTEGER|Max number of CPU physical cores|`TBD`|
|TBD|chassis_bridge_capability_available|INTEGER|Chassis bridge capability availability|`TBD`|
|TBD|chassis_bridge_capability_enabled|INTEGER|Is chassis bridge capability enabled.|`TBD`|
|TBD|chassis_router_capability_available|INTEGER|Chassis router capability availability|`TBD`|
|TBD|chassis_router_capability_enabled|INTEGER|Chassis router capability enabled|`TBD`|
|TBD|chassis_repeater_capability_available|INTEGER|Chassis repeater capability availability|`TBD`|
|TBD|chassis_repeater_capability_enabled|INTEGER|Chassis repeater capability enabled|`TBD`|
|TBD|chassis_wlan_capability_available|INTEGER|Chassis wlan capability availability|`TBD`|
|TBD|chassis_wlan_capability_enabled|INTEGER|Chassis wlan capability enabled|`TBD`|
|TBD|chassis_tel_capability_available|INTEGER|Chassis telephone capability availability|`TBD`|
|TBD|chassis_tel_capability_enabled|INTEGER|Chassis telephone capability enabled|`TBD`|
|TBD|chassis_docsis_capability_available|INTEGER|Chassis DOCSIS capability availability|`TBD`|
|TBD|chassis_docsis_capability_enabled|INTEGER|Chassis DOCSIS capability enabled|`TBD`|
|TBD|chassis_station_capability_available|INTEGER|Chassis station capability availability|`TBD`|
|TBD|chassis_station_capability_enabled|INTEGER|Chassis station capability enabled|`TBD`|
|TBD|chassis_other_capability_available|INTEGER|Chassis other capability availability|`TBD`|
|TBD|chassis_other_capability_enabled|INTEGER|Chassis other capability enabled|`TBD`|
|TBD|chassis_mgmt_ips|TEXT|Comma delimited list of chassis management IPS|`TBD`|
|TBD|port_id_type|TEXT|Port ID type|`TBD`|
|TBD|port_id|TEXT|Port ID value|`TBD`|
|TBD|port_description|TEXT|Port description|`TBD`|
|TBD|port_ttl|BIGINT|Age of neighbor port|`TBD`|
|TBD|port_mfs|BIGINT|Port max frame size|`TBD`|
|TBD|port_aggregation_id|TEXT|Port aggregation ID|`TBD`|
|TBD|port_autoneg_supported|INTEGER|Auto negotiation supported|`TBD`|
|TBD|port_autoneg_enabled|INTEGER|Is auto negotiation enabled|`TBD`|
|TBD|port_mau_type|TEXT|MAU type|`TBD`|
|TBD|port_autoneg_10baset_hd_enabled|INTEGER|10Base-T HD auto negotiation enabled|`TBD`|
|TBD|port_autoneg_10baset_fd_enabled|INTEGER|10Base-T FD auto negotiation enabled|`TBD`|
|TBD|port_autoneg_100basetx_hd_enabled|INTEGER|100Base-TX HD auto negotiation enabled|`TBD`|
|TBD|port_autoneg_100basetx_fd_enabled|INTEGER|100Base-TX FD auto negotiation enabled|`TBD`|
|TBD|port_autoneg_100baset2_hd_enabled|INTEGER|100Base-T2 HD auto negotiation enabled|`TBD`|
|TBD|port_autoneg_100baset2_fd_enabled|INTEGER|100Base-T2 FD auto negotiation enabled|`TBD`|
|TBD|port_autoneg_100baset4_hd_enabled|INTEGER|100Base-T4 HD auto negotiation enabled|`TBD`|
|TBD|port_autoneg_100baset4_fd_enabled|INTEGER|100Base-T4 FD auto negotiation enabled|`TBD`|
|TBD|port_autoneg_1000basex_hd_enabled|INTEGER|1000Base-X HD auto negotiation enabled|`TBD`|
|TBD|port_autoneg_1000basex_fd_enabled|INTEGER|1000Base-X FD auto negotiation enabled|`TBD`|
|TBD|port_autoneg_1000baset_hd_enabled|INTEGER|1000Base-T HD auto negotiation enabled|`TBD`|
|TBD|port_autoneg_1000baset_fd_enabled|INTEGER|1000Base-T FD auto negotiation enabled|`TBD`|
|TBD|power_device_type|TEXT|Dot3 power device type|`TBD`|
|TBD|power_mdi_supported|INTEGER|MDI power supported|`TBD`|
|TBD|power_mdi_enabled|INTEGER|Is MDI power enabled|`TBD`|
|TBD|power_paircontrol_enabled|INTEGER|Is power pair control enabled|`TBD`|
|TBD|power_pairs|TEXT|Dot3 power pairs|`TBD`|
|TBD|power_class|TEXT|Power class|`TBD`|
|TBD|power_8023at_enabled|INTEGER|Is 802.3at enabled|`TBD`|
|TBD|power_8023at_power_type|TEXT|802.3at power type|`TBD`|
|TBD|power_8023at_power_source|TEXT|802.3at power source|`TBD`|
|TBD|power_8023at_power_priority|TEXT|802.3at power priority|`TBD`|
|TBD|power_8023at_power_allocated|TEXT|802.3at power allocated|`TBD`|
|TBD|power_8023at_power_requested|TEXT|802.3at power requested|`TBD`|
|TBD|med_device_type|TEXT|Chassis MED type|`TBD`|
|TBD|med_capability_capabilities|INTEGER|Is MED capabilities enabled|`TBD`|
|TBD|med_capability_policy|INTEGER|Is MED policy capability enabled|`TBD`|
|TBD|med_capability_location|INTEGER|Is MED location capability enabled|`TBD`|
|TBD|med_capability_mdi_pse|INTEGER|Is MED MDI PSE capability enabled|`TBD`|
|TBD|med_capability_mdi_pd|INTEGER|Is MED MDI PD capability enabled|`TBD`|
|TBD|med_capability_inventory|INTEGER|Is MED inventory capability enabled|`TBD`|
|TBD|med_policies|TEXT|Comma delimited list of MED policies|`TBD`|
|TBD|vlans|TEXT|Comma delimited list of vlan ids|`TBD`|
|TBD|pvid|TEXT|Primary VLAN id|`TBD`|
|TBD|ppvids_supported|TEXT|Comma delimited list of supported PPVIDs|`TBD`|
|TBD|ppvids_enabled|TEXT|Comma delimited list of enabled PPVIDs|`TBD`|
|TBD|pids|TEXT|Comma delimited list of PIDs|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#lldp_neighbors)
