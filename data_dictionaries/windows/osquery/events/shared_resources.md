# Shared_resources Table
###### Version: 4.4.2

## Description
Displays shared resources on a computer system running Windows. This may be a disk drive, printer, interprocess communication, or other sharable device.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|description|TEXT|A textual description of the object|`TBD`|
|TBD|install_date|TEXT|Indicates when the object was installed. Lack of a value does not indicate that the object is not installed.|`TBD`|
|TBD|status|TEXT|String that indicates the current status of the object.|`TBD`|
|TBD|allow_maximum|INTEGER|Number of concurrent users for this resource has been limited. If True, the value in the MaximumAllowed property is ignored.|`TBD`|
|TBD|maximum_allowed|INTEGER|Limit on the maximum number of users allowed to use this resource concurrently. The value is only valid if the AllowMaximum property is set to FALSE.|`TBD`|
|TBD|name|TEXT|Alias given to a path set up as a share on a computer system running Windows.|`TBD`|
|TBD|path|TEXT|Local path of the Windows share.|`TBD`|
|TBD|type|INTEGER|Type of resource being shared. Types include: disk drives, print queues, interprocess communications (IPC), and general devices.|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#shared_resources)
