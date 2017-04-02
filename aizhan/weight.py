import requests
from bs4 import BeautifulSoup as bs
from optparse import OptionParser
import threading
import Queue
import re

usage = 'Usage: %prog [-f file] or [-w website] (only one argument)'
parser = OptionParser(usage)
parser.add_option('-w',dest='website',help='The website u want query')
parser.add_option('-f',dest='file',help='The file include websites which u want query')

(options,args) = parser.parse_args()

filetxt = options.file
website = options.website
levels = []

if filetxt != None and website != None:
    print "Error"
    parser.print_help()
    exit()
if filetxt == None and website == None:
    parser.print_help()
    exit()

def read(filetxt):
    file = open(filetxt,'r')
    temp = file.readlines()

    websites = Queue.Queue()
    for website in temp:
        websites.put(website.split("\n")[0])
    
    return websites

def getall(websites):
    query = Query()
    global levels
    while not websites.empty():
        website = websites.get()
        level = {'website':website}
        br = query.weight(website)
        level['br'] = br
        levels.append(level)

class Query(object):
    def __init__(self):
        self.target = "http://www.aizhan.com"
        self.cha ="/cha/"
    
    def weight(self,website):
        types = ['baidu_rank','baidu_mBR']
        br = {types[0]:None,types[1]:None}

        r = requests.get(self.target+self.cha+website)
        soup = bs(r.content,'lxml')

        for type in types:
            a = soup.find_all(name='a',attrs={'id':type})
            img = a[0].find_all(name='img')
            br[type] = re.findall('(\d+)',img[0]['src'])[0]

        return br

def main():
    global levels
    query = Query()
    
    if filetxt != None:
        threads = []
        max_threads = 4

        websites = read(filetxt)

        for i in range(max_threads):
            threads.append(threading.Thread(target=getall,args=(websites,)))
        
        for i in threads:
            i.setDaemon(True)
        for i in threads:
            i.start()

        print "Querying..."
        for i in threads:
            i.join(30)
        while True:
            try:
                level = raw_input('>>')
                for i in levels:
                    if i['br']['baidu_rank'] == level or i['br']['baidu_mBR'] == level:
                        print i['website']
                    continue
            except KeyboardInterrupt:
                print "\n"
                exit()
    else:
        query.weight(website)
        print levels

if __name__ == "__main__":
    main()        