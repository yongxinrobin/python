import mysql.connector
 
mydb = mysql.connector.connect(
  host="192.168.0.130",
  user="root",
  passwd="Likebin123",
  database="tst_db"
)
mycursor = mydb.cursor()

sql = "insert into book(idbook,book_name,create_date) values(00008,'你当鸟飞往你的山','2020-11-15 00:00:00');"

# sql = "insert into book(idbook,book_name,create_date) values(%s,%s,%s);"
# val = (6,'你当鸟飞往你的山','2020-11-15 00:00:00')
# mycursor.execute(sql, val)

mycursor.execute(sql)
mydb.commit()

print("插入成功的记录条数：", mycursor.rowcount, "记录插入成功。")