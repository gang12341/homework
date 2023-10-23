import psycopg2
import csv
import pandas as pd

# conn = psycopg2.connect(
#     user='postgres', password='123456', database='test'
# )
# cursor = conn.cursor()

# cursor.execute('select * from rpt_tutorial ')
# data = cursor.fetchall()

# cursor.close()

# header = ('id','名字','年龄','加入时间')

# with open("test.csv","w+",newline="") as file:
#     p = csv.writer(file)
#     p.writerow(header)

#     for i in data:
#         a = list(i)
#         p.writerow(a)

data2 = pd.read_csv("test.csv",encoding="gbk")
print(data2)

