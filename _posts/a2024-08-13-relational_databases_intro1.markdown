---
layout: post
title: Relational Databases
categories: data science, data engineering
---

<h1> Relational Databases </h1>

A company running an e-commerce store needs to track various aspects like customers, orders, products, and reviews. To manage and connect this information, the company uses a Database Management System (DBMS). Popular DBMS examples include MySQL, Microsoft SQL Server, PostgreSQL, and SQLite.

Using a DBMS, a database can be created with tables that store information about different categories and their relationships. For instance, each order in the 'CustomerOrders' table has a unique 'primary key', and there are 'foreign keys' that link to other tables like 'OrderedItems', which might include attributes such as the quantity of the ordered item.
<h2> Accessing a Database Using SQLite </h2>

To interact with a SQLite database, you can use create_engine to establish a connection. The following code demonstrates how to create an engine and list the tables in the database:
<pre><code>
from sqlalchemy import create_engine, inspect

# Note the use of 3 '/' characters in the connection string
engine = create_engine('sqlite:///Demo_database.sqlite')

# List database tables
inspector = inspect(engine)
demo_table_names = inspector.get_table_names()
</code></pre>

After creating an engine, you can execute SQL queries, manage data, and interact with tables.

Here’s an overview of the process:
<ol>
    <li>Import packages and functions</li>
    <li>Create the database engine</li>
    <li>Connect to the engine</li>
    <li>Query the database</li>
    <li>Save the query results as a DataFrame</li>
    <li>Close the connection</li>
</ol>

You can streamline this process with a context manager for better resource management:
<pre><code>
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///Demo_data.sqlite')

with engine.connect() as con:
    df = pd.read_sql_query("SELECT * FROM Table_Name", con)
</code></pre>

This approach consolidates the connection handling and query execution into one line:
<pre><code>
engine = create_engine('sqlite:///Demo_data.sqlite')
df = pd.read_sql_query("SELECT * FROM Table_Name", engine)
</code></pre>

To further demonstrate SQL querying, consider filtering and ordering data:
<pre><code>
engine = create_engine('sqlite:///Demo_data.sqlite')
df = pd.read_sql_query("SELECT * FROM Table_Name WHERE Column_A >= 6 ORDER BY Column_B", engine)
</code></pre>

Finally, to illustrate the relational aspect of a database, imagine a company with tables 'CustomerInfo' and 'OrderedItems'. To find customers who have made orders, use the following query:
<pre><code>
engine = create_engine('sqlite:///Demo_data.sqlite')
df = pd.read_sql_query("""
    SELECT CustomerInfo.CustomerName, OrderedItems.ItemName
    FROM CustomerInfo
    INNER JOIN OrderedItems ON CustomerInfo.CustomerID = OrderedItems.CustomerID
    """, engine)
</code></pre>

This query joins the CustomerInfo and OrderedItems tables on CustomerID to retrieve the names of customers and the items they have ordered.