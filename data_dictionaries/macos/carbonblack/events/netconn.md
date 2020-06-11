# ingress.event.netconn (Network Connection)

## Description
A network connection has been received or initiated by an endpoint monitored by Carbon Black.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|cb_server|cb_server|TEXT|Used to distinguish between multiple Cb Response servers. Set this in the "server_name" option of cb-event-forwarder.ini.|`cbserver`|
|host_name|computer_name|TEXT|hostname of the sensor|`test-mac`|
|direction|direction|TEXT|Direction of the netconn event: inbound or outbound|`outbound`|
|domain|domain|TEXT|The DNS name of the network peer, if available.|`carbonblack.com`|
|event_type|event_type|TEXT|The type of event|`netconn`|
|ipv4|ipv4|TEXT|remote ipv4 address of network connection. Maintained for backward compatibility for earlier versions of the event forwarder. See local_ip and remote_ip.|`23.4.187.27`|
|process_link|link_process|TEXT|Deep link to Cb Response UI for process|`https://cbtests/#analyze/00000007-0000-090c-01d1-2099b8f18a82/1`|
|sensor_link|link_sensor|TEXT|Deep link to Cb Response UI for sensor|`https://cbtests/#/host/7`|
|src_ip_addr|local_ip|TEXT|Local IP address of network connection (network interface on the endpoint)|`172.31.30.0`|
|src_port|local_port|INTEGER|Local port of the network connection|`49352`|
|hash|md5|TEXT|md5 of process executable|`C10A66189DC8C090E7C84873EDCEBC88`|
|process_id|pid|INTEGER|Endpoint OS Process id of process|`2316`|
|dst_port|port|INTEGER|remote port of the network connection. Maintained for backward compatibility for earlier versions of the event forwarder. See local_port and remote_port.|`80`|
|process_guid|process_guid|TEXT|Cb Process GUID of process|`00000007-0000-090c-01d1-2099b8f18a82`|
|network_protocol|protocol|INTEGER|6=TCP, 17=UDP|`6`|
|dst_ip_addr|remote_ip|TEXT|IP address of the remote system (peer)|`23.4.187.27`|
|dst_port|remote_port|INTEGER|Remote port of the network connection|`80`|
|sensor_id|sensor_id|INTEGER|sensor ID of associated sensor|`7`|
|event_date_creation|timestamp|INTEGER|Endpoint timestamp of this event since epoch|`1447697666`|
|event_type_detailed|type|TEXT|The full type of event|`ingress.event.netconn`|

## References
* [Carbon Black Developer Docs](https://developer.carbonblack.com/reference/enterprise-response/event-forwarder/event-schema/#ingress-event-netconn-network-connection)
