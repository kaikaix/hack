# -*- coding:UTF-8 -*- #
import re
import urllib
import sys
import os

if len(sys.argv) != 2:
    print "Usage:%s name" % sys.argv[0]
    sys.exit(0)
name = sys.argv[1]

def getHtml(url):
    try:
        page = urllib.urlopen(url)
    except:
        print "Error"
        sys.exit(0)
    html = page.read()
    return html

url="http://www.meitulu.com/t/%s"%name

html = getHtml(url)
error=re.findall('<div class="tishi_t">.+?</div>',html)
if len(error)>0:
    print "The name is not exist"
    sys.exit(0)

url_list = re.findall('<li>\n<a href="(.+?)" target=',html)
sequence_n=re.findall("\d{1,4}",str(url_list))
for i in sequence_n:
    try:
        os.system('python crawlbypage.py -b %s -o %s'%(i,i))
        print i
    except:
        continue
