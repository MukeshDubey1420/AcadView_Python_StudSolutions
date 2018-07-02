'''
Installation steps
1. First install mysql-community software(refer the link mentioned below)<br > https://www.youtube.com/watch?v=WuBcTJnIuzo

2. Set path to be able to access mysql command-

    To make it easier to invoke MySQL programs, you can add the path name of the MySQL bin directory to your Windows system PATH environment variable:

    On the Windows desktop, right-click the My Computer icon, and select Properties.

    Next select the Advanced tab from the System Properties menu that appears, and click the Environment Variables button.

    Under System Variables, select Path, and then click the Edit button. The Edit System Variable dialogue should appear.

    Place your cursor at the end of the text appearing in the space marked Variable Value. (Use the End key to ensure that your cursor is positioned at the very end of the text in this space.) Then enter the complete path name of your MySQL bin directory (for example, C:\Program Files\MySQL\MySQL Server 5.7\bin)

    Note
    There must be a semicolon separating this path from any values present in this field.


3. Now run mysql in your terminal
    Make a password for root, root password
    mysql -u root -p
    Enter the password you had set during installation to enter the MySQL Command Line
    Create a database-  create database demo;
    Create user-  CREATE USER 'helpme'@'localhost';
    After that grant all privileges to this user- GRANT ALL PRIVILEGES ON demo.* TO 'helpme'@'localhost';

4. Now go back to your command line and login using new user details
    mysql -u helpme
    You should be able to see demo when you run this- show databases;

5.  pip install pymysql

    To connect to your databse and user, don't forget to put your detail while making a connection
    i.e. pymysql.connect(host='localhost', database='demo', user='helpme')

'''
#Basic establish a connection
# import pymysql
#
#
# try:
#     connection = pymysql.connect(host='localhost', database='yello', user='helpme')
#     print(connection)
#
# finally:
#     connection.close()
#     print('Done!!')

#Create
# import pymysql as pm
#
# try:
#     con = pm.connect(host='localhost', database='yello', user='helpme')
#
#     cursor = con.cursor()
#
#     query = 'create table employees1(eno int(5) primary key, ename varchar(10), eage int(3), eincome double(10,2))'
#
#     cursor.execute(query)
#
#     print('Table created successfully!!')
#
# except pm.DatabaseError as e:
#     if con:
#         con.rollback()
#         print('Problem occured: ', e)
#
# finally:
#     if cursor:
#         cursor.close()
#     if con:
#         con.close()
#     print('Done!!')

#Insert
# import pymysql as pm
#
# try:
#     con = pm.connect(host='localhost', database='yello', user='helpme')
#
#     cursor = con.cursor()
#
#     query = "insert into employees1(eno, ename, eage, eincome) \
#     values(%s, %s, %s, %s)"
#
#     records = [(1, 'abc', 23, 23000),
#                (2, 'def', 24, 20000),
#                (3, 'ghi', 50, 100000)]
#
#     cursor.executemany(query, records)
#
#     con.commit()
#
# except pm.DatabaseError as e:
#     if con:
#         con.rollback()
#         print('Problem occured: ', e)
#
# finally:
#     if cursor:
#         cursor.close()
#     if con:
#         con.close()
#     print('Done!!')

#Read
# import pymysql as pm
#
# try:
#     con = pm.connect(host='localhost', database='yello', user='helpme')
#
#     cursor = con.cursor()
#
#     query = 'select * from employees1'
#
#     cursor.execute(query)
#
#     data = cursor.fetchall()
#
#     for row in data:
#         print('Eno: {}, Ename: {}, Eage: {}, Esal: {}' \
#               .format(row[0], row[1], row[2], row[3]))
#
# except pm.DatabaseError as e:
#     if con:
#         con.rollback()
#         print('Problem occured: ', e)
#
# finally:
#     if cursor:
#         cursor.close()
#     if con:
#         con.close()
#     print('Done!!')

#Update
# import pymysql as pm
#
# try:
#     con = pm.connect(host='localhost', database='yello', \
#                      user='helpme')
#
#     cursor = con.cursor()
#
#     query = "update employees1 set eage=eage+1 where ename = 'def'"
#
#     cursor.execute(query)
#
#     con.commit()
#
# except pm.DatabaseError as e:
#     if con:
#         con.rollback()
#         print('Problem occured: ', e)
#
# finally:
#     if cursor:
#         cursor.close()
#     if con:
#         con.close()
#     print('Done!!')

#Delete
# import pymysql as pm
#
# try:
#     con = pm.connect(host='localhost', database='yello', \
#                      user='helpme')
#
#     cursor = con.cursor()
#
#     age = input('Enter age: ')
#
#     query = "delete from employees1 where eage='%s'" % (age)
#
#     cursor.execute(query)
#
#     con.commit()
#
# except pm.DatabaseError as e:
#     if con:
#         con.rollback()
#         print('Problem occured: ', e)
#
# finally:
#     if cursor:
#         cursor.close()
#     if con:
#         con.close()
#     print('Done!!')