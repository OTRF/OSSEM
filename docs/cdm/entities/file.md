# file

Event fields used to define/normalize metadata about files either locally or over the wire (Network Traffic). This entity and attributes can extend other entities such as source and destination.

## Attributes

| Name | Type | Description | Sample Value |
|:---|:---|:---|:---|
 | file_accessed_time | date | When the file was last accessed . Also known as `atime` | ```2016-11-25 18:21:47``` |
 | file_changed_time | date | When the file was last changed. Also known as `ctime` | ```2016-11-25 18:21:47``` |
 | file_company | string | Company name a file belongs to | ```Microsoft Corporation``` |
 | file_creation_time | date | When the file was created. Also known as `crtime` | ```2016-11-25 18:21:47``` |
 | file_description | string | Description of a file | ```Console Window Host``` |
 | file_directory | string | Directory of file(s). It does not include the file name | ```C:\users\wardog\``` |
 | file_extension | string | The extension name or type of the file. | ```exe``` |
 | file_hard_links | integer | Number of hard links | ```3``` |
 | file_hash_imphash | string | IMPHASH hash of the image/binary/file | ```2505BD03D7BD285E50CE89CEC02B333B``` |
 | file_hash_md5 | string | MD5 hash of the image/binary/file | ```6A255BEBF3DBCD13585538ED47DBAFD7``` |
 | file_hash_sha1 | string | SHA1 hash of the image/binary/file | ```B0BF5AC2E81BBF597FAD5F349FEEB32CAC449FA2``` |
 | file_hash_sha256 | string | SHA256 hash of the image/binary/file | ```4668BB2223FFB983A5F1273B9E3D9FA2C5CE4A0F1FB18CA5C1B285762020073C``` |
 | file_hash_sha512 | string | SHA512 hash of the image/binary/file | ```1AD1D79F85D8F6A50EA282F63898D652661DAA0C1FD361C22647CABC98A70E8CBCE83200D579D10DD0A3D46BE9496DCDFDDF28B0C5E9709343B032A8796FBECB``` |
 | file_inode | integer | Filesystem inode number | `````` |
 | file_link_name | string | path of the hard link | ```C:\Docs\My.exe``` |
 | file_mime_type | string | MIME type name specified for the file | ```application/msword``` |
 | file_modified_time | date | When the file was last modified. Also known as `mtime` | ```2016-11-25 18:21:47``` |
 | file_name | string | name of the file without its full path. This could be a local file or one transmitted over the network. | ```a.exe``` |
 | file_path | string | full path of a file including the name of the file. This could be a local file or one transmitted over the network. | ```C:\users\wardog\z.exe``` |
 | file_previous_accessed_time | date | When the file was previously accessed | ```2016-11-25 18:21:47``` |
 | file_previous_changed_time | date | When the file was previously changed | ```2016-11-25 18:21:47``` |
 | file_previous_creation_time | date | When the file was previously created | ```2016-11-25 18:21:47``` |
 | file_previous_modified_time | date | When the file was previously modified | ```2016-11-25 18:21:47``` |
 | file_previous_name | string | The file's previous name | ```cmd.exe``` |
 | file_previous_path | string | The file's previous path | ```C:\\Windows\system32\cmd.exe``` |
 | file_product | string | The file's product name | ```Microsoft® Windows® Operating System``` |
 | file_size | integer | Size of the file, in bytes. | ```45``` |
 | file_symlink | integer | 1 if the path is a symlink, otherwise 0 | ```0``` |
 | file_symlink_name | string | path of the symlink | ```C:\Docs\My.exe``` |
 | file_system_block_size | integer | Block size of filesystem | `````` |
 | file_system_type | string | The file system type, ex:  fat32, ntfs, vmfs, ext3, ext4, xfs | ```ntfs``` |
 | file_version | string | file version. i.e. image loaded version | ```10.0.16299.15 (WinBuild.160101.0800)``` |
