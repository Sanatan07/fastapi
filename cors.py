#cors handling

'''1. what is cors -  it is a browser security rule when frontend and backend are on 
different port/url, so the browser blocks it until backend gives permission to connect
to the frontend application
eg. frontend on localhost:3000  and backend on localhost:5000 browser will block it until 
we allow cors in backend that the frontend is authorized api can be used on this frontend
2. enable in fastapi
3. frontend reactjs connection
'''

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allowed Origins (no trailing slashes)
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "Cors enabled api"
    }