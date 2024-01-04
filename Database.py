import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Swapna@2003')
print(mydb.connection_id)
cur=mydb.cursor()
# creating Inventory_Management database
cur.execute('create database Inventory_Management')