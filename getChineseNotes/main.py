import io
import os
from bs4 import BeautifulSoup
import requests
import time

url = "https://www.clearnotebooks.com/zh-TW/notebooks/673824" # Clearnote url required
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}

# request url
req = requests.get(url, headers=header)

# initialize bs4 obj
content = BeautifulSoup(req.content, features="html.parser")

# find target url(download node)
urls = content.select(".pages__page__trimming img")

for each in urls:
    print(f'Name: {each.get("alt")[-4:]}, url: {each.get("src")}')

# download process

def download(ele):
    urlCont = requests.get(ele.get("src")).content
    binIo = io.BytesIO(urlCont)

    with open(f'download/{ele.get("alt")[-3:]}.webp','wb') as f:
        r = f.write(binIo.getvalue())

for each in urls:
    if("ad" not in each.get('alt')):
        download(each)  


dirName = urls[1].get("alt")[:-3]
os.rename("download",dirName)
os.mkdir("download")