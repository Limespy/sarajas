# Æther database

- [Æther database](#æther-database)
  - [Fundamentals](#fundamentals)
    - [Aim](#aim)
    - [Meditations](#meditations)
    - [Philosophies](#philosophies)
      - [Logic separate from implementation](#logic-separate-from-implementation)
      - [Maximum freedom](#maximum-freedom)
      - [Version control](#version-control)
      - [](#)
    - [Doctrines](#doctrines)
      - [Everything is item](#everything-is-item)
  - [Design](#design)
    - [Security](#security)
    - [Item files](#item-files)
    - [Version control](#version-control-1)
    - [Indexes](#indexes)
  - [Implementation](#implementation)
    - [Item storage](#item-storage)
    - [Program language](#program-language)
    - [Booting](#booting)
    - [Version control](#version-control-2)

## Meta

## Fundamentals

### Aim

To get a database/API hybrid to allow management of arbitrary systems.

### Meditations

Flexibility is paramount



### Philosophies

#### Logic separate from implementation

This system should be implementable in many different ways

#### Maximum freedom

Similar to avoiding premature optimization.
Only implicit limitations due to the inherent features of the system are allowed.
Even self harm and logical paradoxes are allowed leaving user to set the guidelines for themselves.

#### Version control

Full version history and control

#### 

### Doctrines

#### Everything is item

All things are items in the database, including the source code.
This means the source code allows modification of itself. 
Please be careful. 
## Design

The database should be considered an indexing system for arbitrary number of multiple different systems. The data can be fully stored in the database item or exist outside with database item functioning as metadata, linking and API layer to the actual data. 



### Security

There will be both item and key level access permissions.

### Item files



### Version control

All information is stored. The DB shall be full record of all of it's states since its creation.

### Indexes

Indeces, like all other things here, are items in the database.

Index contains additionally

- Reference to sorting condition
- Descrition

| item id | value type | value | 


Whenever item is added or removed from the database, it goes through the indexing conditions, which decide to which index tables to add it.


## Implementation

### Item storage

File extension will be aedb.

YAML will be the file markup language.
This makes AEDB file markup subset of YAML.

### Program language

Python

### Booting

There is \_\_init__.py to bootstrap the DB

```
python "database folder name"
```

### Version control

Version control provided by Git

There shall be git wrapper through python 
