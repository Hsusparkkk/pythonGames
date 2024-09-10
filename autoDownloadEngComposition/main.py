import requests
import io
import bs4 as bs
import time as t

# set target web url and headers
url = "https://www.ceec.edu.tw/xmdoc/cont?xsmsid=0J071624926253508127&sid=0O089336014967309929"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

# get pdfs in web
web = requests.get(url, headers=headers)
webHtml = bs.BeautifulSoup(web.text, "html.parser")
pdfs = webHtml.select("a.file_ext.file_pdf")

# collect download-file-urls
urls = []
for each in pdfs:
    urls.append(each.get("href"))

# download 
def downloadPdf(path, name, url):
    response = requests.get(url, headers=headers)
    bytesObj = io.BytesIO(response.content) # create a byteIO obj with binary data from url
    with open(f'{path}{name}-origonal.pdf', 'wb') as f:
        f.write(bytesObj.getvalue())

for i in range(len(urls)):
    cur_time = t.localtime()
    file_name = str(cur_time.tm_mon) + "_" + str(cur_time.tm_mday) + "_" + str(i)
    downloadPdf("download/", file_name, urls[i])