#oAuth2 and JWT

'''
1. Secure routes
2. token validation
3. password hashing
'''


from fastapi import FastAPI, HTTPException, Depends
from jose import jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta, timezone
import bcrypt

app = FastAPI()

# JWT Config
SECRET_KEY = "mysecret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# OAuth Setup
oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

# Password helper functions
def hash_password(password: str) -> str:
    pwd_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pwd_bytes, salt).decode("utf-8")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

# Dummy user db
fake_user_db = {
    "admin": {
        "username": "admin",
        "hashed_password": hash_password("1234"),
    }
}

# Create Token
def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Login endpoint
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_user_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=400,
            detail="Invalid Username or Password"
        )
    access_token = create_token({"sub": form_data.username})
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

# Verify Token Dependency
def verify_token(token: str = Depends(oauth2_schema)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid Token")
        return username
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid Token")

# Protected route
@app.get("/protected")
def protected_route(username: str = Depends(verify_token)):
    return {
        "message": f"Hello {username}, you have access to this protected route!",
        "user": username,
    }