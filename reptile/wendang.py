import requests
from bs4 import BeautifulSoup



result = requests.get('https://wenku.baidu.com/view/865b86340540be1e650e52ea551810a6f524c8c0.html')

soup = BeautifulSoup(result.text, 'html.parser')

print(soup.find_all(attrs={"class": "reader-container"})