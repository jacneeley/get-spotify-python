import os
import re
import requests

parent_dir = os.path.dirname(__file__).replace("\\","/")
directory = '/top-30-imgs/'
folder_path = parent_dir + directory

def download_imgs(df):
    if os.path.exists(folder_path) == False:
        os.mkdir(folder_path)
        print("Directory '% s' created" % directory)
    else: 
        print("'% s' exists" % directory)
    albums = []
    urls = []
    for a,u in zip(df['Album'],df['Album Picture Url']):
        albums.append(a)
        urls.append(u)
    for album , url in zip(albums,urls):
        file_name = re.sub(r'[^\w_. -]', '_', album)
        with open(os.path.join(folder_path,file_name + ".png"),"wb") as handle:
            data = requests.get(url, stream=True)
            if not data.ok:
                print(data)
            for img in data.iter_content(1024):
                if not img:
                    break
                handle.write(img)
                print("downloaded...")