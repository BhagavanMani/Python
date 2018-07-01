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

print("hello")

print round(6.6)

print "Hello\bits B Now,\tits T now,\"its doubleQuote now,\'its SingleQuote now,\\Double slash returns?"

str="Bhagavan"
print str[1]

text='''The south asia satellite will be launchuded on may 5, prime minister narendra modi announced on sunday  describing it as indias pricless gift to its neighbours 
seven out of eight SAARC countries are a part of the project which pakistan  refused to join as it did not want the gift form india 
we have always attempted to move ahead with the concept of sabka sath sabka vikas(cooper action of all deevelopment for all) mr modi said in his monthly radio programme manna
ki baat 
the concept is not confied to india but is relevant globally especially in the context of the neighbourhood  he said 
there should be cooperation of our neighbour and there should be development of our  neighbours too he said 
on may 5 india will launch the south asia satellite the benefits of this satellite will go along way to meeting the developmental needs of the countries participating in this project he said 
this is an appropriate example of our commitment towards south asia the satellite of south asia will help in the ovrall develapment of the entire region he said 
the benifits 
The south asia satellite will be launched on may 5, prime minister narendra modi'''
print text.center(5)
