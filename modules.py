import requests
import json


accepted_code = [200, 201, 202, 203, 204, 205, 206]

def auth(user, password):
    r = requests.post("https://api.onupkeep.com/api/v2/auth", data={'email':user, 'password':password})
        
    if r.status_code in accepted_code:
        temp = json.loads(r.text)
        temp = temp["result"]
        token = temp["sessionToken"]
        return token
    else:
        temp = "Error: Code " + r.status_code
        return temp
