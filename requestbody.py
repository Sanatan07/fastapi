'''request body is the data that the client sends to the backend
for eg. when a users fills login id like email password and clicks login this dataa is sent to the backend
backend handles this data in terms of request body'''

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name:str
    age:int

#send data in query format
@app.post("/create-user")
def create_user(name:str,age:int):
    return{
        "Name":name,
        "Age":age
    }

#send data in form of json
@app.post("/create-pydantic-user")
def create_pydantic_user(user:User):
    return{
        "message":"User Created",
        "data":user
    }

#when we send data in json format the data is not validated, so we use pydantic
'''using pydantic we can validate data and define data structure'''
