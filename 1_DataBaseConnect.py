#CREATE USER 'Bhagavan'@'127.0.0.1' IDENTIFIED BY 'mani';
#GRANT ALL PRIVILEGES ON * . * TO 'Bhagavan'@'127.0.0.1';
#FLUSH PRIVILEGES;
'''create a user  in mysql provide necessary permissions''' 

import mysql.connector
con=mysql.connector.connect(user='Bhagavan',password='mani',host='localhost')#,database='sys')
# print ("hello")
mycur=con.cursor()
mycur.execute("sHOW databases")
# mycur.execute("show variables like '%version%'")
# mycur.execute("create DATABASE Python")
# mycur.execute("use python")
# mycur.execute('''drop table Emp; create TABLE Emp
# (
# id int primary key,
# name varchar(5500),
# age int,
# emp_id int 
# )''')
# mycur.execute('''insert into Emp values
# (
# 5,
# 'hkjfdfdf',
# 27,
# 1004 
# )''')
# con.commit()
# mycur.execute("select * from Emp order by 4")
print(mycur.fetchall())
# mylst=mycur.fetchall()
 # for x in mylst:
		# print (x)
		
		
'''import mysql.connector

config = {
  'user': 'scott',
  'password': 'tiger',
  'host': '127.0.0.1',
  'database': 'employees',
  'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)

cnx.close()
'''