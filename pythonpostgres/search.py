import psycopg2

def get_db_conn():
    conn = psycopg2.connect(host="localhost", database="bdusters", user="postgres", password="postgres")
    return conn

conn = get_db_conn()
cur = conn.cursor()

sql = 'SELECT * FROM customers WHERE name = %s'
searchName = 'Anj'
# cur.execute(sql, [searchName,])
cur.execute('SELECT * FROM customers WHERE name = %s', [searchName,])

searchrec = cur.fetchone()

print(searchrec)

conn.commit()
cur.close()
conn.close()