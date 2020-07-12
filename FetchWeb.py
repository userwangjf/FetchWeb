
from bs4 import BeautifulSoup
from CrawlerBase import Crawler
import logging
import re
from tomd import Tomd
from urllib import request
import requests
from fetchHtml import fetchHtml

class FetchWeb(Crawler):
    def __init__(self):
        pass

    def GetAllMenu(self,url):
        try:
            soup = BeautifulSoup(super().Request_Net(url).content, "html5lib")
            #menu_tag = soup.find(class_="design")
            menu_tag = soup.find(id="leftcolumn")
            for a in menu_tag.find_all("a"):    
                href = str(a.get('href'))
                print(self.href2url(url,href))

        except Exception as e:
            print(e)

    def GetAllBody(self,url):

        soup = BeautifulSoup(requests.get(url).content,"html5lib")
        
        soup = BeautifulSoup(super().Request_Net(url).content, "html5lib")
        body_class = soup.find_all(class_="article-body")
        body = str(body_class[0])
        print(body.replace('\r\n','--'))

        with open("3.body","w",encoding="utf-8") as f:
            f.write(str(body).replace("\\r","--"))

        with open("3.md","w",encoding="utf-8") as f:
            md = Tomd(body).markdown
            f.write(md)
    
    #转换相对地址的herf为完整的url
    def href2url(self,url,href):
        result = href.find('/')
        if result == -1:
            full = super().Parse_URL(url).get('url_head', 'invalid url_head of key') + href
        else:
            full = super().Parse_URL(url).get('url_domain', 'invalid url_domain of key') + href
        return full
        
if __name__ == "__main__":
    fetchWeb = FetchWeb()
    #fetchWeb.GetAllMenu("https://www.runoob.com/python3/python3-basic-syntax.html")
    fetchWeb.GetAllBody("https://www.runoob.com/python/python-basic-syntax.html")

