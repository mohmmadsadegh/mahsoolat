from sqlalchemy import create_engine, String, Integer, Column, Table, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

engine = create_engine("sqlite:///mahsool4.db", echo=True) 
Base = declarative_base()
Session = sessionmaker(engine)
session1 = Session()

mahsol_human = Table("mahsool_human", Base.metadata,
                   #Column("id", Integer, primary_key=True),
                   Column("human_id", Integer, ForeignKey("human.id")),
                   Column("mahsool_id", Integer, ForeignKey("mahsool.id"))
                   )

class human(Base):
    __tablename__ = "human"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    famili = Column(String)
    mahsool = relationship("mahsool", secondary=mahsol_human,
                           back_populates="human")
    
    def __init__(self, name, famili):
        self.name = name
        self.famili = famili


class mahsool(Base):
    __tablename__ = "mahsool"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    ghimat = Column(String)
    tedad = Column(Integer)
    human = relationship("human", secondary=mahsol_human,
                         back_populates="mahsool")
    
    def __init__(self, name, ghimat, tedad):
        self.name = name
        self.ghimat = ghimat
        self.tedad = tedad
        
        
class Repisitory():
    def Add(self, obj):
        session1.add(obj)
        session1.commit()
        return True
    
    def Select_all(self, obj):
        result = session1.query(obj).order_by(obj.id.desc()).limit(3).all()
        return result
    
    def Select_by_id(self, id, obj):
        result = session1.query(obj).filter(obj.id==id).first()
        return result
    
    def Show_obj(self, list, index):
        for item in list:
            atr=getattr(item, index)   
            print(atr)   
            
    def update(self, id, obj, **kwargs):
        record = self.Select_by_id(id,obj)
        for key, value in kwargs.items():
            setattr(record, key, value)
        session1.commit()
        return True
        
    def delete(self,id,obj):        
        record=self.Select_by_id(id,obj)

        session1.delete(record)
        session1.commit()
        return True


Base.metadata.create_all(engine)
repository = Repisitory()
humans1 = human("ali", "moradi")
#session1.add(humans1)
mahsool1=mahsool("apple watch",252,1)
#humans1.mahsool.append(mahsool1)
session1.commit()
#repository.update(4,mahsool,name="teshert",ghimat=150,tedad=2)
#repository.delete(1,human)