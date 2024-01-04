import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Swapna@2003',database='Inventory_Management')
print(mydb.connection_id)
cur=mydb.cursor()
# question 7
d='DELETE FROM purchase WHERE product_name = "shirt" AND purchase_date = "2023-04-01" AND store_name = "ORay"'
cur.execute(d)
mydb.commit()