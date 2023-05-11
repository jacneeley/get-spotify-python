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

artists = []
albums = []

for i in df['Record']:
    albums.append(i)

for i in df['Artist']:
    artists.append(i.lower())


    
    
    
        


