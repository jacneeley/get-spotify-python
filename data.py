import pandas as pd
from dotenv import load_dotenv
import os

# load_dotenv()
# path = os.getenv("PATH")
path = 'C:/Users/jcn73/Documents/python-scripts/NACC_VIEW_CHARTS_EXPORT_20230501.csv'
df = pd.read_csv(path)

artists = []
albums = []

for i in df['Record']:
    albums.append(i)

for i in df['Artist']:
    artists.append(i.lower())


    
    
    
        


