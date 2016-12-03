# -*- coding:UTF-8 -*- ＃
import urllib
import re
import os
import time
import sys
from optparse import OptionParser

usage = 'Usage:%prog -b beginning page -l last page -o output picture'
parser = OptionParser(usage)
parser.add_option('-b',dest="begin",help="The start page to download picture")
parser.add_option('-l',dest="last",help="The last page to download picture(optional)")
parser.add_option('-o',dest="path",help="The path to save picture(optional)")
(options,args) = parser.parse_args()

if options.begin is None:
    parser.print_help()
    sys.exit(0)
begin = int(options.begin)
if options.last is None:
    last = int(options.begin)
elif last < begin:
    print "Last page number must smaller than start page"
    sys.exit(0)

if options.path is None:
    path = "picture"
path = options.path
try:
    os.mkdir(path)
except:
    pass


def getHtml(url):
    try:
        page = urllib.urlopen(url)
    except:
        print "Error"
        sys.exit(0)
    html = page.read()
    return html

x=1

for i in range(int(begin),int(last)+1):
    begin_url = "http://www.meitulu.com/item/%s.html"%i
    html = getHtml(begin_url)
    a=re.findall("<center>.+?</center>",html)
    if a== "":
        print "The page %s is not exsit." % begin
        continue
    
    url=re.findall('<a href="(.+?\.html)"',str(a))#页面链接
    if len(url) == 10:
        page_n=int(re.findall('_(\d.+?)',url[9])[0])
        if page_n > 10:
            for x in range(1,page_n-10):
                url.append('http://www.meitulu.com/item/%s_1%s.html'%(i,x))
    time.sleep(1)
    for list_url in url:
        html=getHtml(list_url)
        picture = re.findall('<center><img src=(.+?\.jpg) alt="',html)#图片链接
        for download in picture:
            urllib.urlretrieve(download,'%s/%s.jpg' % (path,x))#下载图片
            x+=1
    
sys.exit(0)