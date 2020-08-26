# pipe

Event fields used to define metadata about pipes being created or connected in an endpoint.

## Attributes

| Name | Type | Description | Sample Value |
|:---|:---|:---|:---|
 | pipe_flags | string | The flags indicating whether this pipe connection is a server or client end, and if the pipe for sending messages or bytes | `````` |
 | pipe_instances | integer | Number of instances of the named pipe | `````` |
 | pipe_max_instances | integer | The maximum number of instances creatable for this pipe | `````` |
 | pipe_name | string | name of pipe created or connected | ```\srvsvc``` |
