# macOS Carbon Black Event Logs

## Description
Carbon Black data schema as defined by the Carbon Black Developer Resources.

## Data model
![Data model](/resources/images/CarbonBlackDataModel.png)

## Sub Data Sets
|events|Version|Description|Tags|
|---|---|---|---|
|[childproc](events/childproc.md)|0|A process has spawned another process on an endpoint monitored by Carbon Black.||
|[filemod](events/filemod.md)|0|A file on the filesystem has been created, deleted, or modified on an endpoint monitored by Carbon Black.||
|[modload](events/modload.md)|0|This event contains the information for modules loaded by processes on endpoints monitored by Carbon Black.||
|[netconn](events/netconn.md)|0|A network connection has been received or initiated by an endpoint monitored by Carbon Black.||
|[proc](events/proc.md)|0|A new process has started (or exited) on an endpoint monitored by Carbon Black.||

## References
* [Carboon Black Event Schema](https://developer.carbonblack.com/reference/enterprise-response/event-forwarder/event-schema/)