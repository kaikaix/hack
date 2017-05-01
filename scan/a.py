import requests
import sys
import os
import threading
import Queue
from optparse import OptionParser

usage = "Usage: %prog [-p path] [-w website]"
parser = OptionParser(usage)
parser.add_option('-p',dest='path',help='the wordlist\'s path')
parser.add_option('-p',dest='website',help='website')
(option,args) = parser.parse_args()

path = option.path
website = option.website

if path == None or website==None:
    parser.print_help()
    sys.exit()

if not os.path.exists(path):
    print "Doesn't exist"
    sys.exit()
wordlists = Queue.Queue()
def readin(path):
    global wordlists
    try:
        f = open(path,'r')
        lists = f.readlines()
        for i in lists:
            wordlists.put(i.strip('\n'))
    except:
        print "Error"
        sys.exit()

def scan(wordlists):
    while not wordlists.empty():
        link = wordlists.get()
        r=requests.get(website+link,headers={'User-agent':'Mozilla/5.0 (x11; Linux x86_64; rv:19.0) Gecko/20100101 Firefox/19.0'})
        if r.status_code != 404:
            print "["+str(r.status_code)+"]==>"+website+link


def main():
    global path,wordlists
    readin(path)
    threads = []
    max_thread = 5

    for i in range(max_thread):
        threads.append(threading.Thread(target=scan,args=(wordlists,)))
    
    for i in threads:
        i.setDaemon(True)

    for i in threads:
        i.start()

    for i in threads:
        i.join(20)