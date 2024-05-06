from flask import Flask
from app import db
from app.models import User, Post
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')

db = SQLAlchemy(app)

with app.app_context():
    # u = db.session.get(User, 1)
    # posts = db.session.query(Post.body).all()
    # res = u.posts
    # for i in res:
    #     print(i)


    # u = db.session.get(User, 1)
    # p = Post(body='hello!', author=u)
    # db.session.add(p)
    # db.session.commit()




    # u = db.session.get(User, 1)
    # print(u)


   # u = db.session.query(User).all()
   # for i in u:
   #     print(i.id, i.username)



    u = User(username='qwerty', email='qwerty@example.com')
    db.session.add(u)
    db.session.commit()


    # users = db.session.query(User).all()
    # for i in users:
    #     db.session.delete(i)
    #     db.session.commit()


    # posts = db.session.query(Post).all()
    # for i in posts:
    #     print(i.id, i.author.username, i.body)

