#! /usr/lib/python2.7
import random
import sys
import os

#Scrapper

from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards'

filename = "products.csv"
f = open(filename, "w")

headers = "brand, product_name, price, shipping\n"

f.write(headers)

#Open a connection to the web server URL
uClient = uReq(my_url)

#User client.read to pass the html content to a variable
page_html = uClient.read()

#Close the connection
uClient.close()

#HTML Parsing using Beautiful Soup to Parse the HTML
#We use the soup funtion to parse the html, passing in the variable 
#containting the HTML and we have to tell Beautiful Soup what kind of parser to user to decode it
#The data type is of "soup" type
page_soup = soup(page_html, "html.parser")

#Grab a list of graphics cards, they are in div tags with a class of item-container
#This is how we get them out with bs4
containers = page_soup.findAll("div", {"class" : {"item-container"}})

#The retuned value is 12
len(containers)
containers[0]

contain = containers[0]
container = containers[0]

for container in containers:
    brand = container.div.div.a.img["title"]
    title_container = container.findAll("a", {"class" : "item-title"})
    product_name = title_container[0].text
    shipping_container = container.findAll("li", {"class" : "price-ship"})
    shipping = shipping_container[0].text.strip()
    pricing_container = container.findAll("li", {"class" : "price-current"})
    pricing = pricing_container[0].text.replace("\r","").replace("|","").replace("-","")
    
    #first position of example (17 offers)-
    temp_pricing = pricing_container[0].text.replace("\r","").replace("|","").replace("\n","").replace("-","")[0:7]
    
    
    print("brand: " + brand)
    print("product_name: " + product_name)
    print("shipping: " + shipping)
    print("pricing: " + temp_pricing)
    
    f.write(brand + ", " + product_name.replace(",","|") + ", " + temp_pricing + ", " + shipping + "\n")

f.close 
