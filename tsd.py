import re
url = "http://py4e-data.dr-chuck.net/known_by_Cohen.html"
print(re.findall("_(\S+?)\.html",url))