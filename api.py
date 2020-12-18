from fastapi import FastAPI
from controller_user import ControllerUser

controller = ControllerUser('existing_users.json')
api = FastAPI()

@api.get('/')
def index():
    return ("Welcome!")

@api.get('/users')
def get_all_users():
    return controller.print_all_users()

@api.post('/user/')
def post_add_user(name:str,username:str,email:str,password:str):
    return controller.add_user(name,username,email,password)

@api.delete('/user/')
def delete_user(username:str):
    return controller.delete_user(username)

@api.get('/login/')
def login(username:str,password:str):
    return controller.login(username,password)
