import time
import io 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
import requests as rqst
options = Options()
driver = webdriver.Chrome(options=options)
driver.minimize_window()
driver.get("https://www.ceec.edu.tw/xmfile?xsmsid=0J052424829869345634")
driver.find_element(By.LINK_TEXT, "數學").click()
# print(driver.page_source)
# print("=======")
time.sleep(2)
webBs = bs(driver.page_source, "html.parser")
pdfs = webBs.select("a.file_ext.file_pdf") # css selector
# print(driver.page_source)

# get urls needed
urls=[]
for each in pdfs:
    if each.text == "試題內容" or each.text == "選擇(填)題答案":
        urls.append("https://www.ceec.edu.tw/"+each.get("href"))

print(urls)

# download pdfs
sendHeaders ={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8"
}


def dlPdf(path, name, url):
    response = rqst.get(url, sendHeaders)
    bytes = io.BytesIO(response.content)
    if "%88" in url:
        with open(path +str(name)+ "answer.PDF",'wb') as f:
            f.write(bytes.getvalue())
        print(str(name) + "answer pdf downloaded.")
    else:
        with open(path + str(name) + "paper.PDF",'wb') as f:
            f.write(bytes.getvalue())
        print(str(name) + "paper pdf downloaded.")

# main
for url in range(len(urls)):
    dlPdf("downloaded/", url, urls[url])
driver.close()