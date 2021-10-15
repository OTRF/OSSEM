# registry

Event fields used to define metadata about Windows registry entries in a system. The registry is a hierarchical database that contains data that is critical for the operation of Windows and the applications and services that run on Windows. The data is structured in a tree format. Each node in the tree is called a key. Each key can contain both subkeys and data entries called values. Sometimes, the presence of a key is all the data that an application requires; other times, an application opens a key and uses the values associated with the key. A key can have any number of values, and the values can be in any form.

## Attributes

| Name | Type | Description | Sample Value |
|:---|:---|:---|:---|
 | registry_hive_path | string | A hive is a logical group of keys, subkeys, and values in the registry that has a set of supporting files loaded into memory when the operating system is started or a user logs in. | ```HKEY_LOCAL_MACHINE\SAM``` |
 | registry_key_access_rights | string | The Windows security model enables you to control access to registry keys. The valid access rights for registry keys include the DELETE, READ_CONTROL, WRITE_DAC, and WRITE_OWNER standard access rights. Registry keys do not support the SYNCHRONIZE standard access right. | ```KEY_ALL_ACCESS (0xF003F)``` |
 | registry_key_name | string | This field contains the key name without the full path. Take in consideration the name of the key value in the registry key path. | ```Run``` |
 | registry_key_name_modified | string | Original registry key name before being modified. | ```Run``` |
 | registry_key_path | string | Next-level down from registry root-keys. This field contains the full path of a registry key. This is a combination of the root key, hive, key, sub-key, and value. A key is a folder in the registry that contain other sub-keys. | ```HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\WardogPersistence``` |
 | registry_key_path_modified | string | Original registry key path before being modified. | ```HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\WardogPersistence``` |
 | registry_root_key | string | Root-Keys are the root, or primary divisions, of the registry. They do not contain configuration data; they contain the keys, subkeys, and values in which the data is stored. There are six root keys (HKCU, HKU, HKCR, HKLM, HKCC and HKPD) that store information related to currently looged on users, local accounts, performance, and even the current hardware profile. Root-key names represent Windows handles (H) to Keys (K). | ```HKLM or HKEY_LOCAL_MAHINE``` |
 | registry_value_data | string | Each registry key value consists of a value name and its associated data. Registry key value data store the actual configuration data for the operating system and the programs that run on the system. As such, they are different from subtrees, keys, and subkeys, which are merely containers. | ```C:\Path\malware``` |
 | registry_value_data_modified | string | Original registry key value data before being modified. | ```C:\malware.exe``` |
 | registry_value_name | string | Registry values are the lowest-level element in the registry. They appear in the right pane of the registry editor window. Each entry consists of the value name, its Data Types in the Registry (which defines the length and format of data that the entry can store), and a field known as the data of the registry value. These are also known as registry entries. This field contains the key value name without the full registry key path. | ```WardogPersistence``` |
 | registry_value_name_modified | string | Original registry key vakue name before being modified. | ```WardogPersistence``` |
 | registry_value_type | string | values store different kinds of data such as REG_NONE (No value type), REG_SZ (Fixed-length Unicode string), REG_EXPAND_SZ (Variable-length Unicode string that can have embedded environment variables), etc. | ```REG_EXPAND_SZ``` |
 | registry_value_type_modified | string | Original registry key vakue type before being modified. | ```REG_EXPAND_SZ``` |
