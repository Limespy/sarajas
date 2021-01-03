# Flexible Database Concept

## Meta

## Fundamentals

### Aim


### Meditations



### Philosophies

Full version history and control




### Doctrines

## Design

The database should be considered an indexing system for arbitrary number of multiple different systems. The data can be fully stored in the database item or exist outside with database item functioning as metadata, linking and API layer to the actual data. 

All things are items in the database, including the source code.

This means the source code allows modification of itself. 
Please be careful. 

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

### Language

Python

### Booting


```
python "database folder name"
```

### Version control

Version control provided by Git

There shall be git wrapper through python 
