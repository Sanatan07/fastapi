from fastapi.testclient import TestClient
from apitest import app

client = TestClient(app)


#test home api

def test_home():
    response = client.get("/")
    #status code check
    assert response.status_code == 200
    #response data check
    assert response.json() == {"message":"Hello Mohit"}


#test add api
def test_add():
    response = client.get("/add?a=5&b=4")
     #status code check
    assert response.status_code == 200
        #response data check
    assert response.json() == {"result":9}