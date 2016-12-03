# -*- coding:UTF-8 -*- ＃
import urllib
import re
import os
import time
import sys

def getHtml(url):
    try:
        page = urllib.urlopen(url)
    except:
        print "Error"
        sys.exit(0)
    html = page.read()
    return html

x=1
begin=raw_input("Which page you want to download in the beginning:")
last=raw_input("At the end:")
if begin>last:
    print "begin number must smaller than last page number"
    sys.exit(0)

for i in range(int(begin),int(last)):
    begin_url = "http://www.meitulu.com/item/%s.html"%i
    html = getHtml(begin_url)
    a=re.findall("<center>.+?</center>",html)
    if a=="":
        print "The page begin is not exsit."
    url=re.findall('<a href="(.+?\.html)"',str(a))
    time.sleep(3)
    for list_url in url:
        html=getHtml(list_url)
        picture = re.findall('<center><img src=(.+?\.jpg) alt="',html)
        for download in picture:
            urllib.urlretrieve(download,'/root/picture/%s.jpg' % x)
            x+=1
    
sys.exit(0)