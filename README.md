## Python script that interacts with a SQL database.

[![SQL CI/CD](https://github.com/nogibjj/IDS-Week5_MiniProject_us26/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/IDS-Week5_MiniProject_us26/actions/workflows/cicd.yml)


<p align="center">
  <img width="600" src="https://github.com/nogibjj/sqlite-lab/assets/58792/b39b21b4-ccb4-4cc4-b262-7db34492c16d" alt="sql">
</p>


### Overview

This repo has been created by forked from (https://github.com/nogibjj/sqlite-lab). I have used world university ranking csv file and loaded it into 'ranking.db' database under the table name 'universities'.

Here is an overview of CRUD operations:
		
    CRUD stands for Create, Read, Update, and Delete, which are the four basic operations for managing data in a database or data storage system. These operations are essential for interacting with and manipulating data within an application or database. Here's a brief overview of each CRUD operation:

1. **Create (C)**:
   - Create is the operation used to add new data or records to a database.
   - It typically involves inserting a new row or document into a database table or collection.
   - In SQL, you use the `INSERT INTO` statement to create new records in a table.
   - In NoSQL databases, you often use methods like `insertOne` or `insertMany` to add documents to a collection.

2. **Read (R)**:
   - Read is the operation used to retrieve data from a database.
   - It involves querying the database to fetch existing records based on specific criteria.
   - In SQL, you use the `SELECT` statement to read data from a table.
   - In NoSQL databases, you use various query methods to retrieve documents that match your criteria.

3. **Update (U)**:
   - Update is the operation used to modify existing data in a database.
   - It typically involves changing the values of one or more fields in an existing record.
   - In SQL, you use the `UPDATE` statement to update data in a table.
   - In NoSQL databases, you use methods like `updateOne` or `updateMany` to modify documents in a collection.

4. **Delete (D)**:
   - Delete is the operation used to remove data from a database.
   - It can involve deleting specific records or entire rows from a table.
   - In SQL, you use the `DELETE` statement to remove data from a table.
   - In NoSQL databases, you use methods like `deleteOne` or `deleteMany` to delete documents from a collection.


### Code Description

1. Read
2. Create
3. Update
4. Delete
5. Makefile with the following:

	- install: using requirements.txt file to install required packages

	- test:

	python -m pytest -vv --cov=main *.py
<p align="center">
  <img width="600" src="https://github.com/nogibjj/IDS-Week5_MiniProject_us26/blob/main/images/test.png" alt="install">
</p>

	- format: using black formatter

<p align="center">
  <img width="600" src="https://github.com/nogibjj/IDS-Week5_MiniProject_us26/blob/main/images/format.png" alt="format">
</p>

      - lint: using ruff 

<p align="center">
  <img width="600" src="https://github.com/nogibjj/IDS-Week5_MiniProject_us26/blob/main/images/lint.png" alt="lint">
</p>	
