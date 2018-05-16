# File Schema

Event fields used to define metadata about files either locally or over the wire.

## Data Fields

| Field name | Type | Description | Sample Value |
|--------|---------|-------|-------|
| file_name | string | name of a file without its full path | a.exe |
| file_path | string | full path of a file including the name of the file | C:\users\wardog\z.exe |
| file_extension | string | The file extension of a file (.txt, .exe, etc) | zip |
| file_mime_type | string | Specifies the MIME type name specified for a file | application/msword |
| file_size | string | Specifies the size of a file, in bytes | 45 |
| file_version | string | Version of the image loaded | 10.0.16299.15 (WinBuild.160101.0800) |
| file_description | string | Description of a file | Console Window Host |
| file_product | string | The file's product name | Microsoft® Windows® Operating System |
| file_company | string | Company name a file belongs to | Microsoft Corporation |