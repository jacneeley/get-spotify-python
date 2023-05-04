from dotenv import load_dotenv
import os
import base64
from requests import post,get
import json

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


##request access token
def get_token():
    auth_string = client_id+ ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes),"utf-8")

    url="https://accounts.spotify.com/api/token"
    headers={
        "Authorization" : "Basic " + auth_base64,
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    data={"grant_type": "client_credentials"}
    result = post(url,headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return{"Authorization": "Bearer " + token}

token = get_token()

##send request to web api
def album_search(token,album_name,artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={album_name,artist_name}&type=album,artist&limit=1&market=ES"

    q_url = url + query
    result = get(q_url,headers=headers)
    json_result = json.loads(result.content)["albums"]["items"]
    if len(json_result) == 0:
        print("No albums found...")
        return None
    return json_result[0]["id"]

album=album_search(token,"Precious Metal","Charlie")

def album_search(token, album_id):
    url = f"https://api.spotify.com/v1/albums/{album_id}?album_type=album,compilation&limit=1&market=US"
    headers = get_auth_header(token)
    result = get(url,headers=headers)
    json_result = json.loads(result.content)
    return "Album: "+str(json_result['name']) + " Artist: " + str(json_result['artists'][0]['name']) + " Album Picture Url: "+str(json_result['images'][1]['url'])

album_data = album_search(token,album)