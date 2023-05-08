import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
path = os.getenv("PATH")
df = pd.read_csv(path)

artists = []
albums = []

for i in df['Record']:
    artists.append(i)

for i in df['Artist']:
    albums.append(i.lower())

    
    
    
        


