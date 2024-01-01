import time

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import os

db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data/database.db")
print(db_path)
if not os.path.exists("data"):
    os.mkdir("data")
if not os.path.exists("data/database.db"):
    open(db_path, "w").close()

engine = create_engine("sqlite:///" + db_path, echo=True)

Base = declarative_base()

Session = sessionmaker(bind=engine)

print(time.time())


class User(Base):
    __tablename__ = "users"

    uid = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    is_verified = Column(Integer)
    is_active = Column(Integer)

    level = Column(Integer)
    own_net_number = Column(String)
    create_time = Column(String)
    lsat_login_time = Column(String)
    password = Column(String)


class ztnode(Base):
    __tablename__ = "ztnode"

    node_id = Column(String, primary_key=True)
    node_name = Column(String)
    node_owner_id = Column(String)
    node_ip = Column(String)
    node_token = Column(String)
    node_location = Column(String)
    node_create_time = Column(String)
    node_status = Column(Integer)


class network(Base):
    __tablename__ = "network"

    network_id = Column(String, primary_key=True)
    network_name = Column(String)
    network_owner_id = Column(String)
    network_create_time = Column(String)
    network_status = Column(Integer)
    network_member_list = Column(String)


Base.metadata.create_all(engine)
