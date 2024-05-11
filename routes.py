from app import app
from flask import Flask, render_template
import mysql.connector


db = mysql.connector.connect(
   host="localhost",
   user="cubinez85",
   password="123",
   database="testdb"
)

cursor = db.cursor()

@app.route('/')
def index():

    cursor.execute(
"select u.id, u.username, u.email, p.body, p.timestamp from user u join post p on u.id = p.user_id order by p.body, p.timestamp"

)
    content = cursor.fetchall()
    cursor.execute(
"select u.id, u.username, u.email, p.body, p.timestamp from user u join post p on u.id = p.user_id order by p.body, p.timestamp"

)
    labels = cursor.fetchall()
    labels = list(map(lambda x: x[0], cursor.description))

    return render_template('index.html', labels=labels, content=content)

  
