import psycopg2

def get_db_conn():
    conn = psycopg2.connect(host="localhost", database="bdusters", user="postgres", password="postgres")
    return conn

conn = get_db_conn()
cur = conn.cursor()

name = 'Nosa'
newname = 'Anju'
base_sql = ["UPDATE customers SET "]
base_list = (newname, name)

if newname != "":
    base_sql.append("name = %s")
    sql = str("".join(base_sql))
    #base_list.append(newname)

#base_list.append(name)


print(sql, base_list)

cur.execute(sql, base_list)
# cur.execute('UPDATE customers SET name = %s WHERE name = %s',(newname, name))
cur.execute('Select * from customers')
cust = cur.fetchall()
print(cust)

conn.commit()
cur.close()
conn.close()
      





    