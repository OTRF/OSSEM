# Entity Structure

Entities are documented in `YAML` format, and are the source files for every entity documentation in the common data model. These source files can be used to define the logic behind each entity and automate the creation of field names and documentation.

**Example:**

```yaml
name: hash
prefix:
- hash
id: 42C1A34E-D474-468D-8EFB-09454CA8BFC2
description: Event fields used to capture metadata about hashes of an image/binary/file.
extends_entities:
- process
- file
attributes:
- name: md5
  type: string
  description: MD5 hash of the image/binary/file
  sample_value: 6A255BEBF3DBCD13585538ED47DBAFD7
- name: sha1
  type: string
  description: SHA1 hash of the image/binary/file
  sample_value: B0BF5AC2E81BBF597FAD5F349FEEB32CAC449FA2
- name: sha256
  type: string
  description: SHA256 hash of the image/binary/file
  sample_value: 4668BB2223FFB983A5F1273B9E3D9FA2C5CE4A0F1FB18CA5C1B285762020073C
references: []
tags: []
```

## Entity Definitions

```yaml
name: hash
prefix:
- hash
id: 42C1A34E-D474-468D-8EFB-09454CA8BFC2
description: Event fields used to capture metadata about hashes of an image/binary/file.
```
* **name:** Name of the current entity.
  * Name must be lower case
  * Multiple words in an entity name must be separated by an underscore (i.e `user_agent`)

* **prefix:** Prefix used for every attribute defined under the current entity.
  * `hash`_md5
  * `hash`_sha1
  * `hash`_sha256
  
  You can specify more than one prefix. This is the case for entities that might have attributes that can be defined twice under the same entity. This is different from extending other entities since the additional prefix only makes sense to the current entity (i.e `process` and `process_parent`).
  * `process`_name
  * `process`_path
  * `process_parent`_name
  * `process_parent`_path

* **id:** Unique identifier for the current entity (i.e `035E058E-5405-4B3B-9288-E78A63B40DAA`)
    * You can generate an ID value by running the following command `uuidgen` in macOS.

* **description:** Description of the current entity.

## Entity Extensions

```yaml
extends_entities:
- process
- file
```

* An entity can extend another entity.
* This is the case of entities such as `Hash` extending other entities such as `Process` and `File`.
    * As we know, telemetry from processes could also provide `hash` information of the file backing up the process (i.e an executable).
    * Therefore, we can say that the `Hash` entity and its atrributes (i.e. md5,sha1,sha256) could extend the `Process` entity.
* We can describe this logic by leveraging the **`extends_entities`** property of the current entity.
    * It only accepts a `list` of entity names.
* By default, in the example above, the `Hash` entity extended the `Process` entity by appending all possible field names from the `Hash` entity to the `Process` prefix values. Since `Process` has two prefixes, we end up with something similar to:
    * `process_hash_md5`
    * `process_hash_sha256`
    * `process_parent_hash_md5`
    * `process_parent_hash_sha256`
* This does not apply to every attributes in the extended entity (i.e `process_id`, `process_command_line`, `process_integrity`, etc). We can only extend the entity **prefix** values to create the entity field names. The following would not make sense:
    * `process_id_hash_md5`
    * `process_command_line_hash_256`

## Entity Attributes

```yaml
attributes:
- name: md5
  type: string
  description: MD5 hash of the image/binary/file
  sample_value: 6A255BEBF3DBCD13585538ED47DBAFD7
- name: sha1
  type: string
  description: SHA1 hash of the image/binary/file
  sample_value: B0BF5AC2E81BBF597FAD5F349FEEB32CAC449FA2
- name: sha256
  type: string
  description: SHA256 hash of the image/binary/file
  sample_value: 4668BB2223FFB983A5F1273B9E3D9FA2C5CE4A0F1FB18CA5C1B285762020073C
```

* Entity attributes are provided under the **attributes** property of the current entity.
* The **attributes** property is a list of dictionaries.
* Each dictionary provides metadata about each attribute
    * **name:** Name of the attribute
    * **type:** Data type of the attribute
    * **description:** Description of the attribute
    * **sample_value:** An example of the expected attribute value
* Attribute names must be lower case
* Multiple words in an attribute must be separated by an underscore (i.e. record_id)
* Descriptions must be generic enough to cover entities extensions (extending other entities and itself)
    * For example, the description of the attribute `name` in a `Process` entity should fit `process_name`, `process_parent_name`, `source_process_name`
    * we can simply describe the attribute `name` in a `Process` entity as the `name of the application backing up the process in a system. Name without full path of the file or executable backing up the process. It can be leveraged in the context of child, parent, source and even target process`