# Zeek Miscellaneous Event Logs

Events regarding abnormal traffic (ie: protocols that are not adhering to an RFC) and or that could commonly be used to try to evade different detections/analyzers for that protocol.

## Data Dictionaries

- [dpd.log](./dpd.md)
- [weird.log](./weird.md)

## Data Dictionary
The following are fields added to each event, for the rest of the fields see its corresponding log 

|	        Standard Name       	|	     Sample Value           	|       	    Type            	|   	    Description          	
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
| event_type                     | miscellaneous             | string | The zeek category of logs |

## Resources

* [Miscellaneous Logs](https://docs.zeek.org/en/stable/script-reference/log-files.html#miscellaneous)
* [DPD Framework Description](https://docs.zeek.org/en/stable/scripts/base/frameworks/dpd/main.zeek.html#base-frameworks-dpd-main-zeek)
* [Weird Framework Description](https://docs.zeek.org/en/stable/scripts/base/frameworks/notice/weird.zeek.html#base-frameworks-notice-weird-zeek)