import pymysql

# conn = mysql.connector.connect(user='root', password='123456', database='test'
#                                ,auth_plugin ='mysql_native_password')
conn = pymysql.connect(
    user='root', password='123456', database='test'
)
cursor = conn.cursor()
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# # 插入一行记录，注意MySQL的占位符是%s:
# cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])


# cursor.rowcount
# conn.commit()
# cursor.close()

cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
cursor.close()

conn.close()

