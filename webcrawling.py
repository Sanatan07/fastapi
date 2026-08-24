#web crawling using fastapi

'''
1. what is external api
2. install requests
3. basic api call
4. single data fetch
5. fastapi integration
'''

#EVERY WEBSITE DOES NOT ALLOW WEB CRAWLING
#WEB CRAWLING IS ILLEGLE

'''
Python example
import requests
from bs4 import BeautifulSoup

url = "https://source.android.com/docs/security/bulletin"

response = requests.get(url)

# Pass the response HTML content and use 'html.parser'
soup = BeautifulSoup(response.text, "html.parser")

if soup.title:
    print(soup.title.text)

'''


from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/news")
def get_news():
    url = "https://medium.com/me/following-feed/writers/fd73615058e1" 
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")

    title = []
    for item in soup.find_all("a",class_="as x au ci aw ab ax i ac ae af ag ah ai aj"):
        title.appeand(item.text)

    return{
        "news":title
    }
