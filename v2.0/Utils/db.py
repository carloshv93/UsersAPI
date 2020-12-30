from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root:this-is-a-very-strong-password@localhost:3306/usersAPI')
SessionLocal = sessionmaker(engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  