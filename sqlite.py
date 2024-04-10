from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()



#connection.commit()

#connection.close()

@app.route('/')
def index():

    cursor.execute("select * from Users")
    data = cursor.fetchall()

    return render_template('db.html', data = data)



if __name__ == "__main__":
    app.run(debug=True)
