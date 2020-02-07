# Windows Carbon Black Event Logs

## Description
Carbon Black data schema as defined by the Carbon Black Developer Resources.

## Data model
![Data model](/resources/images/CarbonBlackDataModel.png)

## Sub Data Sets
|events|Description|Tags|
|---|---|---|
|[childproc](events/childproc.md)|A process has spawned another process on an endpoint monitored by Carbon Black.||
|[cross_process](events/cross_process.md)|A process has attempted to open a handle into another process OR if a remote thread was created.||
|[emetmitigation](events/emetmitigation.md)|Microsoft EMET has killed a process on an endpoint monitored by Carbon Black.||
|[filemod](events/filemod.md)|A file on the filesystem has been created, deleted, or modified on an endpoint monitored by Carbon Black.||
|[modload](events/modload.md)|This event contains the information for modules loaded by processes on endpoints monitored by Carbon Black.||
|[netconn](events/netconn.md)|A network connection has been received or initiated by an endpoint monitored by Carbon Black.||
|[proc](events/proc.md)|A new process has started (or exited) on an endpoint monitored by Carbon Black.||
|[processblock](events/processblock.md)|A process was blocked from executing on an endpoint monitored by Carbon Black because the process MD5 has been blacklisted.||
|[regmod](events/regmod.md)|A registry key has been created, deleted, or modified on an endpoint monitored by Carbon Black.||
|[tamper](events/tamper.md)|A process tampered with a critical Carbon Black userspace process or kernel driver.||

## Resources
* [Carboon Black Event Schema](https://developer.carbonblack.com/reference/enterprise-response/event-forwarder/event-schema/)