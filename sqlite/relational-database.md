# Relational Database
* Relational databases model data by storing rows and columns in tables.
The power of the relational database lies in its ability to efficiently
retrieve data from those tables and in particular where there are multiple
tables and relationship with between those tables

### Terminology
 * Database - contain many tables
 * Relation (or table) - contains tuples and attributes
 * Tuple (or row) - a set of fields that generally represents "object"
   like a person or a music track
 * Attribute (also column or field) - one of possibly many elements of data
   corresponding to the object represented by the row

### Summary
 * A relational database is defined as a set of tuples that have the same
 attributes. A tuple usually represents an object and information about
 that object. Objects are typically physical objects or concepts.
 A relation is usually described as a table, which is organized into rows
 and columns. All the data referenced by an attribute are in the same domain
 and conform to the same concepts.

## SQL
##### Search Query Language
 * a language we use to issue commands to the database
 * create table
 * retrieve some data
 * insert data
 * delete data

### Web Applications with Database
 * Application Developer - Builds the logic for the application, the look and
  feel of the application - monitors the application for problems
 * Database Administrator - Monitors and adjusts the database as the program
 runs
 * Often both people participate in the building of the "data model"

### Database Administrator
 * A database administrator (DBA) is a person responsible for the design,
 implementation, maintenance, and repair of an organization's database.
 The role includes the development and design of database strategies, monitoring
 and improving database performance and capacity, and planning for the future
 expansion requirements. They may also plan, coordinate, and implement security
 measures to safeguard the database.

#### Database Model
 * A database model or database schema is the structure or format of a database,
 described in a formal language supported by the database management system. In
 other words, a database model is the application of a data model when used in
 conjunction with a database management system.

#### Common Databases Systems
 * MySQL
 * Oracle
 * SQL Server
 * SQLite


### Database Normalization
 * There is tons of database theory - way too much to understand without
 excessive predicate calculus
 * **Do not replicate data** - reference data - point to data
 * Use integers for keys and references
 * Add a special **key** column to each table which we'll make references to.
 By conversion, many programmers call this **column id**

##### Three Kinds of Keys
 1. Primary key - generally a integer auto-incremented field
 2. Logical key - what the outside world uses for look up
 3. Foreign key - generally a integer key pointing to a row in another table
###### Foreign key more deeply
 * A foreign key is when a table has column that contains a key which points
 to the primary key of another table
 * When all primary keys are integers, then all foreign keys are integers - this
 is good - very good

  ##### Keys Rules
  **Best practices**
  * Never use your logical key as the primary keys
  * Logical keys can and do change, albeit slowly
  * Relationship that are based on matching string are less efficient than
  integers

##### links used in the class
* commands
<a>https://www.py4e.com/lectures3/Pythonlearn-15-Database-Handout.txt</a>

* Sqlite Browser for linux

```bash
snap install sqlitebrowser
```
### Relational Power
 * By removing the replicate data and replacing with reference for a single
 copy of each bit of data we build a **web** of information that the relational
 database can read through very quickly - even for very large amount of data.
 
 * Often when you want some data it comes from a number of tables linked by
 these foreign keys

### The Join Operation
 * the **join** operation links across several tables as part of a select
 operation

 * you must tell the **join** how to use the keys that make a connection
 between tables using the **on clause**  


### Many-to-Many Relationships
 * Sometimes we need to model a relationship that is many to many
 * We need to add a "connection" table with two foreign keys
 * There is usually no separate primary keys