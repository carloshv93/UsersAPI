from pydantic import BaseModel

class File:
    def __init__(self,path,method):
        self._file = open(path,method)

    def __enter__(self):
        return self._file
        
    def __exit__(self, type, value, traceback):
        self._file.close()

class User(BaseModel):
    name: str
    username: str
    email:str
    password:str

    def __repr__(self):
        return {"name":self.name,"username":self.username,"email":self.email,"password":self.password}

    def update(self,user):
        self.name = user.name
        self.username = user.username
        self.email = user.email
        self.password = user.password

class UserRequestDelete(BaseModel):
    username:str