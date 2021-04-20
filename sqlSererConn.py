import pyodbc
import pandas as pd
import csv
from sqlalchemy import create_engine
import urllib
import time

class file:

    def __init__(self,conn):
        self.conn = conn
    
    def create_table(self):
        # Dropping table data if exists
        conn.execute("DROP TABLE IF EXISTS tab;")
        sql = '''CREATE TABLE tab(
            name      [NVARCHAR](50)  NOT NULL,
            sku		 [NVARCHAR](100)  NOT NULL,
            description     [NVARCHAR](200)  NOT NULL
        )'''
        # Creating a table
        conn.execute(sql)
        print("data table is created successfully...............")  

    def fun(self):
        cur = conn.cursor()
        start_time = time.time()
        with open('products.csv','r') as f:
            reader = csv.reader(f)
            next(reader) # Skip the header row.
            for row in reader:
                cur.execute(
                'INSERT INTO tab VALUES (?, ?, ?)',
                row)    
        print("pd.read_csv with chunksize took %s seconds" % (time.time() - start_time))
        conn.commit() 
'''
  
    def execute_many(self):

        Data = pd.read_csv('products.csv',index_col=False)
        df = Data
        # Creating a list of tupples from the dataframe values
        tpls = [tuple(x) for x in df.to_numpy()]
    
        # dataframe columns with Comma-separated
        cols = ','.join(list(df.columns))
    
        # SQL query to execute
        sql = "INSERT INTO data VALUES(%s,%s,%s,%s)" % (cols)
        cursor = conn.cursor()
        cursor.executemany(sql, tpls)
        conn.commit()
        print("Data inserted using execute_many() successfully...") 
    

    def using_sqlalchemy(self):
        Data = pd.read_csv('products.csv',index_col=False)
        df = pd.DataFrame(Data)
        print("Inside using_sqlalchemy")
        cols = ','.join(list(df.columns))
        sql='INSERT INTO tab VALUES(%s,%s,%s)'
        cursor = conn.cursor()
        cursor.executemany(sql,)
        start_time = time.time()
        df.read_to_sql(cursor,schema="dbo",con=conn, index=False, if_exists='append',chunksize = 10000)
        print("pd.read_csv with chunksize took %s seconds" % (time.time() - start_time))
        print("Data inserted using to_sql()(sqlalchemy) done successfully...")'''

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=localhost;"
    "Database=file_processor;"     
    "Trusted_Connection=yes;"
    )

file1 = file(conn)
file1.create_table()
file1.fun()