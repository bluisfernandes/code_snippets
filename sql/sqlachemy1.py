from sqlalchemy import create_engine, text, Column, String, Integer, Boolean,ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(
    'sqlite:///database.db',
    echo=True
)
Session =  sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    email = Column("email", String)
    passw = Column("passw", String)
    active = Column("active", Boolean)

    def __init__(self, name, email, passw, active=True):
        self.name = name
        self.email = email
        self.passw = passw
        self.active = active


class Book(Base):
    __tablename__ = "books"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    title = Column("title", String)
    pages = Column("pages", Integer)
    owner = Column("owner", ForeignKey("users.id"))

    def __init__(self, title, pages, owner):
        self.title = title
        self.pages = pages
        self.owner = owner


Base.metadata.create_all(bind=engine)


# CREATE
user = User(name="Robert", email="robert@gmail.com", passw='#$123321')
session.add(user)
session.commit()


# READ


# UPDATE


# DELETE