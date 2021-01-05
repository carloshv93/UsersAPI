from sqlalchemy.orm import Session
from MVC.models import UserSchema, User
class MiddlewareDatabase():
    @staticmethod
    def delete_user(db: Session,user:User):
        user = UserSchema(name= user.name, username= user.username, email= user.email, password= user.password)
        db.delete(user)
        db.commit()

    @staticmethod
    def get_all_users(db: Session):
        users = db.query(UserSchema).all()
        return users
    
    @staticmethod
    def save_users(db: Session,user: User):
        user = UserSchema(name= user.name, username= user.username, email= user.email, password= user.password)
        db.add(user)
        db.commit()
