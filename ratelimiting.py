#rate limiting

'''
1. what is ratelimiting
2. using slowapi library
3. fastapi integration
4. testing
'''
from fastapi import FastAPI, Request, HTTPException
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse

app = FastAPI()

#limiter setup

limiter = Limiter(key_func = get_remote_address)
app.state.limiter = limiter

#error handler
@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code = 429,
        content = {
            "detail" :"Too many requests"
        }
    )


#rate limiter api

@app.get("/data")
@limiter.limit("5/minute")
def get_data(request:Request):
    return{
        "message":"Success"
    }