import psycopg2

conn = psycopg2.connect(
    user='postgres', password='123456', database='test'
)
cursor = conn.cursor()

# cursor.execute('insert into rpt_tutorial (name,age,joindate) values (%s, %s,%s)', ['pyname1', '50','2023-10-19'])
# cursor.execute('insert into rpt_tutorial (name,age,joindate) values (%s, %s,%s)', ['pyname2', '60','2023-10-20'])
# conn.commit()
# print("insert successfully")

# cursor.execute('update  rpt_tutorial set age = %s where name= %s', (66,'pyname2'))
# conn.commit()
# print("update successfully")


cursor.execute('delete from rpt_tutorial where name = %s',('pyname1',))
conn.commit()
print("delete successfully")

cursor.execute('select * from rpt_tutorial ')
values = cursor.fetchall()
print(values)


cursor.close()

conn.close()