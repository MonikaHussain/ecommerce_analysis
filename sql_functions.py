# importing dependencies
import os 
import mysql.connector
# from mysql import connector
from dotenv import load_dotenv
import pandas as pd


# loading dotenv
load_dotenv()
# print(os.getenv(USER))
user = os.getenv('USER')
password = os.getenv('PASSWORD')
host = os.getenv('HOST')
database = 'swiftmarket'


# Establing connection
connection = mysql.connector.connect(user = user,
                                     password = password,
                                     host = host,
                                     database = database)

cursor = connection.cursor()


# to read sql query
def read_query(query):
    
    cursor.execute(query)
    rows = cursor.fetchall()
    
    return pd.DataFrame(data=rows, columns=cursor.column_names)