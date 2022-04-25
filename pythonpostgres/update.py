
import psycopg2

def get_db_conn():
    conn = psycopg2.connect(host="localhost", database="bdusters", user="postgres", password="postgres")
    return conn

conn = get_db_conn()
cur = conn.cursor()
name = 'Anju'
newname = 'Aanju'
cur.execute('UPDATE customers SET name = %s WHERE name = %s',(newname, name))
cur.execute('Select * from customers')
cust = cur.fetchall()
print(cust)

conn.commit()
cur.close()
conn.close()
      
