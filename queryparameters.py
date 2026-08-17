#query parameters and optional parameters

#query parameters are the extra data in the end of the url
#/users?name=mohit
#/products?price=1000
#the query after ? is known as query parameter

#the example of query parameter is amazon filtering the filtering is done on the basis of query parameters

from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def get_users(name:str = None):
    return{"Name":name}

@app.get("/products")
def get_products(limit:int = None):
    return{"limit":limit}

@app.get("/items")
def get_products(name:str = None, price:int=0):
    return{
        "Name":name,
        "Price":price
        }