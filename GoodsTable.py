import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Swapna@2003',database='Inventory_Management')
print(mydb.connection_id)
cur=mydb.cursor()
# creating goods table
t2='create table goods(goods_id integer,color varchar(15),product_name varchar(30),manufacturing_date date)'
cur.execute(t2)
# inserting values into goods table
s2='insert into goods(goods_id,color,product_name,manufacturing_date) values(%s,%s,%s,%s)'
a=[(101,'White','Toy car','2023-04-26'),(102,'Brown','Wooden chair','2023-03-11' ),(103, 'Blue','Shirt','2023-02-20'),(104, 'Brown','Toy train','2023-05-01' ),(105, 'Black','Wooden table','2023-04-17')]
cur.executemany(s2,a)
mydb.commit()