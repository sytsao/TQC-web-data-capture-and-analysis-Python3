import csv
import sqlite3
# CSV 輸入檔的路徑與名稱       
input_file = 'data.csv'

# 建立一個SQLite3 記憶體資料庫 
# 建立有五個屬性的資料表       
con = sqlite3.connect('Supplier.db')
c = con.cursor()
create_table = """CREATE TABLE IF NOT EXISTS Supplier
        (Supplier_Name VARCHAR(20), Part_Number VARCHAR(20),Cost FLOAT,Purchase_Date DATE);"""
c.execute(create_table)
con.commit()
# 讀取CSV檔, 將資料插入Suppliers資料表
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader, None)
for row in file_reader:
	data = []
	for column_index in range(len(header)):
		data.append(row[column_index])	
	c.execute("INSERT INTO Supplier VALUES (?, ?, ?, ?);", data)
con.commit()
# 查詢Suppliers資料表            
output = c.execute("SELECT * FROM Supplier")
rows = output.fetchall()
for row in rows:
	output = []
	for column_index in range(len(row)):
		output.append(str(row[column_index]))
	print(output)
