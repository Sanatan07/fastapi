#Authentication Basics

'''
1. jwt intro - json web token is generated when a user login
this token has all the information about the user, users secret
signature, and users token, the server verifies this token on 
every request sent by the user, based on this token the server
gets to know what all permissions are given to the user
and what all things the user can use in the application

the token is as Authorization: Bearer "token-value"
the token contains 1. header - what type of hashing technique we
are using
2. payload - the information regarding the user, token expiry
3. signature - type of cryptographic algorithm used is in this
signature

the login flow is as follows 
#a login (username and password)
#b validate credentials
#c create and sign token
#d send token
#e store token
#f get user info
#g validate token on each request
#h send data (if user is authorized )

2. token based auth - 
3. login api - '''

#jose - Javascript object signature and encryption
# it is a standard which is used to securely signup and encrypt json data through jwt

from datetime import datetime, timedelta, timezone
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt

app = FastAPI()

SECRET_KEY = "MYSECRET"
ALGORITHM = "HS256"

# Enables the Swagger UI "Authorize" button and parses Bearer tokens
security = HTTPBearer()


def create_token(data: dict):
  to_encode = data.copy()
  expire = datetime.now(timezone.utc) + timedelta(minutes=30)
  to_encode.update({"exp": expire})
  return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


@app.post("/login")
def login(username: str, password: str):
  if username != "admin" or password != "1234":
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
    )
  token = create_token({"sub": username})
  return {"access_token": token, "token_type": "bearer"}


def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
  token = credentials.credentials  # Extracts the raw token string from "Bearer <token>"
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload
  except JWTError:
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired Token",
    )


@app.get("/secure")
def secure_data(user: dict = Depends(verify_token)):
  return {"message": "Secure Data Accessed", "user": user}