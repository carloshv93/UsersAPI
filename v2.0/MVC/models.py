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
        return {"name":self._name,"username":self._username,"email":self._email,"password":self._password}

    def update(self,user):
        self._name = user.name
        self._username = user.username
        self._email = user.email
        self._password = user.password