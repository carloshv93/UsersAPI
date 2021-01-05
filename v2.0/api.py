from fastapi import FastAPI,Depends 
from sqlalchemy.orm import Session

from MVC.controllers import ControllerUser
from MVC.models import Base, User, UserSchema, UserRequestDelete,UserRequestLogin
from Utils.db_conn import engine, SessionLocal

controller = ControllerUser('./Utils/existing_users.json')
api = FastAPI() 
Base.metadata.create_all(engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@api.get('/')
def index():
   return ("Welcome!")

@api.get('/users')
def get_all(db: Session = Depends(get_db)):
    return controller.print_all(db)

@api.post('/user/')
def post_add_user(user:User, db: Session = Depends(get_db)):
    return controller.add_user(db,user) 

@api.delete('/user/')
def delete_user(username_request:UserRequestDelete,db: Session = Depends(get_db)):
    return controller.delete_user(db,username_request)

@api.post('/login/')
def login(credentials_request:UserRequestLogin):
    return controller.login(credentials_request)
