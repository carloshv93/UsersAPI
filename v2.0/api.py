from fastapi import FastAPI
from MVC.controllers import ControllerUser
from MVC.models import User, UserRequestDelete,UserRequestLogin

controller = ControllerUser('./Utils/existing_users.json')
api = FastAPI() 

def main():
    pass

@api.get('/')
def index():
    return ("Welcome!")

@api.get('/users')
def get_all():
    return controller.print_all()

@api.post('/user/')
def post_add_user(user:User):
    return controller.add_user(user) 

@api.delete('/user/')
def delete_user(username_request:UserRequestDelete):
    return controller.delete_user(username_request)

@api.post('/login/')
def login(credentials_request:UserRequestLogin):
    return controller.login(credentials_request)

if __name__ == '__main__':
    main()