# Host Object Relationships
None

## Data Fields

|ATT&CK Data Source|Sub Data Source|Source Data Object|Relationship|Destination Data Object|EventID|
|---|---|---|---|---|---|
|Windows event logs, Authentication logs|NTLM Credentials Validation|host|authenticated|user|4776|
|Process use of network|process network service connection block|host|blocked_service_connection_to|process|5031|
|Process use of network|process network listener allow|host|permitted_listener_on|process|5154|
|Process use of network|process network listener block|host|blocked_listener_on|process|5155|
|Process use of network|process network connection allow|host|permitted_inbound_connection_on|process|5156|
|Process use of network|process network connection allow|host|permitted_outbound_connection_on|process|5156|
|Process use of network|process network connection block|host|blocked_inbound_connection_on|process|5157|
|Process use of network|process network connection block|host|blocked_outbound_connection_on|process|5157|
|Process use of network|process network local port bind allow|host|permitted_local_port_bind_on|process|5158|
|Process use of network|process network local port bind blocked|host|blocked_local_port_bind_on|process|5159|



