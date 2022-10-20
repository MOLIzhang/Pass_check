import requests
from bs4 import BeautifulSoup

req = requests.get('这里填金数据页面')
req.encoding = "utf-8"
html = req.text
soup = BeautifulSoup(html, 'html.parser')
company_item = soup.find('tr',{'data-field':"field_31"})
dd = company_item.text.strip().replace("\n","").replace(" ","")

if dd == '通过情况已通过':
    requests.get('https://api.day.app/这里填barktoken/自由行申请已通过')
else:
    print()



#print(dd)
