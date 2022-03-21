import re
import requests 

data = requests.get("https://en.wikipedia.org/wiki/IP_address").text
p = r"[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+"

for each in re.findall(p,data):
   #print(p)
   print(each)