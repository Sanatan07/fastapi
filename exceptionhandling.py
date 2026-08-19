#exception handling
'''1. HTTPException
2. custom exceptions
3. global error handler
'''

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

class UserNotFoundException(Exception):
    def __init__(self, name:str):
        self.name=name

@app.exception_handler(UserNotFoundException)
def user_not_found_handler(request:Request, exec:UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "status":"error",
            "message":f"User {exec.name} not found"
        }
    )

@app.get("/user/{name}")
def get_users(name:str):
    if name!="mohit":
        raise UserNotFoundException(name)
    return{
        "name":name
    }

@app.get("/users/{user_id}")
def get_user(user_id:int):
    if user_id !=1:
        raise HTTPException(
            status_code=404,
            detail="User Not Found"
        )
    return{
        "id":1,
        "name":"Mohit"
    }