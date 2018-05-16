# Common Information Model

The common information model facilitates the normalization of data sets by providing a standard way to parse security event logs. It is organized by specific entities associated with event logs defined by [data dictionaries](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries)

## Entities Defined

| Entity | Description |
|--------|---------|
| [destination](https://github.com/Cyb3rWard0g/OSSEM/blob/master/common_information_model/destination.md) | Event fields used to define the destination in a network connection event. |
| [event](https://github.com/Cyb3rWard0g/OSSEM/blob/master/common_information_model/event.md) | Event fields used to define specific metadata of the event itself. For example, event_id or event_creation_time. |
| [file](https://github.com/Cyb3rWard0g/OSSEM/blob/master/common_information_model/file.md) | Event fields used to define metadata about files either locally or over the wire.|
| [group](https://github.com/Cyb3rWard0g/OSSEM/blob/master/common_information_model/group.md) | Event fields used to define metadata about a security group, or distribution group that is created changed or deleted. |
| [hash](https://github.com/Cyb3rWard0g/OSSEM/blob/master/common_information_model/hash.md) | Event fields used to define metadata about hashes. |
| [host](https://github.com/Cyb3rWard0g/OSSEM/blob/master/common_information_model/host.md) | Event fields used to define metadata about hosts where events are originally created. |
| [ip](https://github.com/Cyb3rWard0g/OSSEM/blob/master/common_information_model/ip.md) | Event fields used to define metadata about IP addresses in a network. It follows the standard from the Destination and Source categories. |
| [module](https://github.com/Cyb3rWard0g/OSSEM/blob/master/common_information_model/module.md) | Event fields used to define metadata about modules in an endpoint. |
| [pipe](https://github.com/Cyb3rWard0g/OSSEM/blob/master/common_information_model/pipe.md) | Event fields used to define metadata about pipes being created or connected in an endpoint. |
| [port](https://github.com/Cyb3rWard0g/OSSEM/blob/master/common_information_model/port.md) | Event fields used to define metadata about ports in a network connection. |
| [process](https://github.com/Cyb3rWard0g/OSSEM/blob/master/common_information_model/process.md)| Event fields used to define metadata about processes in an system. |
| [registry](https://github.com/Cyb3rWard0g/OSSEM/blob/master/common_information_model/registry.md) | Event fields used to define metadata about registry entries in a system. |
| [source](https://github.com/Cyb3rWard0g/OSSEM/blob/master/common_information_model/source.md) | Event fields used to define the source in a network connection event. |
| [target](https://github.com/Cyb3rWard0g/OSSEM/blob/master/common_information_model/target.md) | Event fields used to define entities being targeted by other entities locally in a system. This is different from a network connection event. It is more related to events that involve relationships defined locally by entities such as files, processes,users, etc. |
| [user](https://github.com/Cyb3rWard0g/OSSEM/blob/master/common_information_model/user.md) | Event fields used to define metadata about users in an network environment. |