import mysql.connector

conn = mysql.connector.connect(host="localhost",port="3306",user="root",password="",database="quanlynhanvien")
cursor = conn.cursor()
selectquery = "select * from nhanvien"
cursor.execute(selectquery)
records = cursor.fetchall()
print("Tổng số nhân viên",cursor.rowcount)

for row in records:
    print("MaNV",row[0])
    print("TenNV",row[1])
    print("Gioitinh", row[2])
    print("NgaySinh", row[3])
    print("DiaChi", row[4])
    print("ChucVu", row[5])
    print()
cursor.close()
conn.close()