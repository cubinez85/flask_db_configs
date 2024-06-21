from app import app, db
from app.models import User, Post, Tree
import sqlalchemy as sa
from sqlalchemy import insert
from sqlalchemy import update

app.app_context().push()

db.session.execute(
    update(Tree),
    [
        {'id': 3, 'parent': 1, 'name': 'Толик', 'position': 'HR'},
       # {'parent': 3, 'name': 'Петя', 'position': 'продавец'},





    ],
)

db.session.commit()
