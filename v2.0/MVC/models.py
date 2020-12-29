from pydantic import BaseModel
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base  


if __name__ == '__main__':
    engine = create_engine('mysql://root:O9oiopo9oiopo!@localhost:3306/tiims')
    Base = declarative_base()
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()


class File:
    def __init__(self,path,method):
        self._file = open(path,method)

    def __enter__(self):
        return self._file
        
    def __exit__(self, type, value, traceback):
        self._file.close()
class User(Base):
    __tablename__ = 'users'
    name = Column(String(20),nullable=False)
    username = Column(String(20), nullable=False, unique=True)
    email = Column(String(50),nullable=False, primary_key=True)
    password = Column(String(50),nullable=False)

    def __repr__(self):
        return {"name":self.name,"username":self.username,"email":self.email,"password":self.password}

    def update(self,user):
        self.name = user.name
        self.username = user.username
        self.email = user.email
        self.password = user.password

class UserRequestDelete(BaseModel):
    username:str

class UserRequestLogin(BaseModel):
    username:str
    password:str
