from app import app, db
from app.models import User, Post, Tree
import sqlalchemy as sa
from sqlalchemy import insert
from sqlalchemy import update
from sqlalchemy import delete


app.app_context().push()

stmt = delete(Tree).where(Tree.name == 'Толик')

db.session.execute(stmt)

db.session.commit()
