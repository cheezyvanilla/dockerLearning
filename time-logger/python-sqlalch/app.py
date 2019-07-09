from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time
Base = declarative_base()
class data1(Base):
	__tablename__ = "docker2"
	id = Column(Integer, primary_key=True)
	time = Column(String)
	def __init__(self, time):
		self.time = time

connection_str = 'mysql+pymysql://root:@localhost:3306/latihan'
engine = create_engine(connection_str)

Session = sessionmaker(bind= engine)
session = Session()
while(1):	
	a = time.ctime()
	rn = data1(a)
	session.add(rn)
	session.commit()
	time.sleep(10)
session.close()

