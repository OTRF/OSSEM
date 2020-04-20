# Zeek Network Control Event Logs
Zeek can connect with network devices like, for example, switches or soft- and hardware firewalls using the NetControl framework. The NetControl framework provides a flexible, unified interface for active response and hides the complexity of heterogeneous network equipment behind a simple task-oriented API, which is easily usable via Zeek scripts.

## Data Dictionaries

## Data Dictionary
The following are fields added to each event, for the rest of the fields see its corresponding log 

|	        Standard Name       	|	     Sample Value           	|       	    Type            	|   	    Description          	
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
| event_type                     | netcontrol             | string | The zeek category of logs |


## Resources

* [Network Control Logs](https://docs.zeek.org/en/stable/script-reference/log-files.html#netcontrol)
* [Network Control Framework Description](https://docs.zeek.org/en/stable/frameworks/netcontrol.html)
