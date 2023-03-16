import pymysql

db=pymysql.connect(host="localhost",user="root",password="gireeshdas",db="python_may")

obj=db.cursor()
obj.execute("select version()")
data= obj.fetchone()
print("your database version is", data)

# obj.execute("CREATE TABLE Employee (Id int,name varchar(20),age int,place varchar(20),position varchar(20))")
obj.execute("insert into Employee values(01,'Gireesh Das',25,'Edayar','HR')")
obj.execute("insert into Employee values(01,'Anju',25,'Edayar','Manager')")
obj.execute("select * from Employee")
data=obj.fetchall()
for i in data:
    print(i)
