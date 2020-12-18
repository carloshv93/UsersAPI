import json
from MVC.   models import User, File

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

class ControllerUser:
    def __init__(self,path:str,current_user:User=None):
        self._file = ControllerFile(path)
        self._current_user = current_user # -> el current user tiene que ser de tipo User() , no es tener el print str del usuario es tener un obj usuario
        self._users = self.get_all()

    def print_all(self):
        users = json.loads(self._file.read())
        if self._current_user != None: users.append(self._current_user)
        return (users)

    def is_valid_user(self,user:User) -> bool:
        flag = True
        if not self.is_valid_username(user) or not self.is_valid_password(user) or not self.is_valid_email(user): flag = False
        return flag

    def is_valid_username(self,user:User) -> bool:
        flag = True
        if " " in user._username:
            flag = False
        return flag

    def is_valid_email(self,user:User) -> bool:
        flag = True
        if user._email.find("@") == -1:
            flag = False
        return flag

    def is_valid_password(self,user:User) -> bool:
        flag = True
        if not len(user._password)>=7:
            flag = False
        return flag

    def get_all(self) -> list:
        users = json.loads(self._file.read())
        if self._current_user != None: users.pop()
        users = [User(user['name'],user['username'],user['email'],user['password']) for user in users]
        return users

    def add_user(self,name:str, username:str, email:str, password:str):
        user = User(name,username,email,password)
        if user in self._users:
            return 'User already exists'
        else:               # this method is to big
            if self.is_valid_user(user):
                self._users.append(user)
                self._file.save(self.get_users_dict(self._users))
            else:
                return "Username or Password does not meet requirements"

    def get_user_by_username(self,username:str,users:list) -> User:
        user = None
        for _user in users:
            if _user._username == username:
                user = _user
        return user

    def delete_user(self,username:str):
        user = self.get_user_by_username(username,self._users)
        if user in self._users:
            self._users.remove(user) # this method is to big
            self._file.save(self.get_users_dict(self._users))
        else:
            return 'User does not exists'

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
        if user._password == password:
            result = True
        return result
        
    def get_users_dict(self,users:list) -> dict :
        _users = [
            user.__repr__() for user in users
        ]
        return _users

#######---------END----------####--------USER---------###########