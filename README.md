# Æther database

- [Æther database](#æther-database)
  - [Fundamentals](#fundamentals)
    - [Aim](#aim)
    - [Meditations](#meditations)
      - [Interesting things to do](#interesting-things-to-do)
    - [Philosophies](#philosophies)
      - [Everything is data](#everything-is-data)
      - [Logic separate from implementation](#logic-separate-from-implementation)
      - [Maximum freedom](#maximum-freedom)
      - [Version control](#version-control)
      - [Emergence](#emergence)
    - [Doctrines](#doctrines)
      - [Everything is item](#everything-is-item)
      - [No preliminary limitations](#no-preliminary-limitations)
  - [Design](#design)
    - [Core functions](#core-functions)
    - [Security](#security)
    - [Item files](#item-files)
      - [Data typing](#data-typing)
      - [Version control](#version-control-1)
      - [Indexes](#indexes)
    - [Interactions](#interactions)
  - [Implementation](#implementation)
    - [Boot](#boot)
    - [Item storage](#item-storage)
      - [Data](#data)
      - [Types](#types)
    - [Program language](#program-language)
    - [Booting](#booting)
    - [Version control](#version-control-2)

## Meta

## Fundamentals

### Aim

1. To get a database/API hybrid to allow management and connections between arbitrary systems.
2. Learn metaprogramming with python

### Meditations

Flexibility is paramount.

The system should be transparent.

Complexity from simple rules.

Let's see how far I can take this insanity.



#### Interesting things to do

- More than one way to execute programs within database?
- Database able to move itself?
- Database to be able to launch itself?
- Multiple concurrent instances of the database running concurrently?

### Philosophies
#### Everything is data

Programs are stored data as well

#### Logic separate from implementation

This system should be implementable in many different ways

#### Maximum freedom

Similar to avoiding premature optimization.
Only implicit limitations due to the inherent features of the system are allowed.
Even self harm and logical paradoxes are allowed leaving user to set the guidelines for themselves.

#### Version control

Full version history and control

#### Emergence

Complexity will not be created from complex ruleset, but through interactions of large number of small items.

### Doctrines

#### Everything is item

All things are items in the database, including the source code.
This means the source code allows modification of itself. 
Please be careful. 

#### No preliminary limitations

If in doubt, take the more generalized approach.

## Design

The database should be considered an indexing system for arbitrary number of multiple different systems.
The data can be fully stored in the database item or exist outside with database item functioning as metadata, linking and API layer to the actual data. 

### Core functions

The system needs to be able to:
1. Load files
2. Boot to prepared boot file
3. Take and execute text input
4. Generate files
5. Load file by reference
6. Execute files
### Security

There will be both item and key level access permissions.

### Item files

Item files are core of the system.

Items consist of nested dublets
(key, (type, value))


To keep item files simple, more complex structures are created using referencing to other files.

#### Data typing

Data is typed.
The typing defines how the data is accessed.


#### Version control

All information is stored. The DB shall be full record of all of it's states since its creation.

#### Indexes

Indeces, like all other things here, are items in the database.

Index contains additionally

- Reference to sorting condition
- Descrition

| item id | value type | value | 


Whenever item is added or removed from the database, it goes through the indexing conditions, which decide to which index tables to add it.

### Interactions

There are two things:
1. Items
2. Actions

Actions change items.
Taking inspiration from OOD of Python, actions are responsible for the sematics and items are responsible for the implementation. 
I.e. the action does not need to know the type of the item being acted upon.
Item will give some response.

E.g. 
1. Action is to execute a referenced item with a given arguments
2. The item is loaded
3. Item's executable type is read
4. If the executable type is core executable then skip to step 6
5. Correct executor reference is searched from a specific index and return to step 2
6. Item executable and the arguments are passed into executor.
7. Executor executes and returns output.

Hmmmm... maybe this mess needs cleaning

## Implementation

### Boot

Note:
No options to be given in boot.
Only after booting, the system will be ready accept input.
All configuration for boot should be in the boot file.

There are following implementation options:
1. Start with module source and execute
2. Start with module source containing only class and execute and initialise

### Item storage

File extension will be aedb.

YAML will be the file markup language.
This makes AEDB file markup subset of YAML.

Options

#### Data

"Key" will be python dict key and "type - value pair" a tuple.

#### Types

types starting "_" will be designed for internal use.

Values with types starting "\_ref_" are not the actual data, but reference to said data.

Some keys that are or will be used:
| Key          | Description                                             |
| ------------ | ------------------------------------------------------- |
| _hash        | Hash of the contents of the item without the hash.      |
| _description | Description of the item                                 |
| _source_code | Source code in the item (meaning the item is a program) |
| _program     | Program (meaning the item is a program)                 |

Some types that are or will be used:
| Type                  | Description                  |
| --------------------- | ---------------------------- |
| \_python              | Python code                  |
| \_ref_internal_python | Reference to internal python |

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
