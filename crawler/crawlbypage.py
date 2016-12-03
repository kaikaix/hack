# -*- coding:UTF-8 -*- ＃
import urllib
import re
import os
import time
import sys
from signal import signal,SIGALRM,alarm
from optparse import OptionParser

y=1
url_list = []
got_timeout = True
lost_url = []

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

path = options.path
if options.path is None:
    path = "picture"

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

def cbk(a, b, c):
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print '%.2f%%' % per

for i in range(int(begin),int(last)+1):
    begin_url = "http://www.meitulu.com/item/%s.html"%i
    html = getHtml(begin_url)
    a=re.findall("<center>.+?</center>",html)
    if a== "":
        print "The page %s is not exsit." % begin
        continue
    first_h = re.findall('<a class="a1" href="(.*?)">.+?</a>',html)#第一个链接
    url=re.findall('<a href="(.+?\.html)"',str(a))#页面链接
    print url
    url_list.append(first_h[0])
    print url_list
    length = len(url)-1
    print length
    if length >= 8:
        page_n = int(re.findall('_(\d.+?)',url[length])[0])
    else:
        page_n = int(re.findall('_(\d.*?)\.{0}',url[length])[0])

    for x in range(2,page_n+1):
        url_list.append('http://www.meitulu.com/item/%s_%s.html'%(i,x))
    for url in url_list:
        html=getHtml(url)
        picture = re.findall('<center><img src=(.+?\.jpg) alt="',html)#图片链接
        for download in picture:
            print "download:%s"%download
            urllib.urlretrieve(url=download,filename='%s/%s.jpg' % (path,y))#下载图片
            y+=1
sys.exit(0)
