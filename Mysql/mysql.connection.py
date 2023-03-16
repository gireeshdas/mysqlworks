import pymysql

db=pymysql.connect(host="localhost",user="root",password="gireeshdas",db="college")

obj=db.cursor()

obj.execute("SELECT VERSION()")
data= obj.fetchone()
print("your database version is", data)


obj.execute("show tables")
a=obj.fetchall()
print("your tables are:",a)


obj.execute("select * from teacher")
output=obj.fetchall()
for i in output:
    print(i)