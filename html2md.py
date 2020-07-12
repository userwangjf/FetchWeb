import html2text as ht  # pip install html2text
import os 
text_maker = ht.HTML2Text()
#text_maker.ignore_links = True
text_maker.bypass_tables = False
path ="./2.html"
htmlfile = open(path,'r',encoding='UTF-8')
htmlpage = htmlfile.read()
text = text_maker.handle(htmlpage)
md = text.split('#')  # split post content
open("2.md","w").write(md[1])  # write file as a md file