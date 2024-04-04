from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import DeclarativeBase

app = Flask(__name__)

mysql_database = 'mysql://cubinez85:123@localhost/testdb'

engine = create_engine(mysql_database)

class Base(DeclarativeBase): pass

class Person(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), unique=True, index=True)
    age = Column(String(128))

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_db()
    app.run(debug=True)
