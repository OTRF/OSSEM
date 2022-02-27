# Source or Destination or Target

Several events that the OSSEM CDM project describes have a sense of direction.
Usually in a network connection, this sense of direction is represented by `source` and `destination` to describe the `origin` of the connection and where the network packets are `sent to`.
This concept of direction is not only represented in a `network connection`, but also other events such as `creation of a process` where an entity interacts with another entity.
Therefore, the OSEEM project is also using the concept of `target` instead of `destination` when describing an interaction between entities that are not part of a network connection. 

## Source and Destination Example

When the metadata of the event describes a network connection and the same entity type is used:

* `source.ip` -> `connected_to` -> `destination.ip`
* `source.host` -> `connected_to` -> `destination.host`

## Source and Target Example

When the metadata of the event does `not` describe a network connection and the same entity type is used:

* `source.process` -> `created` -> `target.process`
* `source.process` -> `accessed` -> `target.process`

## The use of Aliases

When the metadata of the event does not use the same entity type, we can use `aliases` for both entities and query them without `source`, `destination` and `target` annotations.
This also works when the event provides metadata of only one entity which could be the `source`, `destination` or `target`.

### Before
`source.process`

* `source.process` -> `created` -> `target.file`
* `source.host` -> `connected_to` -> `target.ip`

### After
`process`

* `process` -> `created` -> `file`
* `host` -> `connected_to` -> `ip`

