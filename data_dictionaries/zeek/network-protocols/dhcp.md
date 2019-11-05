# DHCP Log

## Description

## Event JSON

```json
```

## Data Dictionary

|	        Standard Name       	|            Field Name             |       	    Type            	|   	    Description          	|	     Sample Value           	|
|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|	-------------------------------	|
|#TODO:NewFieldName|@stream|string|||||||
|#TODO:NewFieldName|ts|date_time|||||||
|#TODO:NewFieldName|client_addr|ip|IP address of the client. If a transaction is only a client sending INFORM messages then there is no lease information exchanged so this is helpful to know who sent the messages. Getting an address in this field does require that the client sources at least one DHCP message using a non-broadcast address.||||||
|#TODO:NewFieldName|server_addr|ip|IP address of the server involved in actually handing out the lease. There could be other servers replying with OFFER messages which won’t be represented here. Getting an address in this field also requires that the server handing out the lease also sources packets from a non-broadcast IP address.||||||
|#TODO:NewFieldName|uids|array_string|A series of unique identifiers of the connections over which DHCP is occurring. This behavior with multiple connections is unique to DHCP because of the way it uses broadcast packets on local networks.||||||
|#TODO:NewFieldName|domain|string|Domain given by the server in option 15.||||||
|#TODO:NewFieldName|host_name|string|Name given by client in Hostname option 12.||||||
|#TODO:NewFieldName|lease_time|float|IP address lease interval.||||||
|#TODO:NewFieldName|agent_remote_id|string|"(present if policy/protocols/dhcp/sub-opts.bro is loaded) A globally unique identifier added by relay agents to identify the remote host end of the circuit."||||||
|#TODO:NewFieldName|assigned_addr|ip|IP address assigned by the server.||||||
|#TODO:NewFieldName|circuit_id|string|"(present if policy/protocols/dhcp/sub-opts.bro is loaded) Added by DHCP relay agents which terminate switched or permanent circuits. It encodes an agent-local identifier of the circuit from which a DHCP client-to-server packet was received. Typically it should represent a router or switch interface number."||||||
|#TODO:NewFieldName|client_message|string|Message typically accompanied with a DHCP_DECLINE so the client can tell the server why it rejected an address.||||||
|#TODO:NewFieldName|client_software|string|"(present if policy/protocols/dhcp/software.bro is loaded) Software reported by the client in the vendor_class option."||||||
|#TODO:NewFieldName|client_fqdn|string|FQDN given by client in Client FQDN option 81.||||||
|#TODO:NewFieldName|mac|string|Client’s hardware address.||||||
|#TODO:NewFieldName|msg_orig|array_ip|"(present if policy/protocols/dhcp/msg-orig.bro is loaded) The address that originated each message from the msg_types field."||||||
|#TODO:NewFieldName|msg_types|array_string|The DHCP message types seen by this DHCP transaction||||||
|#TODO:NewFieldName|requested_addr|ip|IP address requested by the client.||||||
|#TODO:NewFieldName|server_message|string|Message typically accompanied with a DHCP_NAK to let the client know why it rejected the request.||||||
|#TODO:NewFieldName|server_software|string|"(present if policy/protocols/dhcp/software.bro is loaded) Software reported by the server in the vendor_class option."||||||
|#TODO:NewFieldName|subscriber_id|string|"(present if policy/protocols/dhcp/sub-opts.bro is loaded) The subscriber ID is a value independent of the physical network configuration so that a customer’s DHCP configuration can be given to them correctly no matter where they are physically connected."||||||
|#TODO:NewFieldName|duration|float|Duration of the DHCP “session” representing the time from the first message to the last.||||||
|#TODO:NewFieldName|server_addr|n/a|IP address of the server involved in actually handing out the lease. There could be other servers replying with OFFER messages which won’t be represented here. Getting an address in this field also requires that the server handing out the lease also sources packets from a non-broadcast IP address.||||||