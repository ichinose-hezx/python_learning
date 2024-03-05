import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

total = 0
url = input('Enter location:')
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_42.json"
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
info = json.loads(data.decode())

for item in info["comments"]:
    total = total + int(item["count"])

print("Count:",len(info["comments"]))
print("Sum:",total)