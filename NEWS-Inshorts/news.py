#DAILY - NEWS - INSHORTS

from urllib.request import urlopen
from bs4 import BeautifulSoup
import os,urllib.request,getch,sys,time

html=urlopen("https://www.inshorts.com/en/read")
text=html.read()
soup=BeautifulSoup(text,'html.parser')

x=soup.find_all("span",attrs={'itemprop': "headline"})
links=soup.find_all("a",attrs={'style': "color:#44444d!important"})
pretext="https://www.inshorts.com"

link=[]
news=[]
print("\t\t\t\t TOP NEWS HEADLINES [BY: INSHORTS]")
print("\t\t\t\t\t[{0}]\n".format(time.strftime("%d-%m-%Y")))

for i in links:
    link.append(pretext+i.get('href'))

length=len(link)

for i in x:
    news.append(i.get_text())

for i in range(length):
    print("*****  {0}".format(news[i]))
    print("Link : {0}\n".format(link[i]))

getch.getch()
