import requests
import os
from bs4 import BeautifulSoup

URL = os.environ["URL"]
BARKTOKEN = os.environ["BARKTOKEN"]

req = requests.get('%s' % URL)
req.encoding = "utf-8"
html = req.text
soup = BeautifulSoup(html, 'html.parser')
company_item = soup.find('tr',{'data-field':"field_31"})
dd = company_item.text.strip().replace("\n","").replace(" ","")

if dd == '通过情况已通过':
    requests.get('https://api.day.app/%s/自由行申请已通过?icon=https://wx2.sinaimg.cn/mw2000/74b9b5ddly8h2top5l7u9j20rh0yzgwh.jpg' % BARKTOKEN)
else:
    print()

print('运行结束')

#print(dd)
