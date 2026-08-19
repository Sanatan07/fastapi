# path + query + body

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#/users/101 - path parameter
#nitify=true - query parameter
#PUT /users/101?notify=true
''' this is the request body with the path
{
    "name" : "Sanatan"
    "age" : 25
}
'''

user = []
class User(BaseModel):
    name:str
    age:int


@app.post("/users")
def create_user(users:User):
    users.append(user)
    return{
        "message":"User Created",
        "data":user
    }

@app.put("/users/{user_id}")
def updated_user(user_id:int, users:User, notify:bool=False):
    if user_id < len(users):
        users[user_id]=user
        return{
            "message":"User Updated",
            "notify":notify,
            "data":user
        }
    return{
        "error":"User not found"
    }