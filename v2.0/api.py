from fastapi import FastAPI,Depends 
from sqlalchemy.orm import Session

from MVC.controllers import ControllerUser
from MVC.models import User, UserRequestDelete,UserRequestLogin
from Utils.db import get_db, Base, engine
from Utils.middleware import get_users

controller = ControllerUser('./Utils/existing_users.json')
api = FastAPI() 
Base.metadata.create_all(engine)


@api.get('/')
def index():
    return ("Welcome!")

@api.get('/users')
def get_all():
    return get_users(db:sqlalchemy.orm.Session = Depends(get_db))

@api.post('/user/')
def post_add_user(user:User):
    return controller.add_user(user) 

@api.delete('/user/')
def delete_user(username_request:UserRequestDelete):
    return controller.delete_user(username_request)

@api.post('/login/')
def login(credentials_request:UserRequestLogin):
    return controller.login(credentials_request)