import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Swapna@2003',database='Inventory_Management')
print(mydb.connection_id)
cur=mydb.cursor()
# creating manufacture table
t1='create table manufacture(m_id integer,color varchar(35),product_name varchar(30),no_of_items_req integer,defective_items integer,manufacturing_date date,company varchar(70))'
cur.execute(t1)
#inserting values into manufacture table
s1='insert into manufacture(m_id,color,product_name,no_of_items_req,defective_items,manufacturing_date,company) values(%s,%s,%s,%s,%s,%s,%s)'
a=[(1,'red','Toy car', 50, 2,'2023-04-25','ABC'),(2,'Brown','Wooden chair', 100,5, '2023-03-15','SS export' ),(3,'Blue','Shirt', 200, 5,'2023-02-20','SSS'),(4,'Brown','Toy train', 75,3, '2023-05-01','PQR' ),(5,'Black','Wooden table',  50,5, '2023-04-10','CCC')]
cur.executemany(s1,a)
mydb.commit()
