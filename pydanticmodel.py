''' pydantic model is a schema structure '''

from fastapi import FastAPI
from pydantic import BaseModel

app =FastAPI()

#nested pydantic model
class User(BaseModel):
    name:str
    age:int
    email:str
    address:Address

class Address(BaseModel):
    city:str
    pincode:int


@app.post("/create-user")
def create_user(user:User):
    return{
        "message": "User Created",
        "data":user
    }