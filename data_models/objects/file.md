# File Object

## Data Fields

| field name | field type | description |
|--------|---------|-------|
| file_name | string | name of file without the full path |
| file_path | string | full path of the file including the name of the file |
| file_extension | string | The file extension of a file (.txt, .exe, etc) |
| file_mime_type | string | Specifies the MIME type name specified for the file. For example, application/msword |
| file_size | string | Specifies the size of the file, in bytes |
| file_version | string | Version of the image loaded |
| file_description | string | Description of the file |
| file_product | string | The file product name |
| file_company | string | Company name the file belongs to |
| date_creation | date | Specifies the date/time the file was created |
| date_modified | date | Specifies the date/time the file was last written to/modified |
| date_accessed | date | Specifies the date/time the file was last accessed |
| process_name | string | The name of the process that created/modified/deleted the file |
| process_path | string | The complete path and name of the process that created/modified/deleted the file |
| process_id | integer | Process ID of the process that created/modified/deleted the file |
| user_name | string | The name of the user that created/modified/deleted the file |
| user_domain | string | The name of the domain the user that that created/modified/deleted the file belongs to |
| user_logon_id | integer | Logon ID of the user that that created/modified/deleted the file in the event |
| hash_md5 | string | MD5 hash of the file |
| hash_sha1 | string | SHA1 hash of the file |
| hash_sha256 | string | SHA256 hash of the file |
| hash_imphash | string | IMPHASH hash of the file |
| host_name | string | Name of the endpoint where the file exists. Usually without the FQDN |
| host_fqdn | string | The fully qualified domain name of the host where file exists |