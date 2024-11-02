---
layout: post
title: Data Engineer
categories: data science, data engineering
---

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Package Comparison Table</title>
    <style>
        table {
            width: 50%;
            border-collapse: collapse;
            margin: 25px 0;
            font-size: 18px;
            text-align: left;
        }
        th, td {
            padding: 12px;
            border: 1px solid #ddd;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>


<h1> On importing data and relational databases (in Python) </h1>

While preparing data for analysis leans towards the responsibility of the data engineering team, the actual analysis is left to the, well, data analysts. What a surprise! However, before the analysis can begin, the data needs to be imported - from it's source, into the actual environment where it will be used; and that is the topic of this article.

<h2> Barebones basics </h2>

- basic opening files
- flat files
- numeric vs string (numpy vs pandas)
- additional file types (hdf5, pickled files)

In the current world of programming, it is not necessarily a requirement to know the basics of how the parts under the hood work to produce a working program. That being said, it is good practice and one should have an idea of why things are done the way they are. This next section aims to provide some rudimentary information on the background of the different data-science-relevant basics.

<ol>
    <li>
    To access a file with data, one can read a file into the environment. However, as this file will require resources (file handles, memory buffers - RAM) when open, it is best practice to use a context manager. This will close the file after it has been loaded.
    <pre><code>
    with open('demo.txt', 'r') as file:
        print(file.read())
    </code></pre>
    </li>
</ol>

A file will be defined as a 'flat file' if the data is structured in a 2-dimensional manner and  the records (rows) follow a uniform format.


Data will arrive in two fashions, numerical (1,3.14) and string ('quick'). For numeric data, one can use the package 'Numpy' on account of its efficiency in handling numeric data. When it is said that Numpy is efficient, it is referring to it's memory usage and speed for computations. And while string types can be dealt with in Numpy, this is better reserved for the package 'Pandas'. Regarding Pandas, it is the preferred choice when dealing with mixed data types (i.e numeric + string).

<table>
    <tr>
        <th>Data Type</th>
        <th>Numpy</th>
        <th>Pandas</th>
    </tr>
    <tr>
        <td>Numeric</td>
        <td style="text-align: center;">X</td>
        <td></td>
    </tr>
    <tr>
        <td>String</td>
        <td></td>
        <td style="text-align: center;">X</td>
    </tr>
    <tr>
        <td>Mixed</td>
        <td></td>
        <td style="text-align: center;">X</td>
    </tr>
</table>

<pre><code>
import pandas as pd
file_name = "test_file.txt"
data = pd.read_csv("test_file.txt")
</code></pre>

One clever implementation of both numpy and pandas in this corner would be to handle the loading and preprocessing of a .csv file with pandas and then using the .to_numpy() method to convert the data to a Numpy array to leverage Numpy's optimized computational efficiency.

<h2> Pickled files </h2>

import pickle

'rb' stands for 'r' read and 'b' binary.

<pre><code>
with open('test_data.pkl', 'rb') as file:
    x = pickle.load(file)
</code></pre>

<h2> Further file types (excel) </h2>

To load in an excel file with multiple sheets:

<pre><code>
file = 'data.xlsx'
xls = pd.ExcelFile(file)
print(xls.sheet_names)
</code></pre>

And for accessing the sheets + viewing the head:

<pre><code>
df = xls.parse(['sheet_name']) # by name
df1 = xls.parse(0) # by index
df.head() # view the head
df1.head()

# More arguments
df = xls.parse(0, skiprows=[0,1], usecols=[0,1], names=['Height', 'Weight])
</code></pre>


So far the process of importing local files has been reviewed, next, this topic of external importing will be discussed.

<h2> Importing web data </h2>

This requires coding (python) and is better for scaling and reproducibility. First HTTP requests (GET requests) are made, then using modules like beautifulsoup and urllib can be used to parse and download webdata.

Starting with the urllib module, the submodule urllib.request can be accessed to import the urlretrieve() function.

<pre><code>
url = https://www.demo-site.com
urlretrieve(url, 'dataset-demo.csv')
</code></pre>






<h2> List of relevant commands </h2>

<ol>
    <li> 
        Basic importing using a context manager
        <pre><code>
        with open('demo.txt', 'r') as file:
            print(file.read())
        </code></pre>
        </li>
    <li>
        Numpy numeric importing flat file
        <pre><code>
        np.loadtxt('filename.txt', delimiter=',', skiprows=1, usecols[0,1])
        </code></pre>
        </li>
    <li>
        Pandas importing csv files
        <pre><code>
        pd.read_csv('filename.txt', header = None)
        </code></pre>
        </li>
    <li>
        converting pandas dataframe to numpy array
        <pre><code>
        data_object.to_numpy()
        </code></pre>
        </li>
    
</ol>

</body>