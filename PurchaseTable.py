import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Swapna@2003',database='Inventory_Management')
print(mydb.connection_id)
cur=mydb.cursor()
# creating purchase table
t3='create table purchase(purchase_id integer,color varchar(15),product_name varchar(30),store_name varchar(30),purchase_date date,purchase_amount integer)'
cur.execute(t3)
# inserting values into purchase table
s3='insert into purchase(purchase_id,color,product_name,store_name,purchase_date,purchase_amount) values(%s,%s,%s,%s,%s,%s)'
a=[(201,'White','Toy car','Modern Store','2023-04-26',1000),(202,'Brown','Wooden chair','MyKids','2023-05-01',2000 ),(203, 'Blue','Shirt','ORay','2023-02-20',3000),(204, 'Brown','MyCare','Wooden table','2023-05-01',5000 ),(205, 'Black','Wooden table','Fly buy','2023-04-17',4000)]
cur.executemany(s3,a)
mydb.commit()