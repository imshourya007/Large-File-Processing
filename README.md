# Large-File-Processing
To import products from a CSV file and into a database. There are half a million product details to be imported into the database.

Points to achieve:
  1.Your code should follow concept of OOPS
  2.Support for regular non-blocking parallel ingestion of the given file into a table. Consider thinking about the scale of what should happen if the file is to be processed in 2     mins.
  3.Support for updating existing products in the table based on `sku` as the primary key. (Yes, we know about the kind of data in the file. You need to find a workaround for it)
  4.All product details are to be ingested into a single table
  5.An aggregated table on above rows with `name` and `no. of products` as the columns


Download csv file from: https://drive.google.com/drive/folders/1X3qomdbjWU1oOTbBvxchTzjLMAwYBWFT

# Choosing programming language

I choose woring on python and the reasons are:
  1. Python is Open-source and Easy to Learn
  2. Python is Flexible and Scalable
  3. Python has Multiple Libraries
  4. Python is Portable and Extensible
  
Note: for further details refer: https://www.geeksforgeeks.org/10-reasons-why-you-should-choose-python-for-big-data/

# choosing a database

I choose woring on Microsoft SQL Server Management and sqlite
Note: The project did'nt work accordingly so I have deployed same project in differnt ways.
      1. The file:'sqlServerConn.py': it successfully established a connection between my database 'file_processor' and by using 'create_table()' it is creating a table name
         'tab' in the database.
      3. The function 'fun()': is importing csv file in the database which took '1010.3141043186188 seconds'.
      4. The file: 'LFP.ipynb' it successfully created a 'csv_database' file and on using datframe.to_sql() it took '19.397265672683716 seconds'

# 1. Detailed process of working with 'sqlServerConn.py' and Microsoft SQL Server Management

1. In Microsoft SQL Server Management created a database 'file_processor'.
2. Using Visual Studios: imported pyodbc to establish a conncetion.
3. Create an object to call functions.

Result:
 ![image](https://user-images.githubusercontent.com/64213221/115427484-2302bd00-a21f-11eb-9fb5-b424cf36907e.png)
 ![image](https://user-images.githubusercontent.com/64213221/115427774-63fad180-a21f-11eb-9d4c-93a9d8482fea.png)

What is not done from “Points to achieve”. If not achieved write the possible reasons and current workaround:
Point2: Support for regular non-blocking parallel ingestion of the given file into a table. Consider thinking about the scale of what should happen if the file is to be processed in 2 mins.

What would you improve if given more days:

Create a temp table in your database with the same structure as your main table and create an after insert trigger that updates the records in the main table based on the values inserted into the temp one.   Use "Delete Data and Append" to dump the data into the temp table.  The database will then update the main table as quickly as possible.  

 

# 2. Detailed process of working with 'LFP.ipynb' and sqlite:

The file: 'LFP.ipynb' it successfully created a 'csv_database' file and on using datframe.to_sql() it took '19.397265672683716 seconds'

![image](https://user-images.githubusercontent.com/64213221/115427948-88ef4480-a21f-11eb-9d6e-723237431a76.png)

What is not done from “Points to achieve”. If not achieved write the possible reasons and current workarounds:
point 3.Support for updating existing products in the table based on `sku` as the primary key. (Yes, we know about the kind of data in the file. You need to find a workaround for it)







