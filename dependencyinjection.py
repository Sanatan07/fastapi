#dependency injection
'''1. What is depends()
2. reusable logic
3. auth example intro'''

#dependency injection is a design pattern which is provided to the function dependency from an external source
#depends method is used to call a function automatically and its result is injected in the api function
'''real use case of dependency injection
1. access authorization
2. connect database
3. logging
4. reuse logic
5. in an auth system depends method is used to verify token and
make secure endpoint '''

from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()

def verify_token(token:str = Header(None)):
    if token != "mysecrettoken":
        raise HTTPException(
            status_code = 401,
            detail = "Unauthorized"
        )
    return{
        "user":"Authorized User"
    }

@app.get("/secure-data")
def secure_data(user=Depends(verify_token)):
    return{
        "message":"Secure Data Accessed",
        "user":user
    }

def common_logic():
    return{
        "message":"Common Logic Executed"
    }

@app.get("/home")
def home(data = Depends(common_logic)):
    return data


def get_current_user():
    return{
        "user":"Mohit"
    }

@app.get("/profile")
def profile(user = Depends(get_current_user)):
    return user

@app.get("/dashboard")
def profile(user = Depends(get_current_user)):
    return user