# DHCP Log

## Description
None

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|@timestamp|ts|date_time|Timestamp of the beginning of the event in epoch format|`1300475167.096535`|
|src_ip_addr|client_addr|ip|IP address of the client. If a transaction is only a client sending INFORM messages then there is no lease information exchanged so this is helpful to know who sent the messages. Getting an address in this field does require that the client sources at least one DHCP message using a non-broadcast address.|`10.1.1.1`|
|dst_ip_addr|server_addr|ip|IP address of the server involved in actually handing out the lease. There could be other servers replying with OFFER messages which won't be represented here. Getting an address in this field also requires that the server handing out the lease also sources packets from a non-broadcast IP address|`10.2.2.2`|
|event_uid|uids|array_string|A series of unique identifiers of the connections over which DHCP is occurring. This behavior with multiple connections is unique to DHCP because of the way it uses broadcast packets on local networks.|````|
|src_domain|domain|string|Domain given by the server in option 15.|`somedomain.local`|
|src_host_name|host_name|string|Name given by client in Hostname option 12.|`somegreat-hostname`|
|dhcp_lease_time|lease_time|float|IP address lease interval.|`6`|
|TBD|agent_remote_id|string|present if policy/protocols/dhcp/sub-opts.bro is loaded A globally unique identifier added by relay agents to identify the remote host end of the circuit."|``|
|dhcp_assigned_ip_addr|assigned_addr|ip|IP address assigned by the DHCP server.|`10.3.3.3`|
|dhcp_circuit_id|circuit_id|string|present if policy/protocols/dhcp/sub-opts.bro is loaded Added by DHCP relay agents which terminate switched or permanent circuits. It encodes an agent-local identifier of the circuit from which a DHCP client-to-server packet was received. Typically it should represent a router or switch interface number."|``|
|TBD|client_message|string|Message typically accompanied with a DHCP_DECLINE so the client can tell the server why it rejected an address.|``|
|TBD|client_software|string|present if policy/protocols/dhcp/software.bro is loaded Software reported by the client in the vendor_class option."|`Cisco Systems, Inc. IP Phone CP-8945`|
|src_fqdn|client_fqdn|string|FQDN given by client in Client FQDN option 81.|`somegreat-hostname.somedomain.local`|
|src_mac|mac|string|Client's hardware address.|`aa:bb:cc:dd:ee:ff`|
|TBD|msg_orig|array_ip|present if policy/protocols/dhcp/msg-orig.bro is loaded The address that originated each message from the msg_types field."|`[ "0.0.0.0", "0.0.0.0", "0.0.0.0", "0.0.0.0", "192.168.254.1", "192.168.254.1", "192.168.254.1", "192.168.254.1"  ]`|
|TBD|msg_types|array_string|The DHCP message types seen by this DHCP transaction|`INFORM`|
|dhcp_requested_ip_addr|requested_addr|ip|IP address requested by the client.|`1.1.1.1`|
|TBD|server_message|string|Message typically accompanied with a DHCP_NAK to let the client know why it rejected the request.|`requested address is incorrect`|
|TBD|server_software|string|present if policy/protocols/dhcp/software.bro is loaded Software reported by the server in the vendor_class option."|`PXEClient`|
|dhcp_subscriber_id|subscriber_id|string|present if policy/protocols/dhcp/sub-opts.bro is loaded The subscriber ID is a value independent of the physical network configuration so that a customer's DHCP configuration can be given to them correctly no matter where they are physically connected."|``|
|event_duration|duration|float|Duration of the DHCP "session" representing the time from the first message to the last.|``|
