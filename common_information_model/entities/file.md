# File Schema
Event fields used to define metadata about files either locally or over the wire.

## Data Fields
|Standard Name|Type|Description|Sample Value|
|---|---|---|---|
| file_accessed_time          | date    | When the file was last accessed . Also known as `atime`       | `2016-11-25 18:21:47`                  |
| file_changed_time           | date    | When the file was last changed. Also known as `ctime`         | `2016-11-25 18:21:47`                  |
| file_company                | string  | Company name a file belongs to                                | `Microsoft Corporation`                |
| file_creation_time          | date    | When the file was created. Also known as `crtime`             | `2016-11-25 18:21:47`                  |
| file_description            | string  | Description of a file                                         | `Console Window Host`                  |
| file_directory              | string  | Directory of file(s). It does not include the file name       | `C:\users\wardog\`                     |
| file_extension              | string  | The file extension of a file (.txt, .exe, etc)                | `exe`                                  |
| file_hard_links             | integer | Number of hard links                                          | `3`                                    |
| file_inode                  | integer | Filesystem inode number                                       |                                        |
| file_link_name              | string  | path of the hard link                                         | `C:\\Docs\\My.exe`                     |
| file_mime_type              | string  | Specifies the MIME type name specified for a file             | `application/msword`                   |
| file_modified_time          | date    | When the file was last modified. Also known as `mtime`        | `2016-11-25 18:21:47`                  |
| file_name                   | string  | name of a file without its full path                          | `a.exe`                                |
| file_path                   | string  | full path of a file including the name of the file            | `C:\users\wardog\z.exe`                |
| file_previous_accessed_time | string  | When the file was previously accessed                         | `2016-11-25 18:21:47`                  |
| file_previous_changed_time  | string  | When the file was previously changed                          | `2016-11-25 18:21:47`                  |
| file_previous_creation_time | string  | When the file was previously created                          | `2016-11-25 18:21:47`                  |
| file_previous_modified_time | string  | When the file was previously modified                         | `2016-11-25 18:21:47`                  |
| file_previous_name          | string  | The file's previous name                                      | `C:\\Windows\system32\cmd.exe`         |
| file_product                | string  | The file's product name                                       | `Microsoft® Windows® Operating System` |
| file_size                   | string  | Specifies the size of a file, in bytes                        | `45`                                   |
| file_symlink                | integer | 1 if the path is a symlink, otherwise 0                       | `0`                                    |
| file_symlink_name           | string  | path of the symlink                                           | `C:\\Docs\\My.exe`                     |
| file_system_block_size      | integer | Block size of filesystem                                      |                                        |
| file_system_type            | string  | The file system type, ex:  fat32, ntfs, vmfs, ext3, ext4, xfs | `ntfs`                                 |
| file_version                | string  | Version of the image loaded                                   | `10.0.16299.15 (WinBuild.160101.0800)` |
