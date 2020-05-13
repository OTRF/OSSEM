# Meta Schema

Added fields that are derived from an event's data/fields after it is has been logged or stored and more specifically could change based on future information. In the simplest form, this would include enrichments of the data.
A good example, would be the Autonomous System Number lookup of an IP address. The reason, is because an IP address on 2018-01-01 may belong to one entity and the later in the future could be acquired by a new entity and thus the data from 2018-01-01 may be different than say 2022-01-01. Actually, a great example of this example is the IP address `1.1.1.1` that for a long time belonged to APNIC, and then was acquired by Cloudflare in 2019. The Meta schema, is a way that can help aide an analyst to know the field they are looking at may be derived from a data source or calculation that could change over time.  

The best way to use this field schema, may be to copy the fields/values that may already exist in a dataset to one of the following categories.  
For example: a url category would be set to `meta_dst_host_name_category`


## Data Fields
|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
| meta_dst_host_name_category                    | string    | Used for URL/domain category (ie: Adult, Abuse, Parked, RFC-1918, etc)                                                                           | `` |
| meta_powershell_param_value_has_non_ascii      | boolean   |                                                                                                                                                  | `` |
| meta_powershell_scriptblock_text_has_non_ascii | boolean   |                                                                                                                                                  | `` |
| meta_powershell_scriptblock_text_length        | integer   |                                                                                                                                                  | `` |
| meta_process_command_line_has_net              | boolean   | if `process_command_line` contains `http:` or `ftp:\\` or `smb:\\` or `file:\\` or `://` or `localhost` or r`\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}` | `` |
| meta_process_command_line_has_non_ascii        | boolean   |                                                                                                                                                  | `` |
| meta_process_command_line_length               | integer   |                                                                                                                                                  | `` |
| meta_target_user_name_is_machine               | boolean   |                                                                                                                                                  | `` |
| meta_user_name_is_machine                      | boolean   |                                                                                                                                                  | `` |
| meta_user_reporter_name_is_machine             | boolean   |                                                                                                                                                  | `` |
| TBD                                            | string    | Data describing an alert                                                                                                                         | `` |
| TBD                                            | geo_point | Geo longitude and latitude point of a field                                                                                                      | `` |
| TBD                                            | integer   | Autonomous System (AS) number (BGP AS Number)                                                                                                    | `` |
| TBD                                            | string    | Autonomous System (AS) organization (BGP AS Name)                                                                                                | `` |
| ttp                                            | string    | Tactic, technique, and procedure                                                                                                                 | `` |



# Fingerprint Schema
Enrichments that create a unique value (fingerprint)

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
| fingerprint_network_community_id             | string | Network community ID as outlined by the standard from https://github.com/corelight/community-id-spec. Standardized hashing of network tuple. The combination, most commonly, of Source IP, Source Port, Destination IP, Destination Port, and IP Protocol allows pivoting between multiple log types | 1:EeVyZ07VGj1n0rld+xCLFdM+u8M=
| fingerprint_powershell_param_value_mm3       | string | Murmur3(MM3) hash of `powershell.param.value`                                                                                                                                                                                                                                                        | ``                             |
| fingerprint_powershell_scriptblock_text_sha1 | string | SHA1 hash of `powershell.scriptblock.text`                                                                                                                                                                                                                                                           | ``                             |
| fingerprint_process_command_line_mm3         | string | Murmur3(MM3) hash of `process_command_line`                                                                                                                                                                                                                                                          | ``                             |
