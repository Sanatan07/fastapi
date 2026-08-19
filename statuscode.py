#status codes and responses

'''1. Http status codes
2. custom responses
3. error handling basics
'''

from fastapi import FastAPI, status, HTTPException

app = FastAPI()

#sending status codes
@app.post("/create_user", status_code=status.HTTP_201_CREATED)
def create_user():
    return{
        "message":"User Created"
    }

#sending custom response
@app.get("/user")
def get_users():
    return{
        "status":"Success",
        "message":"User Fetched",
        "data":{
            "name":"Mohit",
            "age":24
        }
    }

#error handling using HTTPException

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