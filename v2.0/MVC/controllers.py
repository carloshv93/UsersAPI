import json
from MVC.models import User, File,UserRequestDelete
from pydantic import BaseModel

class ControllerFile:
    def __init__(self,path:str):
        self._path = path
        with File(self._path,'r') as _:
            self.content = _.read()
            
    def read(self):
        with File(self._path,"r") as _:
            return _.read()

    def save(self,data):
        self.write(data)
        with File(self._path,"w") as _: 
            _.write(json.dumps(self._content)) 

    def write(self,data):
        self._content = data

#######---------END----------####--------FILE---------###########

class ControllerUser():
    def __init__(self,path:str,current_user:User=None):
        self._file = ControllerFile(path)
        self._current_user = current_user
        self._users = self.get_all()

    def print_all(self) -> list:
        users = json.loads(self._file.read())
        if self._current_user != None: users.append(self._current_user)
        return (users)

    def is_valid_user(self,user:User) -> bool:
        flag = True
        if not self.is_valid_username(user) or not self.is_valid_password(user) or not self.is_valid_email(user): flag = False
        return flag

    def is_valid_username(self,user:User) -> bool:
        flag = True
        if " " in user.username:
            flag = False
        return flag

    def is_valid_email(self,user:User) -> bool:
        flag = True
        if user.email.find("@") == -1:
            flag = False
        return flag

    def is_valid_password(self,user:User) -> bool:
        flag = True
        if not len(user.password)>=7:
            flag = False
        return flag

    def get_all(self) -> list:
        users = json.loads(self._file.read())
        if self._current_user != None: users.pop()
        users = [User(name=user['name'],username=user['username'],email=user['email'],password=user['password']) for user in users]
        return users

    def add_user(self,user:User):
        if user in self._users:
            return 'User already exists'
        else:
            if self.is_valid_user(user):
                self._users.append(user)
                self.saveFile()
            else:
                return "Username or Password does not meet requirements"

    def get_user_by_username(self,username:str,users:list) -> User:
        user = None
        for _user in users:
            if _user.username == username:
                user = _user
        return user

    def delete_user(self,username_request:UserRequestDelete):
        user = self.get_user_by_username(username_request.username,self._users)
        if user in self._users:
            self._users.remove(user)
            self.saveFile()
        else:
            return 'User does not exists'
            
    def saveFile(self, content:str=None):
        if content == None:
            content = self.get_users_dict(self._users)
        self._file.save(content)

    def login(self,username:str,password:str):
        user = self.get_user_by_username(username,self._users)
        if user in self._users:
            if (self.check_password(user,password)):
               self._current_user = user
               result = "login sucess"
            else:
                result = "wrong password"
        else:
            result = "User does not exists"
        return result
        
    def check_password(self,user:User,password:str) -> str:
        result = False
        if user.password == password:
            result = True
        return result
        
    def get_users_dict(self,users:list) -> dict :
        _users = [
            user.__repr__() for user in users
        ]
        return _users

#######---------END----------####--------USER---------###########