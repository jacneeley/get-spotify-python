from dotenv import load_dotenv
from requests import post,get
import json
import pandas as pd
from auth import get_token,get_auth_header
from data import albums, artists

token = get_token()

##send request to web api
def spotify_search(token,album_name,artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={album_name,artist_name}&type=album,artist&market=ES&limit=1"

    q_url = url + query
    result = get(q_url,headers=headers)
    json_result = json.loads(result.content)['albums']['items']
    if len(json_result) == 0:
        print("No album(s) found...")
        return None
    return json_result[0]["id"]

def album_search(token, album_id):
    url = f"https://api.spotify.com/v1/albums/{album_id}?album_type=album,compilation&limit=1&market=US"
    headers = get_auth_header(token)
    result = get(url,headers=headers)
    json_result = json.loads(result.content)
    return {"Album":str(json_result['name']),
            "Artist":str(json_result['artists'][0]['name']),
            "Album Picture Url":str(json_result['images'][1]['url'])}


album_data = []
print("Creating CSV...")
for album,artist in zip(albums, artists):
    album=spotify_search(token,album,artist)
    if album == None:
        album_data.append({"Album":"No Album Found","Artist":"None","Album Picture Url":"None"})
        print("No Album Found...")
    else:
        album_data.append(album_search(token,album))
        print(str(album_search(token,album)) + ' added...')
    top_albums = pd.DataFrame(album_data)

#change column positions.
new_cols = ['Artist','Album','Album Picture Url']
top_albums = top_albums.reindex(columns=new_cols)

#export 
if len(top_albums) > 5:
    export_csv = top_albums.to_csv(r'top-albums.csv',index=None,header = True)
else:
    export_csv = top_albums.to_csv(r'top-adds.csv',index=None,header = True)
print("Done.")  
