import io
import requests 
import bs4
url = "https://idv.sinica.edu.tw/andyliu/tc/Perl/ch1.htm#RegularExpressions"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}



web = requests.get(url, headers = headers)


bytesio = io.BytesIO(web.content)
with open(f'pdfFile.html', 'wb') as f:
    f.write(bytesio.getvalue())
