# Pipes Table
###### Version: 4.4.2

## Description
Named and Anonymous pipes.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|process_id|pid|BIGINT|Process ID of the process to which the pipe belongs|`TBD`|
|pipe_name|name|TEXT|Name of the pipe|`TBD`|
|pipe_instances|instances|INTEGER|Number of instances of the named pipe|`TBD`|
|pipe_max_instances|max_instances|INTEGER|The maximum number of instances creatable for this pipe|`TBD`|
|pipe_flags|flags|TEXT|The flags indicating whether this pipe connection is a server or client end, and if the pipe for sending messages or bytes|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#pipes)
