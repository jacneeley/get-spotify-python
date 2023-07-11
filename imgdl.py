import os
import requests
import shutil
import pandas
folder_path = 'C:/Users/Owner/Documents/Python-Scripts/get-spotify-python/top-30-imgs/'
def download_imgs(dataframe , column):
    count = 0
    urls = []
    for i in dataframe[column]:
        count += 1
        urls.append(i)
    for url in urls:
        file_name = url.split('/')[-1]
        with open(os.path.join(folder_path,file_name+".png"),"wb") as handle:
            data = requests.get(url, stream=True)
            if not data.ok:
                print(data)
            for img in data.iter_content(1024):
                if not img:
                    break
                handle.write(img)
                print("downloaded...")
                
            # data.raw_decode_content = True
            # shutil.copyfileobj(data.raw,file)