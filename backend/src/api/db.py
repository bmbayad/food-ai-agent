


import os

import time

import sqlmodel
from sqlmodel import Session, SQLModel

 


DATABASE_URL = os.environ.get("DATABASE_URL")


if DATABASE_URL is None:
    raise NotImplementedError("`DATABASE_URL` environment variable is not set")


engine = sqlmodel.create_engine(DATABASE_URL)


#dabase models
def init_db():
    
    print("creating database tables...")
    time.sleep(20) #wait for database to be ready 20 seconds
    SQLModel.metadata.create_all(engine)

def get_session():
    print("creating database session...")
    with Session(engine) as session:
        yield session
        