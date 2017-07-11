#! /usr/bin python
# -*- coding:utf-8 -*-


from bs4 import BeautifulSoup
import requests


url=input("lütfen url giriniz  örn: www.python.tc : ")
req=requests.get("http://"+url)
veri=req.text
soup=BeautifulSoup(veri,'html.parser')
dosya=open("links.txt","w")
for link in soup.find_all('a',href=True):
     dosya.write(link['href'])
     dosya.write('\n')

dosya.close()
print("linkler links.txt dosyasına aktarıldı")