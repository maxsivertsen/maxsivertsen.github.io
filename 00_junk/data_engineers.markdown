---
layout: post
title: Data Engineer
categories: data science, data engineering
---

<h1> What is data engineering? </h1>

Data engineering is storing, cleaning, and managing data. But to contextualize it in the bigger picture, let's write a story.

Imagine that there is a restaurant with a high customer flow. For a successful evening, the business requires a team of members, each with their own individual task. Before the first customer has even arrived, the shift has begun. First, the ingredients for the evening's dishes need to be delivered by a logistics team. Next, the chefs in the kitchen will prepare their dishes using these ingredients, they check if there is mold or if there are any ingredients missing. Things are heating up now, and it is important that the chefs and servers have good communication, they function as one. Servers quickly grab the dishes and plate up, presenting them to the customer. After everything has been finished, the night comes to a close. As a final effort, the owner evaluates the customer reviews to determine any necessary changes.

In this example, we can break down the evenings responsible groups as follows:
- logistics team delivering *
- chefs preparing ingredients **
- servers presenting dishes **
- owner evaluating ***

If you are familiar with machine learning and data science, you might already see the not-so-hidden metaphor. Working from the top then, the owner evaluating the reviews would be the machine learning team, using models to determine if the combination of ingredients resulted in good reviews. Presentation of the dishes and their preparation can be attributed to data scientists, who are cleaning and preparing food, experimenting with design, and perfecting appearance of the dishes (data). Finally, we have the logistics team. They deliver the ingredients to the restaurant. It is their responsibility to obtain the ingredients in raw format, they need to make it available for the kitchen, and it needs to be packaged in a way that it doesn't cause a headache for the chefs.

To get away from the metaphor - a data engineer has to collect and store the data in such a way that data scientist can easily access and analyze the data. This involves not only storing the data, but also creating databases and building data pipelines.

<h2> Data structures </h2>

Data engineering requires storing and handling data of different types. Some data may be easily defined and stored in a a simple spread sheet, this would be structured data. Other data may have a less defined frame, such a XML or JSON format. Finally, there is unstructured data. This could be pictures, text, videos and images. These data are difficult to categorize and evaluate without the help of machine learning (for example clustering techniques).

<h2> Data lakes, -warehouses, and -catalogs </h2>

These terms are essential when understanding data engineering. As the warden of your teams incoming data, it is your job to handle all incoming data and prepare it for use down the line. This begins with a datalake, the manner in which all data is stored in an unorganized, data-type indiscriminate approach. This often is done without a hierarchial file structure, and items can only be accessed by token-ID. Once this data has been processed, it can be stored in data warehouses. Here, the data is labeled and likely to have a traditional hierarchial file structure format. However, to allow for reproducibility and tracking of the processes at hand, a data catalog is necessary to avoid a data swamp. It is good practice and should be employed for any data engineering project.

<h2> Data processing </h2>

To ensure a better working environment for data scientists, it is necessary to process the data before they receive it. This is done by the data engineer. It involves file resizing, data type conversion, filtering bad data, organizing, and structuring the data. To facilitate this process, a pipeline can be created to handle the data preemptively and save the engineer some work. For example, this may involve automatic filtering of corrupted files or compression of a filtered file type. A common framework for handling data processing is Spark, which will assist the engineer in processing large amounts of data.