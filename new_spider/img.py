import requests
from pyquery import PyQuery as pq


html=pq(url="http://movie.douban.com/celebrity/1018667/photo/651781439/")

img=html(".mainphoto img")

src=img.attr("src")

pic=requests.get(src)
with open("/home/aljun/pythonlearning/spider/requests/masami.jpg",'w') as f:
	f.write(pic.content)

