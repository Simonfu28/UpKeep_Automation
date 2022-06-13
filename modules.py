import requests
import json


accepted_code = [200, 201, 202, 203, 204, 205, 206]

def auth(user, password):
    r = requests.get("https://api.onupkeep.com/api/v2/auth", data={'email':user, 'password':password})
    print(r.text)
        
    if r.status_code in accepted_code:
        temp = json.loads(r.text)
        temp = temp["result"]
        token = temp["sessionToken"]
        return token
    else:
        temp = "Error: Code " + str(r.status_code)
        return temp
        ## Throw error here
    
def test(token):
    payload = {"id": "O1L94DYjCv"}

    r = requests.get("https://api.onupkeep.com/api/v2/work-orders/", params=payload, headers={"Session-Token": token})
    print(r.status_code, r.text)