from model_user import User
from controller_file import ControllerFile
import json

class ControllerUser:
    def __init__(self,path:str,current_user:User=None):
        self._file = ControllerFile(path)
        self._current_user = current_user

    def print_all_users(self):
        users = json.loads(self._file.read())
        if self._current_user != None: users.append(self._current_user)
        return (users)

    def validateUser(self,user:User) -> bool:
        flag = True
        if not self.validateUsername(user) or not self.validatePassword(user) or not self.validateEmail(user): flag = False
        return flag

    def validateUsername(self,user:User) -> bool:
        flag = True
        if " " in user._username:
            flag = False
        return flag

    def validateEmail(self,user:User) -> bool:
        flag = True
        if user._email.find("@") == -1:
            flag = False
        return flag

    def validatePassword(self,user:User) -> bool:
        flag = True
        if not len(user._password)>=7:
            flag = False
        return flag

    def get_all_users(self) -> list:
        users = json.loads(self._file.read())
        if self._current_user != None: users.pop()
        users = [
            User(user['name'],user['username'],user['email'],user['password']) for user in users]
        return users

    def add_user(self,name:str, username:str, email:str, password:str):
        users = self.get_all_users()
        user = User(name,username,email,password)
        if user in users:
            return 'User already exists'
        else:
            user = User(name,username,email,password)
            if self.validateUser(user):
                users.append(user)
                self._file.save(self.get_users_dict(users))
            else:
                return "Username or Password does not meet requirements"

    def get_user_by_username(self,username:str,users:list) -> User:
        user = None
        for _user in users:
            if _user._username == username:
                user = _user
        return user

    def delete_user(self,username:str):
        users = self.get_all_users()
        user = self.get_user_by_username(username,users)
        if user in users:
            users.remove(user)
            self._file.save(self.get_users_dict(users))
        else:
            return 'User does not exists'

    def login(self,username:str,password:str):
        result = ''
        users = self.get_all_users()
        user = self.get_user_by_username(username,users)
        if user in users:
            if user._password == password:
                self._current_user = user
                result = "login success"
            else:
                result = 'password wrong'
        else:
           result = "User does not exists"
        return result

    def get_users_dict(self,users:list) -> dict :
        _users = [
            user.__repr__() for user in users
        ]
        return _users