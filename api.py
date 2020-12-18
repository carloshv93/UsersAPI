from fastapi import FastAPI
from MVC.controllers import ControllerUser

controller = ControllerUser('./Utils/existing_users.json')
api = FastAPI() # exc este archivo

def main():
    pass

@api.get('/')
def index():
    return ("Welcome!")

@api.get('/users')
def get_all():
    return controller.print_all()

@api.post('/user/')
def post_add_user(name:str,username:str,email:str,password:str):
    return controller.add_user(name,username,email,password)

@api.delete('/user/')
def delete_user(username:str):
    return controller.delete_user(username)

@api.get('/login/')
def login(username:str,password:str):
    return controller.login(username,password)

if __name__ == '__main__':
    main()