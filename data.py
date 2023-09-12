import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
path = os.getenv("FILE_PATH")

if(path == None):
    print("No path provided in .env")
    path = str(input("please provide a file path: "))
    path.replace("\\","/")

df = pd.read_csv(path)
df.rename(columns={'Record' : 'Album'}, inplace=True)
artists = []
albums = []

for i in df['Album']:
    albums.append(i.replace('"',"").replace("[","").replace("]","").lower())

for i in df['Artist']:
    artists.append(i)
