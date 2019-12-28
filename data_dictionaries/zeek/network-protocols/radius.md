# Radius Log

## Description

## Event JSON

```json
{
    "ts": 1249636718.341183,
    "uid": "CyNvve2esjlujRyQI2",
    "id.orig_h": "172.30.166.3",
    "id.orig_p": 1645,
    "id.resp_h": "172.30.166.116",
    "id.resp_p": 1812,
    "username": "xuan",
    "mac": "",
    "result": "success",
    "ttl": 0.015289
}
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|     @timestamp     |     ts               |     date_time     |        Timestamp of the beginning of the event in epoch format     |     `1300475167.096535`  |
|     src_ip_addr     |     id.orig_h     |     ip     |     The originating/source IP address     |     `10.1.1.1`     |
|     src_port     |     id.orig_p          |     integer     |       The originating/source port        |     `37682`     |
|     dst_ip_addr     |     id.resp_h     |     ip     |     The responding/destination IP address     |     `10.2.2.2`     |
|     dst_port     |     id.resp_p          |     integer     |       The responding/destination port        |     `1812`     |
|     event_uid     |     uid     |     string     |     Unique ID for the connection.     |     `CHhAvVGS1DHFjwGM9`     |
|     TBD     |     username     |     string     |     The username, if present.   |   `host/somecomputername.domain.local`    |
|     TBD     |     ttl     |     float     |     The duration between the first request and either the “Access-Accept” message or an error. If the field is empty, it means that either the request or response was not seen     |     ``     |
|     TBD     |     result     |     boolean     |     Successful or failed authentication.   | `failed`    |
|     TBD     |     mac     |     string     |     MAC address, if present     |     ``     |
|     TBD     |     connect_info     |     string     |     Connect info, if present     |     ``     |
|     TBD     |     framed_addr     |     ip     |     The address given to the network access server, if present. This is only a hint from the RADIUS server and the network access server is not required to honor the address     |     ``     |
|     TBD     |     reply_msg     |     string     |     Reply message from the server challenge. This is frequently shown to the user authenticating     |     ``     |
|     TBD     |     tunnel_client     |     string     |     Address (IPv4, IPv6, or FQDN) of the initiator end of the tunnel, if present. This is collected from the Tunnel-Client-Endpoint attribute     |     ``     |