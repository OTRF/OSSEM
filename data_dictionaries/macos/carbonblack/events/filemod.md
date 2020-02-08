# ingress.event.filemod (File Modification)

## Description
A file on the filesystem has been created, deleted, or modified on an endpoint monitored by Carbon Black.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|action|action|TEXT|Type of file modification: create, write, delete, lastwrite|`create`|
|actiontype|actiontype|INTEGER|Enum value of the file modification: 1=create, 2=write, 4=delete, 8=lastwrite|`1`|
|cb_server|cb_server|TEXT|Used to distinguish between multiple Cb Response servers. Set this in the "server_name" option of cb-event-forwarder.ini.|`cbserver`|
|host_name|computer_name|TEXT|hostname of the sensor|`JASON-MAC-VM`|
|event_type|event_type|TEXT|The type of event|`filemod`|
|filetype|filetype|INTEGER|Enum value of the detected file type of this file. Only valid for "lastwrite" actions. See the CbFileType protobuf definition for the available values.|`0`|
|filetype_name|filetype_name|TEXT|The detected file type of this file. Only valid for "lastwrite" actions. Currently supported file types: PE, ELF, UniversalBin, Eicar, OfficeLegacy, OfficeOpenXml, PDF, PKZIP, LZH, LZW, RAR, TAR, and 7zip.|`Unknown`|
|process_link|link_process|TEXT|Deep link to Cb Response UI for process|`https://cbtests/#analyze/00000001-0000-0c70-01d1-1e951aae7e2f/1`|
|sensor_link|link_sensor|TEXT|Deep link to Cb Response UI for sensor|`https://cbtests/#/host/1`|
|hash|md5|TEXT|md5 of process executable|`7A2870C2A8283B3630BF7670D0362B94`|
|file_path|path|TEXT|Full file path|`/opt/test/test.sh`|
|process_id|pid|INTEGER|Endpoint OS Process id of process|`3184`|
|process_guid|process_guid|TEXT|Cb Process GUID of process|`00000001-0000-0c70-01d1-1e951aae7e2f`|
|sensor_id|sensor_id|INTEGER|sensor ID of associated sensor|`1`|
|event_date_creation|timestamp|INTEGER|Endpoint timestamp of this event since epoch|`1447696804`|
|event_type_detailed|type|TEXT|The full type of event|`ingress.event.filemod`|

## Resources
* [Carbon Black Developer Docs](https://developer.carbonblack.com/reference/enterprise-response/event-forwarder/event-schema/#ingress-event-filemod-file-modification)
