import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Swapna@2003',database='Inventory_Management')
print(mydb.connection_id)
cur=mydb.cursor()
# creating Inventory_Management database
cur.execute('create database Inventory_Management')
# creating manufacture table
t1='create table manufacture(m_id,color varchar(15),product_name varchar(30),no_of_items_req integer,defective_items integer,manufacturing_date date,company varchar(70))'
cur.execute(t1)
# creating goods table
t2='create table goods(goods_id integer,color varchar(15),product_name varchar(30),manufacturing_date date)'
cur.execute(t2)
# creating purchase table
t3='create table purchase(purchase_id integer,color varchar(15),product_name varchar(30),store_name varchar(30),purchase_date date,purchase_amount integer)'
cur.execute(t3)
# creating sale table
t4='create table sale(sale_id integer,color varchar(15),product_name varchar(30),store_name varchar(30),sale_date date,sale_amt integer,profit_margin float,manufacturing_date date)'
cur.execute(t4)
mydb.commit()
# inserting values into manufacture table
s1='insert into manufacture(m_id,color,product_name,no_of_items_req,defective_items,manufacturing_date,company) values(%s,%s,%s,%s,%s,%s,%s)'
a=[(1,'red','Toy car', 50, 2,'2023-04-25','ABC'),(2,'Brown','Wooden chair', 100,5, '2023-03-15','SS export' ),(3,'Blue','Shirt', 200, 5,'2023-02-20','SSS'),(4,'Brown','Toy train', 75,3, '2023-05-01','PQR' ),(5,'Black','Wooden table',  50,5, '2023-04-10','CCC')]
cur.executemany(s1,a)
mydb.commit()
# inserting values into goods table
s2='insert into goods(goods_id,color,product_name,manufacturing_date) values(%s,%s,%s,%s)'
a=[(101,'White','Toy car','2023-04-26'),(102,'Brown','Wooden chair','2023-03-11' ),(103, 'Blue','Shirt','2023-02-20'),(104, 'Brown','Toy train','2023-05-01' ),(105, 'Black','Wooden table','2023-04-17')]
cur.executemany(s2,a)
mydb.commit()
# inserting values into purchase table
s3='insert into purchase(purchase_id,color,product_name,store_name,purchase_date,purchase_amount) values(%s,%s,%s,%s,%s,%s)'
a=[(201,'White','Toy car','Modern Store','2023-04-26',1000),(202,'Brown','Wooden chair','MyKids','2023-05-01',2000 ),(203, 'Blue','Shirt','ORay','2023-02-20',3000),(204, 'Brown','MyCare','Wooden table','2023-05-01',5000 ),(205, 'Black','Wooden table','Fly buy','2023-04-17',4000)]
cur.executemany(s3,a)
mydb.commit()
# inserting values into sale table
s4='insert into sale(sale_id,color,product_name,store_name,sale_date,sale_amt,profit_margin,manufacturing_date) values(%s,%s,%s,%s,%s,%s,%s,%s)'
a=[(10,'White','Toy car','Modern Store','2023-05-01',1500,0.3,'2023-04-01'),(11,'Brown','Wooden chair','Honeydew','2023-04-20',2500,0.5,'2023-03-11'),(203, 'Blue','Shirt','The Blue dress','2023-05-4',3500,0.4,'2023-02-20'),(204, 'Brown','MyCare','Wooden table','2023-04-01',5500,0.5,'2023-05-01' ),(205, 'Black','Wooden table','Fly buy','2023-05-22',4000,0.2,'2023-04-17')]
cur.executemany(s4,a)
mydb.commit()
# q7
d='DELETE FROM purchase WHERE product_name = "Shirt" AND purchase_date = "2023-04-01" AND store_name = "ORay"'
cur.execute(d)
mydb.commit()
# q9
s='UPDATE manufacture SET  = 500 WHERE color = "Red" AND manufacture_id IN (SELECT manufacture_id FROM goods WHERE goods_id IN (SELECT goods_id FROM sale WHERE store_name = "MyKids")'
cur.execute(s)
mydb.commit()

#q9
u='SELECT * FROM  goods JOIN manufacture ON goods.manufacture_id = manufacture.manufacture_id WHERE product_name = "wooden chair" AND manufacture_date < "2023-05-01"'
cur.execute(u)
rows=cur.fetchall()
for x in rows:
    print(x)
mydb.commit()
#q10
v='SELECT sale.profit_margin FROM sale JOIN goods ON sale.goods_id = goods.goods_id JOIN manufacture ON goods.manufacture_id = manufacture.manufacture_id JOIN purchase ON goods.purchase_id = purchase.purchase_id WHERE product_name = "wooden table" AND store_name = "MyCare",company = "SS Export"'
cur.execute(v)
row = cur.fetchone()
print(row[0])
mydb.commit()
