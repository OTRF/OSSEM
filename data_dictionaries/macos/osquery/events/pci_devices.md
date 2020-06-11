# Pci_devices Table

## Description
PCI devices active on the host system.

## Data Dictionary
|Standard Name|Field Name|Type|Description|Sample Value|
|---|---|---|---|---|
|TBD|pci_slot|TEXT|PCI Device used slot|`TBD`|
|TBD|pci_class|TEXT|PCI Device class|`TBD`|
|TBD|driver|TEXT|PCI Device used driver|`TBD`|
|TBD|vendor|TEXT|PCI Device vendor|`TBD`|
|TBD|vendor_id|TEXT|Hex encoded PCI Device vendor identifier|`TBD`|
|TBD|model|TEXT|PCI Device model|`TBD`|
|TBD|model_id|TEXT|Hex encoded PCI Device model identifier|`TBD`|
|TBD|subsystem|TEXT|PCI Device subsystem|`TBD`|
|TBD|express|INTEGER|1 If PCI device is express else 0|`TBD`|
|TBD|thunderbolt|INTEGER|1 If PCI device is thunderbolt else 0|`TBD`|
|TBD|removable|INTEGER|1 If PCI device is removable else 0|`TBD`|
|TBD|pci_class_id|TEXT|PCI Device class ID in hex format [LINUX]|`TBD`|
|TBD|pci_subclass_id|TEXT|PCI Device  subclass in hex format [LINUX]|`TBD`|
|TBD|pci_subclass|TEXT|PCI Device subclass [LINUX]|`TBD`|
|TBD|subsystem_vendor_id|TEXT|Vendor ID of PCI device subsystem [LINUX]|`TBD`|
|TBD|subsystem_vendor|TEXT|Vendor of PCI device subsystem [LINUX]|`TBD`|
|TBD|subsystem_model_id|TEXT|Model ID of PCI device subsystem [LINUX]|`TBD`|
|TBD|subsystem_model|TEXT|Device description of PCI device subsystem [LINUX]|`TBD`|

## References
* [OSQuery table documentation](https://osquery.io/schema/current#pci_devices)

## Tags
* version_4.4.2