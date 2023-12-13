import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///data/database.db", echo=True)

Base = declarative_base()

Session = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)

    password = Column(String)

    def __repr__(self):
        return "<User(username='%s', password='%s')>" % (self.username, self.password)
Session.
