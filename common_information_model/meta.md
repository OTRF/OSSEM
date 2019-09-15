# Meta Schema

Added fields that are derived from an event's data/fields after it is has been logged or stored and more specifically could change based on future information. In the simplest form, this would include enrichments of the data.
A good example, would be the Autonomous System Number lookup of an IP address. The reason, is because an IP address on 2018-01-01 may belong to one entity and the later in the future could be acquired by a new entity and thus the data from 2018-01-01 may be different than say 2022-01-01. Actually, a great example of this example is the IP address `1.1.1.1` that for a long time belonged to APNIC, and then was acquired by Cloudflare in 2019. The Meta schema, is a way that can help aide an analyst to know the field they are looking at may be derived from a data source or calculation that could change over time.

The best way to use this field schema, may be to copy the fields/values that may already exist in a dataset to one of the following categories.

For example: `url_category` would be copied to `meta_url_category`

## Data Fields

| Standard Name | Type | Description | Sample Value |
|--------|---------|-------|-------|
| category | string | Description to define a grouping of a value. Commonly used for URL/domain category (ie: Adult, Abuse, Parked, RFC-1918, etc) | `` |
| ttp | string | Tactic, technique, and procedure | `` |
| alert | string | Data describing an alert | `` |
| geo location | geo_point | Geo longitude and latitude point of a field | `` |
| AS Number | integer | Autonomous System (AS) number (BGP AS Number)| `` |
| AS Org | string | Autonomous System (AS) organization (BGP AS Name) | `` |