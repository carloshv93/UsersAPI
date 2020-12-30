from pydantic import BaseModel
from Utils.db import Base
from sqlalchemy import Column, String, create_engine

class File:
    def __init__(self,path,method):
        self._file = open(path,method)

    def __enter__(self):
        return self._file
        
    def __exit__(self, type, value, traceback):
        self._file.close()

class UserSchema(Base):
    __tablename__ = 'users'
    name = Column(String(20),nullable=False)
    username = Column(String(20), nullable=False, unique=True)
    email = Column(String(50),nullable=False, primary_key=True)
    password = Column(String(50),nullable=False)

class User(BaseModel):
    name: str
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True

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
