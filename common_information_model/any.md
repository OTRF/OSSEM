# Any Schema

Fields used to define metadata for a single field to include data from multiple fields with similar/same values/data.  This data is most commonly created from an ETL pipeline.

## Data Fields

| Standard Name | Type | Description | Sample Value |
|--------|---------|-------|-------|
| any_domain | string | Allows searching a single field for all domains. All domain fields copied/duplicated to a single field as an array. | `[ "google.com", "example.local", "1.1.1.1" ]` |
| any_ip_geo.asn | string | Allows searching a single field for all BGP AS Numbers. All AS number fields copied/duplicated to a single field as an array. | `` |
| any_ip_geo.as_org | string | Allows searching a single field for all BGP AS Organization Names. All AS name fields copied/duplicated to a single field as an array. | `` |
| any_hash | string | Allows searching a single field for all hashes. All hash fields copied/duplicated to a single field as an array. | `` |
| any_ip_addr | string | Allows searching a single field for all IPs. All IP fields copied/duplicated to a single field as an array. | `` |
| any_log_id | string | Allows searching a single field for all log IDs. All log ID fields copied/duplicated to a single field as an array. | `` |
| any_mac_addr | string | Allows searching a single field for all MAC addresses. All MAC address fields copied/duplicated to a single field as an array. | `` |
| any_user | string | Allows searching a single field for all users. All user fields copied/duplicated to a single field as an array. | `` |
| any_vlan_id | integer | Allows searching a single field for all VLAN IDs. All VLAN ID fields copied/duplicated to a single field as an array. | `` |