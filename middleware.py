'''A middleware is a function or layer that sits between an incoming HTTP request and the final route handler (endpoint) in a web application.

It intercepts every request before it reaches your route code, and intercepts the response before it goes back to the client.



Client Request ──► [ Middleware 1 ] ──► [ Middleware 2 ] ──► Route Handler (main.py)
                                                                    │
Client ◄────────── [ Middleware 1 ] ◄── [ Middleware 2 ] ◄──────────┘



What Middleware Can Do
Inspect & Modify Requests: Read headers, parse auth tokens, reject invalid requests before hitting your business logic.

Inspect & Modify Responses: Inject custom headers, compress payload data (GZip), track execution duration.

Short-circuit Execution: Return early (e.g., return a 401 Unauthorized without calling the route).'''


from fastapi import FastAPI, Request
import time

app = FastAPI()

#logging middleware
@app.middleware("http")
async def log_middleware(request:Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time()-start_time
    print(f"Path:{request.url.path} | Time:{process_time}")
    return response


@app.middleware("http")
async def my_middleware(request:Request, call_next):
    print("Request Received")

    response = await call_next(request)

    print("Response Sent")
    return response


