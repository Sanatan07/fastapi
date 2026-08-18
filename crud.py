from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id:int
    title:str
    completed:bool

#create api
@app.post("/todos")
def create_todo(todo:Todo):
    todos.append(todo)
    return{
        "message":"Todo Added",
        "data":todo
    }

#read api
@app.get("/todos")
def get_todo():
    return todos

#read single todo api
@app.get("/todos/{todo_id}")
def get_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {
        "error": "Todo Not Found"
    }


#update api
@app.put("/todos/{todo_id}")
def update_todo(todo_id:int, update_todo:Todo):
    for index,todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = update_todo
            return{
                "message":"Updated Todo",
                "data":update_todo
            }
    return{
        "error":"Todo not found"
    }


#delete api
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"message":"Data Deleted"}