#third party api integration

'''
1. what is external api
2. install requests
3. basic api call
4. single data fetch
5. fastapi integration
'''


#get data directly using python
'''

import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")
data = response.json()
print(data[:2])

'''

#get data with id
'''

import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
data = response.json()
print(data[])

'''

#get data with fastapi

from fastapi import FastAPI
import requests

app = FastAPI()

#get all data
@app.get("/posts")
def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts/"
    response = requests.get(url)
    return response.json()


@app.get("/posts/{post_id}")
def get_posts(post_id:int):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url)
    return response.json()

