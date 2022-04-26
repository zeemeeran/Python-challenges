
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
    
    if request.method == 'POST':
        searchName = request.form['name']

        if searchName:                        
            conn = get_db_conn()
            # Open a cursor to perform database operations
            cur = conn.cursor()
            
            cur.execute('SELECT * FROM customers WHERE name = %s', [searchName,])

            searchrec = cur.fetchall()
            conn.commit()
            cur.close()
            conn.close()
            if searchrec :
                return render_template("search.html", searchName = searchName, searchrec = searchrec )
            else :
                return render_template("search.html", searchName = searchName, notfoundmsg = 1 )
        else :
            return render_template("search.html", nonamemsg = 1)
        
    return render_template("search.html", searchName = "Search Name")



@app.route("/add/", methods = ['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        phone = request.form['phone']

        if name != "" :
            conn = get_db_conn()
            cur = conn.cursor()
            cur.execute('INSERT INTO customers (name, address, city, state, phone)'
                        'VALUES (%s, %s, %s, %s, %s)',
                        (name, address, city, state, phone))
            
            conn.commit()
            cur.close()
            conn.close()
            return render_template("add.html", name = name)
        else :
            return render_template("add.html", nonamemsg = 1 )
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

        if name != "" :
            
            if newname == "" and address == "" and city == "" and state == "" and phone == "" :
                return render_template("edit.html", noeditmsg = 1, name = name)
            else :
                notfoundmsg = 1
                conn = get_db_conn()
                cur = conn.cursor()
                cur.execute('select * from customers where name = %s ', (name, ))
                cust = cur.fetchall()
                
                if len(cust) != 0 :
                    notfoundmsg = 0
                    if newname != "":
                        cur.execute('UPDATE customers SET name = %s WHERE name = %s ', (newname, name))

                    if address != "":
                        cur.execute('UPDATE customers SET address = %s WHERE name = %s ', (address, name))
                    
                    if city != "":
                        cur.execute('UPDATE customers SET city = %s WHERE name = %s ', (city, name))

                    if state != "":
                        cur.execute('UPDATE customers SET state = %s WHERE name = %s ', (state, name))

                    if phone != "":
                        cur.execute('UPDATE customers SET phone = %s WHERE name = %s ', (phone, name))
                    
                conn.commit()
                cur.close()
                conn.close()
                return render_template('edit.html', notfoundmsg = notfoundmsg, name = name)
        else :
            return render_template("edit.html", name = "Edit Customer Name", nonamemsg = 1)

    return render_template("edit.html", name = "Edit Customer Name")


@app.route("/delete", methods = ['GET', 'POST'] )
def delete():
    if request.method == 'POST':
        delName = request.form['name']
        
        if delName :
            conn = get_db_conn()
            cur = conn.cursor()
            cur.execute('select * from customers where name = %s ', (delName, ))
            cust = cur.fetchall()
            notfoundmsg = 1        

            if len(cust) !=  0 :
                notfoundmsg = 0
                sql = "DELETE FROM CUSTOMERS WHERE NAME = %s"
                cur.execute(sql, [delName,])
            
            conn.commit()
            cur.close()
            conn.close()
            return render_template("del.html", notfoundmsg = notfoundmsg, delName = delName )
        else :
            return render_template("del.html", nonamemsg = 1)
                    
    return render_template("del.html", delName = "delete customer")


if __name__ == '__main__' :
   app.run(debug=True)

