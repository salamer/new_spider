# coding=utf-8
import requests
from bs4 import BeautifulSoup as bs

s = requests.Session()
headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
 'Origin': 'http://www.v2ex.com',
 'Referer': 'http://www.v2ex.com/signin',
 'Host': 'www.v2ex.com',
}
r = s.get('http://www.v2ex.com/signin', headers=headers)
soup = bs(r.content)
once = soup.find('input', {'name': 'once'})['value']

login_data = {'u': '***', 'p': '***', 'once': once, 'next': '/'}

s.post('http://www.v2ex.com/signin', login_data, headers=headers)

f = s.get('http://www.v2ex.com/settings', headers=headers)
print f.content
