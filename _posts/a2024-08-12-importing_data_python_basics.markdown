---
layout: post
title: Importing Data
categories: data science, data engineering
---

<h1>Importing Data and Relational Databases in Python</h1>

When preparing data for analysis, the heavy lifting is often done by data engineers. Their role is to ensure that data is properly imported from its source into the environment where it will be used for analysis. This post explores the fundamentals of importing data and handling relational databases using Python.

<h2>Basics of Data Importing</h2>

Before diving into specifics, it's important to understand some core concepts of data importing:

<h3>Basic File Operations</h3>

To work with data files in Python, efficient management of file access and resources is essential. Here’s a basic example of how to read a file using a context manager:

<pre><code>
with open('demo.txt', 'r') as file:
    print(file.read())
</code></pre>

Using a context manager ensures that the file is properly closed after it's read, which helps manage system resources effectively.

<h3>Flat Files and Data Types</h3>

Flat files are structured in a two-dimensional format where records (rows) follow a uniform structure. Data in these files can be numerical or string-based:

- **Numerical Data:** For efficient handling of numerical data, the `NumPy` library is recommended due to its optimized performance in terms of memory usage and computation speed.
- **String Data:** While `NumPy` can handle strings, the `Pandas` library is generally preferred for mixed data types (numeric and string).

<h4>Data Type Comparison</h4>

Here is a quick comparison of how `NumPy` and `Pandas` handle different data types:

<table>
    <tr>
        <th>Data Type</th>
        <th>NumPy</th>
        <th>Pandas</th>
    </tr>
    <tr>
        <td>Numeric</td>
        <td style="text-align: center;">✔️</td>
        <td></td>
    </tr>
    <tr>
        <td>String</td>
        <td></td>
        <td style="text-align: center;">✔️</td>
    </tr>
    <tr>
        <td>Mixed</td>
        <td></td>
        <td style="text-align: center;">✔️</td>
    </tr>
</table>

<pre><code>
import pandas as pd

file_name = "test_file.txt"
data = pd.read_csv(file_name)
</code></pre>

A common approach is to use `Pandas` for loading and preprocessing data, and then convert it to a `NumPy` array for optimized computations:

<pre><code>
numpy_array = data.to_numpy()
</code></pre>

<h2>Pickled Files</h2>

Pickled files are used to serialize and deserialize Python objects. To load data from a pickled file, use the following code:

<pre><code>
import pickle

with open('test_data.pkl', 'rb') as file:
    data = pickle.load(file)
</code></pre>

Here, `'rb'` stands for 'read binary', indicating that the file is read in binary mode.

<h2>Working with Excel Files</h2>

Excel files often contain multiple sheets. To handle these, the `Pandas` library can be used:

<h3>Loading Excel Files</h3>

<pre><code>
file = 'data.xlsx'
xls = pd.ExcelFile(file)
print(xls.sheet_names)
</code></pre>

<h3>Accessing Sheets and Viewing Data</h3>

To access specific sheets and view the data:

<pre><code>
df = xls.parse('sheet_name')  # by name
df1 = xls.parse(0)  # by index
print(df.head())  # view the head
print(df1.head())
</code></pre>

Skipping rows and selecting specific columns while importing can be done as follows:

<pre><code>
df = xls.parse(0, skiprows=[0,1], usecols=[0,1], names=['Height', 'Weight'])
</code></pre>

<h2>Summary of Commands</h2>

Here is a quick reference for common data importing commands:

<ol>
    <li>Basic File Importing Using Context Manager
        <pre><code>
        with open('demo.txt', 'r') as file:
            print(file.read())
        </code></pre>
    </li>
    <li>NumPy Numeric Importing from Flat Files
        <pre><code>
        import numpy as np
        np.loadtxt('filename.txt', delimiter=',', skiprows=1, usecols=[0,1])
        </code></pre>
    </li>
    <li>Pandas Importing CSV Files
        <pre><code>
        import pandas as pd
        pd.read_csv('filename.txt', header=None)
        </code></pre>
    </li>
    <li>Converting Pandas DataFrame to NumPy Array
        <pre><code>
        numpy_array = data_object.to_numpy()
        </code></pre>
    </li>
</ol>

This guide provides a basic foundation for importing data and working with various file types in Python.