from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
   host="localhost",
   user="cubinez85",
   password="123",
   database="testdb"
)

cursor = db.cursor()

@app.route('/')
def index():

    cursor.execute("select * from tree")
    content = cursor.fetchall()
    cursor.execute("select * from tree")
    labels = cursor.fetchall()
    labels = list(map(lambda x: x[0], cursor.description))

    return render_template('sqlite.html', labels=labels, content=content)

@app.route('/sale')
def sale():

    cursor.execute("select * from tree where parent in (2, 5)")
    content = cursor.fetchall()
    cursor.execute("select * from tree")
    labels = cursor.fetchall()
    labels = list(map(lambda x: x[0], cursor.description))

    return render_template('sqlite_sale.html', labels=labels, content=content)

@app.route('/support')
def support():

    cursor.execute("select * from tree where parent in (3, 6)")
    content = cursor.fetchall()
    cursor.execute("select * from tree")
    labels = cursor.fetchall()
    labels = list(map(lambda x: x[0], cursor.description))

    return render_template('sqlite_support.html', labels=labels, content=content)

@app.route('/IT')
def IT():

    cursor.execute("select * from tree where parent in (4, 7)")
    content = cursor.fetchall()
    cursor.execute("select * from tree")
    labels = cursor.fetchall()
    labels = list(map(lambda x: x[0], cursor.description))

    return render_template('sqlite_IT.html', labels=labels, content=content)



if __name__ == '__main__':
    app.run()

