# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



url = input('Enter - ')
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
i = 0

count = input('Enter count: ')
position = input('Enter position: ')
count = int(count)
position = int(position)

while i < count :
    i = i + 1
    print("Retrieving:",url)        
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    tag = tags[position - 1]
    #print(tag.get('href', None))
    url = tag.get('href', None)

print("Retrieving:",url)
print(re.findall("by_(\S+?)\.html",url))

