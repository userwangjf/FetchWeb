

from pyquery import PyQuery as pq
import requests

with open("3.html",encoding="utf-8") as f:
    html = f.read()
doc = pq(html)
#print(doc('h1'))
html = requests.get("https://www.runoob.com/python/python-basic-syntax.html").content.decode("utf-8")
with open("3_wr.html","w",encoding="utf-8") as f:
    f.write(html)



