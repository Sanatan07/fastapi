#async programming
'''
async prog is a non blocking approach where we can 
execute multiple tasks continuously


1. async/await - define async function and await is used to complete the function without blocking 
2. why async matters -  to run multiple tasks together
3. performance benefits - fast application, better scalability, 
'''

import time
import asyncio
from fastapi import FastAPI

app = FastAPI()

'''
sync programming
def task ():
    time.sleep(3)
    return "Done"
'''

'''
async programming
async def task():
    await asyncio.sleep(3)
    return "Done"
'''

@app.get("/")
async def home():
    await asyncio.sleep(3)
    return {
        "message" : "Async API"
    }

