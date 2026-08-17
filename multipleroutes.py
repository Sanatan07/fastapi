#multiple routes, dynamic routes and path parameter
from fastapi import FastAPI

app = FastAPI()

#Home Route
@app.get("/")
def home():
    return {"message":"Welcome to FastAPI"}

#About Route
@app.get("/about")
def about():
    return{"message":"This is About Page"}

#Users Route
@app.get("/users/{user_id}")
def get_users(user_id:int):
    return{
        "user_id":user_id
    }

#



