#testing api
#use test_main.py for api testing with pytest
'''1. why testing
2. install pytest
3. pytest + fastapi
4. test endpoints'''


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message":"Hello Mohit"
    }

@app.get("/add")
def add(a:int, b:int):
    return{
        "result":a+b
    }