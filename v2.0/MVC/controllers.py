import json
from pydantic import BaseModel
from sqlalchemy.orm import Session
from Utils.db_conn import SessionLocal
from MVC.models import User, UserSchema , UserRequestDelete, UserRequestLogin
from Utils.middleware_dabatase import MiddlewareDatabase

class ControllerUser():
    def __init__(self,path:str,current_user:User=None):
        self._current_user = current_user
        self._users = self.get_all(SessionLocal())

    def print_all(self,db: Session) -> list:
        users = self.get_all(db)
        if self._current_user != None: users.append(self._current_user)
        return (users)

    def is_valid_user(self,user:User) -> bool:
        flag = True
        if not self.is_valid_username(user) or not self.is_valid_password(user) or not self.is_valid_email(user):
            flag = False
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

    def get_all(self,db) -> list:
        users = MiddlewareDatabase.get_all_users(db)
        if self._current_user != None: users.pop()
        return users

    def add_user(self,db: Session, user:User):
        if self.exist(user):
            return 'Username already exists'
        else:
            if self.is_valid_user(user):
                return self.save_user(db,user)
            else:
                return "Username or Password does not meet requirements"
    
    def exist(self,user:User):
        True if self.get_user_by_username(user.username,self._users) != None else False
            

    def save_user(self,db: Session, user:User):
        self._users.append(user)
        MiddlewareDatabase.save_users(db,user)
        return 'User added'

    def get_user_by_username(self,username:str,users:list) -> User:
        user = None
        for _user in users:
            if _user.username == username:
                user = _user
        return user

    def delete_user(self,db:Session,username_request:UserRequestDelete):
        user = self.get_user_by_username(username_request.username,self._users)
        if user in self._users:
            MiddlewareDatabase.delete_user(db,user)
        else:
            return 'User does not exists'

    def login(self,user_request:UserRequestLogin):
        user = self.get_user_by_username(user_request.username,self._users)
        if user in self._users:
            if (self.check_password(user,user_request.password)):
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