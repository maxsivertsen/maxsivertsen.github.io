---
layout: post
title: Data Engineer
categories: data engineering, dbms, database, relational databases
---

<h1> Relational Databases </h1>

A company runs an e-commerce store and would like to keep track of their customers, the customer orders, ordered items, products, reviews, and so on. To connect the different categories of information, the company uses a software type called DBMS - database management system. Examples of popular DBMS are MySQL, Microsoft SQL Server, PostgreSQL, and SQLite.

One can then use a DBMS to create a database. Inside of the database, different tables exist and contain information about the various categories and their relations to one another. For example, each order in the 'CustomerOrders' table will have a unique ID known as the 'primary key'. Additionally, there will be further 'foreign' keys that relate a given entry (row) to another table; this could be an attribute (column) called 'OrderedItems'. The foreign key can be followed to it's native table where the relevant information will be contained; in this case we could imagine that one of the attributes in 'OrderedItems' may be the quantity of the ordered item.

<h2> Accessing a database using SQLite </h2>

To access a database in SQLite, one uses create_engine to establish a connection to a database while passing (defining) the database type and its location (connection string). The following code demonstrates creating an engine and viewing the tables of the loaded database.

<pre><code>
from sqlalchemy import create_engine

# Note 3 '/' characters : the 3rd '/' is part of the database's file path
engine = create_engine('sqlite:///Demo_database.sqlite')

# Read the database tables
demo_table_names = engine.table_names()

</code></pre>

After creating an engine object, it can be used to execute SQL queries, manage the database's data, and interact with tables. 

To provide an overview of the process: 
<ol>
    <li> Import packages and functions </li>
    <li> Create the database engine </li>
    <li> Connect to the engine </li>
    <li> Query the database </li>
    <li> Save the query results as a DataFrame </li>
    <li> Set the column names (if desired) </li>
    <li> Close the connection </li>
</ol>

<pre><code>
# Import
from sqlalchemy import create_engine
import pandas as pd

# Create the engine
engine = create_engine('sqlite:///Demo_data.sqlite')

# Connect the engine
con = engine.connect()

# Query the database
results = con.execute("SELECT * FROM Table_Name")

# Save the results
df = pd.DataFrame(results.fetchall())

# Column names
df.columns = results.keys()

# Close connection
con.close()
</code></pre>

This process could be improved by incorporating a context manager as follows:

<pre><code>
engine = create_engine('sqlite:///Demo_data.sqlite')

with engine.connect() as con:
    result = con.execute("SELECT * From Table_Name")
    df = pd.DataFrame(result.fetchall())
    df.columns = result.keys()

</code></pre>

By using the context maanger, file handling and resource management is better utilized.

So far, this process has been diluted to four steps post engine creation: engine connection, data extraction, saving the data, defining column names. This can be further compressed into just one single line of code.

<pre><code>
engine = create_engine('sqlite:///Demo_data.sqlite')
df = pd.read_sql_query("SELECT * FROM Table_Name", engine)
</code></pre>

As a further snippet to demonstrate the SQL phrasing:

<pre><code>
engine = create_engine('sqlite:///Demo_data.sqlite')
df = pd.read_sql_query("SELECT * FROM Table_Name WHERE Column_A >= 6 ORDER BY Column_B", engine)
</code></pre>

Finally, it would be good to conclude with a return to the relational aspect of the database. Imagine again the example from the beginning, a company that has an e-commerce website. It has a database with different tables, and for the use-case here, the tables 'CustomerInfo' and 'OrderedItems' will be shown. The attributes of interest are the customer name and the name of the ordered item. Both tables include an attribute called CustomerID - with this attribute being the primary key in the CustomerInfo and a foreign key in the OrderItems table. Using the pd.read_sql_query function, a search can be made to return all rows where customers have made orders (imagine for a moment that some customers have registered, but never made an order, thus the filtering).

<pre><code>
engine = create_engine('sqlite:///Demo_data.sqlite')
df = pd.read_sql_query("SELECT CustomerName, ItemName FROM CustomerInfo INNER JOIN OrderedItems on CustomerInfo.CustomerID = OrderedItems.CustomerID", engine)
</code></pre>