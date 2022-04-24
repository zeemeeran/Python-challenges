
#from operator import ge
#import re
import re
from flask import Flask, redirect, url_for, render_template, request
from  flask_sqlalchemy import SQLAlchemy
import psycopg2
#from requests import request

app = Flask(__name__)

def get_db_conn():
    conn = psycopg2.connect(host="localhost", database="bdusters", user="postgres", password="postgres")
    return conn


'''
#cur.execute('DROP TABLE IF EXISTS cutomers;')
cur.execute('CREATE TABLE if not exists customers (id serial PRIMARY KEY,'
                                 'name varchar (100) NOT NULL,'
                                 'address varchar (150) NOT NULL,'
                                 'city varchar(30) NOT NULL,'
                                 'state varchar(5),'
                                 'phone varchar(15));'
                                 )


cur.execute('INSERT INTO customers (name, address, city, state, phone) VALUES (%s, %s, %s, %s, %s)',('Zee','10 park st','Miami', 'FL','1231231234'))
'''


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    names = ["Adam", "John", "Jake"]
    return render_template("about.html", names=names)


@app.route("/admin")
def admin():
    return redirect(url_for("index"))

@app.route("/display", methods= ['GET'])
def display():
    conn = get_db_conn()
    # Open a cursor to perform database operations
    cur = conn.cursor()
    cur.execute("select * from customers")
    cust = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return render_template("display.html", cust = cust)


@app.route("/search", methods= ['GET', 'POST'])
def search():
    conn = get_db_conn()
    # Open a cursor to perform database operations
    cur = conn.cursor()
    searchName = "search name"

    if request.method == 'POST':
        searchName = request.form['name']
                        
        sql = 'SELECT * FROM customers WHERE name = %s'
        #return render_template("edit.html", sql=sql)
        
        #cur.execute(sql,[searchName])

        # cur.execute(sql, [searchName,])
        cur.execute('SELECT * FROM customers WHERE name = %s', [searchName,])

        searchrec = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        #return render_template("edit.html", =sql)
        return render_template("search.html", searchName = searchName, seachrec = searchrec )
        
    
    return render_template("search.html", searchName = searchName)



@app.route("/add/", methods = ['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        phone = request.form['phone']

        conn = get_db_conn()
        cur = conn.cursor()
        cur.execute('INSERT INTO customers (name, address, city, state, phone)'
                    'VALUES (%s, %s, %s, %s, %s)',
                    (name, address, city, state, phone))
        
        conn.commit()
        cur.close()
        conn.close()
        #return redirect(url_for('index'))
        return render_template("add.html", name = name)

    return render_template("add.html")


@app.route("/edit", methods = ['GET', 'POST'])
def edit():
    if request.method == 'POST':
        name = request.form['name']
        newname = request.form['newname']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        phone = request.form['phone']

        conn = get_db_conn()
        cur = conn.cursor()
        cur.execute('UPDATE customers SET name = %s WHERE name = %s ', [name, newname])
        
        conn.commit()
        cur.close()
        conn.close()
        return render_template('edit.html', name = name)

    return render_template("edit.html")


@app.route("/delete", methods = ['GET', 'POST'] )
def delete():
    conn = get_db_conn()
    # Open a cursor to perform database operations
    cur = conn.cursor()

    if request.method == 'POST':
        delName = request.form['name']
                        
        sql = "DELETE FROM CUSTOMERS WHERE NAME = %s"
               
        cur.execute(sql, [delName,])
        #searchrec = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return render_template("del.html", delName = delName )
          
    return render_template("del.html")


if __name__ == '__main__' :
   app.run(debug=True)

