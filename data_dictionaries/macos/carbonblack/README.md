# macOS Carbon Black Event Logs

## Description
Carbon Black data schema as defined by the Carbon Black Developer Resources.

## Data model
![Data model](/resources/images/CarbonBlackDataModel.png)

## Sub Data Sets
|events|Description|Tags|
|---|---|---|
|[childproc](events/childproc.md)|A process has spawned another process on an endpoint monitored by Carbon Black.||
|[filemod](events/filemod.md)|A file on the filesystem has been created, deleted, or modified on an endpoint monitored by Carbon Black.||
|[modload](events/modload.md)|This event contains the information for modules loaded by processes on endpoints monitored by Carbon Black.||
|[netconn](events/netconn.md)|A network connection has been received or initiated by an endpoint monitored by Carbon Black.||
|[proc](events/proc.md)|A new process has started (or exited) on an endpoint monitored by Carbon Black.||

## References
* [Carboon Black Event Schema](https://developer.carbonblack.com/reference/enterprise-response/event-forwarder/event-schema/)