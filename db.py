'''1. api call
2. run sql query
3.  save data to db or fetch data from db 
4. response '''


'''SQLALCHEMY is a orm (object relationship model) which is on top of 
sqlite
we have sqlite builtinto python but we need to install
sqlalchemy
we can handle sqlalchemy using python classes
when using any orm we can use the specific language to create 
queries (python code)
'''

import sqlite3
from fastapi import FastAPI

app = FastAPI()

#opens db
conn  = sqlite3.connect("test.db", check_same_thread=False)

#runs sql command
cursor = conn.cursor()

#runs query
cursor.execute("""
CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY,
        title TEXT,
        completed TEXT
    )
""")

#save changes to db
conn.commit()

@app.get("/")
def home():
    return{
        "message": "SQLite Connected"
    }