import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Swapna@2003',database='Inventory_Management')
print(mydb.connection_id)
cur=mydb.cursor()
# creating sale table
#t4='create table sale1(sale_id integer,color varchar(35),product_name varchar(30),store_name varchar(30),sale_date date,sale_amt integer,profit_margin float,manufacturing_date date)'
#cur.execute(t4)
# inserting values into sale table
s4='insert into sale(sale_id,color,product_name,store_name,sale_date,sale_amt,profit_margin,manufacturing_date) values(%s,%s,%s,%s,%s,%s,%s,%s)'
a=[(10,'White','Toy car','Modern Store','2023-05-01',1500,0.3,'2023-04-01'),(11,'Brown','Wooden chair','Honeydew','2023-04-20',2500,0.5,'2023-03-11'),(203, 'Blue','Shirt','The Blue dress','2023-05-4',3500,0.4,'2023-02-20'),(204, 'Brown','MyCare','Wooden table','2023-04-01',5500,0.5,'2023-05-01' ),(205, 'Black','Wooden table','Fly buy','2023-05-22',4000,0.2,'2023-04-17')]
cur.executemany(s4,a)
mydb.commit()