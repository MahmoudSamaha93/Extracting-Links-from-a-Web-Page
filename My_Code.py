# Importing some libraries, and BeautifulSoup.
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Taking URL from User.
while True:
    _url = input('Enter URL [Starting with http/s]:--->     ')
    url_str = str(_url)
    try:
        if url_str.startswith('http'):
            url = url_str
            break
    except:
        print('*********** Invalid URl ***********')
        continue
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
