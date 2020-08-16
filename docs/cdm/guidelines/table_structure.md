# Table Structure

Tables are documented in `YAML` format, and are the source files for every table documentationin the common data model. These source files can be used to define the logic behind each table and automate the creation of field names and documentation. Tables are objects that group several entities together creating relationships among them to standardize diverse datasets that share a common definition. For example, the `NetworkSession` table leverages entities such as `http`, `url`, `network`, etc.

**Example:**

```yaml
name: NetworkSession
id: 189BC2EE-44BF-4A8A-A257-5521C67D457B
description: Event fields used to define network sessions in an endpoint.
entities:
- hash
- user
- name: file
  prefix:
  - file
  attributes:
  - name
  - path
- name: custom
  entities:
  - name: threat
    attributes:
    - name: name
      type: string
      description: The name of the threat or malware identified
      sample_value: 'Win32.Small.ahif(90603579)'
```
## Table Definitions

```yaml
name: network_session
id: 189BC2EE-44BF-4A8A-A257-5521C67D457B
description: Event fields used to define network sessions in an endpoint.
```
* **name:** Name of the current table.
  * Name must be lower case
  * Multiple words in an entity name must be separated by an underscore (i.e `user_agent`)

* **id:** Unique identifier for the current entity (i.e `035E058E-5405-4B3B-9288-E78A63B40DAA`)
    * You can generate an ID value by running the following command `uuidgen` in macOS.

* **description:** Description of the current table.

## Entities

```yaml
entities:
- hash
- user
- name: file
  prefix:
  - file
  attributes:
  - name
  - path
- name: custom
  entities:
  - name: threat
    prefix:
    - threat
    attributes:
    - name: name
      type: string
      description: The name of the threat or malware identified
      sample_value: 'Win32.Small.ahif(90603579)'
```

* As mentioned before, we can define tables by grouping more than one pre-defined entity.
* Entities that form a table are added under the `entities` property.
* The `entities` property expects a list of `strings` or `dictionaries`
  * `Strings` are used to directly call an entity and all its attributes.
    * They must be lower case (Following the same guidelines defined in the `Entity Structure` documentation)
  * `Dictionaries` can be used for two things:

* You can use a dictionary to define what specific attributes you want from existing entities.

```yaml
- name: file
  prefix:
  - file
  attributes:
  - name
  - path
```
* We define the name of the entity and the valid prefix for the entity.
  * We define the entity to be flexible and be able to be very specific when pulling field names (prefix + attribute) from our already defined entities.
  * All we do next is just take the `prefix`, append it to the `attribute` and compare it with attributes in our official entities list. If we find a match then we add it to the table.
* A table would end up with the following attributes from the `file` entity
  * `file_name`
  * `file_path`

* You can also use a dictionary to introduce custom entities with custom attributes that do not exist currently in the common data model. This is good for collaboration purposes.

* `Custom` dictionaries contain a list of dictionaries.
  * Each dictionary is a custom/new entity
    * Each entity name follows the same guidelines defined in the `Entity Structure` documentation.
    * Each entity has a `prefix` property (same to the entity concepts in this common data model)
  * Each dictionary/entity has an `attributes` property that allows users to introduce new attributes to the common data model
    * Each attribute contains the usual properties (`name`, `type`, `description`, `sample_value`)
    * Each attribute name follows the same guidelines defined in the `Entity Structure` documentation.