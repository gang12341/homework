import psycopg2
import csv
import pandas as pd

tablename = "rpt_tutorial"

conn = psycopg2.connect(
    user='postgres', password='123456', database='test'
)
cursor = conn.cursor()


with open("test.csv","r") as file:
    next(file)
    cursor.copy_from(file,tablename,sep=',',)

conn.commit()
cursor.close()