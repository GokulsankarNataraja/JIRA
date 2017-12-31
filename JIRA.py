# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 09:51:30 2017

@author: Gokul
"""

from bs4 import BeautifulSoup as soup

from urllib.request import urlopen as Ureq

def star():
    file = open(r'C:\Users\Gokul\Desktop\Url.txt')
    filename = "pro1.csv"
    f = open(filename,"w")
    for line in file:
        par(line,f)
    f.close()

def par(my_url,f):
    uClient = Ureq(my_url)
    page_html = uClient.read()

    uClient.close()

    page_soup = soup(page_html,"html.parser")

    

    containers = page_soup.findAll("li",{"class":"item"})
    feild_name,feild_value  = {},{}
    for i in range(0,7):
        feild_name[i] = containers[i].strong.text
        feild_value[i] = containers[i].span.text.split()
  
    for i in range(0,6):
        print(feild_name[i])
        #print (feild_value[i])
        f.write(str(feild_name[i]) + ',')
    f.write("\n")
    for i in range(0,6):
        #print(feild_name[i])
        #print (feild_value[i])
        f.write(str(feild_value[i]).replace(","," ") + ',')
    
    
    containers1 = page_soup.findAll("div",{"id":"descriptionmodule"})
    Des_text = containers1[0].text
    print(containers1)
    print(Des_text)
    n_Des_text = Des_text.replace("\n","\\n")
    c_Des_text = n_Des_text.replace(",","@")
    f.write(c_Des_text)
    f.write("\n")
    #print (Des_text)
    
if __name__ == "__main__":
    star()