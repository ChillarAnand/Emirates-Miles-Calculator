#! /usr/bin/python

from bs4 import BeautifulSoup
import urllib2

url = "http://www.emirates.com/account/english/miles-calculator/miles-calculator.aspx?org=BOM&dest=JFK&trvc=0&h=7b1dc440b5eecbda143bd8e7b9ef53a27e364b"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
  
print soup
