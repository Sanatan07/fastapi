'''Database Integration (sqlalchemy)
1. what is sqlalchemy
2. install sqlalchemy
3. setup db
4. model (table) create
5. table create in DB
6. connect fastapi with db'''

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

#specify a database url
DATABASE_URL = "sqlite:///./crudwithdb.db"

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

#create api
@app.post("/todos")
def create_todo(title:str, db:Session = Depends(get_db)):
    todo = Todo(title = title, completed = "False")
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return{
        "message":"Todo Created",
        "data":todo
    }
#read all data
@app.get("/todos")
def get_todos(db:Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return{
        "Total":len(todos),
        "data":todos
    }


@app.get("/todos/{todo_id}")
def get_todo(todo_id = int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code = 404, detail = "Todo not found")
    return todo