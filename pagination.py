#pagination 

'''
1. what is pagination - sending data in chunks 
2. pagination logic
3. fastapi integration
'''

from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/news")
def get_news(page: int = 1, limit:int = 5):
    url = "https://news.ycombinator.com/"

    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")

    title = []

    for item in soup.find_all("span", class_ = "titleline"):
        title.append(item.text)

    #pagination logic

    start = (page - 1) * limit
    end = start+limit
    return{
        "page":page,
        "limit": limit,
        "total":len(title),
        "data":title[start:end]
    }