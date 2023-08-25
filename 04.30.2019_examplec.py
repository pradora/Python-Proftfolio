python3
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = 'https://www.newegg.com/Laptop-Memory/SubCategory/ID-381?Tid=7635'
uClient = uReq(my_url)
webPage_rawHTML = uClient.read()
uClient.close()#hi dad
webPage_soup = soup(webPage_rawHTML, "html.parser")
containers = webPage_soup.findAll('a',{"class":"item-title"})
for container in containers:
	print('Product name: ' +'\n'+ container.text)
