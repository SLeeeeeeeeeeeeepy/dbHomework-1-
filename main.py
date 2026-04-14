from sqlalchemy import create_engine , Column , Integer , String 
from sqlalchemy.orm import declarative_base , sessionmaker 

databas = create_engine("sqlite:///example.db") 
Base = declarative_base() 

with databas.connect() as conn:
    print("OK") 

class PRoduct(Base):
    __tablename__ = "products" 
    
    id = Column(Integer , primary_key=True) 
    title = Column(String , nullable=False) 
    price = Column(Integer) 

Base.metadata.create_all(databas) 
Session = sessionmaker(bind=databas) 
session = Session() 

p1 = PRoduct(title="Banana" , price=280)
p2 = PRoduct(title="Boeing 737" , price=9900000000)

session.add(p1) 
session.add(p2) 

session.commit() 

products = session.query(PRoduct).all() 

print("COUNT =" , session.query(PRoduct).count()) 

for i in products :
    print(i.id , i.title , i.price) 