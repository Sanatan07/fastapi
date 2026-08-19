'''1. response validation
2. hide sensitive data
3. output formatting
'''

#response model is the data that we need to send to the client

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name:str
    age:int
    password:str

class UserResponse(BaseModel):
    name:str
    age:int

@app.get("/user", response_model=UserResponse)
def get_user():
    return{
        "name":"Mohit",
        "age":24,
        "password":"123456"
    }