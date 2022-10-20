import requests
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
    requests.get('https://api.day.app/%s/自由行申请已通过' % BARKTOKEN)
else:
    print()



#print(dd)
