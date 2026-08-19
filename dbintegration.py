'''Database Integration (sqlalchemy)
1. what is sqlalchemy
2. install sqlalchemy
3. setup db
4. model (table) create
5. table create in DB
6. connect fastapi with db'''

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi import FastAPI, Depends

app = FastAPI()

#specify a database url
DATABASE_URL = "sqlite:///./abc.db"

#create a db connection
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)

#handle operration in session db
SessionLocal = sessionmaker(bind=engine)

#baseclass of model table
Base = declarative_base()


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    completed = Column(String)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def  home(db:Session = Depends(get_db)):
    return{
        "message":"DB connected"
    }   