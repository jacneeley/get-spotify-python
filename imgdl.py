import os
import requests
parent_dir = 'C:/Users/neele/python_projects/get-spotify-python/'
directory = 'top-30-imgs/'
folder_path = os.path.join(parent_dir, directory)
def download_imgs(dataframe , column):
    if os.path.exists(folder_path) == False:
        os.mkdir(folder_path)
        print("Directory '% s' created" % directory)
    else: 
        print("'% s' exists" % directory)
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