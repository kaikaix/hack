import urllib2
import threading
import Queue
import re
import sys
import time

class Butian(object):
    def __init__(self,list_queue,error_urls):
        self.link_queue = list_queue
        self.error_urls = error_urls
        pass

    def download(self,url,retries=2):
        try:
            e=None
            res = urllib2.urlopen(url)
            return res,e
        except urllib2.URLError as e:
            res = None
            if retries > 0:
                if hasattr(e,'code') and 500 <= e.code < 600:
                    retries -= 1
                    return self.download(url)
        return res,e

    def crawl_link(self,file,number):
        print 'start %d'%number
        while not self.link_queue.empty():
            url = self.link_queue.get()
            res = None
            while res == None:
                res,e = self.download(url)
            sys.stdout.write("Thread %d Download:%s\n"%(number,url))

            if res == None:
                print e.code
                break
            else:
                try:
                    html = res.read()
                except:
                    self.error_urls.put(url)
                    break

                result = re.findall('<td  align="left" style="padding-left:20px;">(.+?)</td>',html)
                for i in result:
                    file.write(i+'\n')
        return 0
    
    def retry_crawl(self,file):
        print "retry again\n"
        while not self.error_urls.empty():
            url = self.error_urls.get()
            res,e = self.download(url)
            print "Downloading %s\n"%url
            if res == None:
                print e.code
            else:
                try:
                    html = res.read()
                except:
                    print "Error:%s\n"%url
                    with open('error.txt','w') as e_file:
                        e_file.write(url+'\n')
                    break
                
                result = re.findall('<td  align="left" style="padding-left:20px;">(.+?)</td>',html)
                for i in result:
                    file.write(i+'\n')
        
        return 0

def main():
    threads = []
    links = Queue.Queue()
    cache_links = Queue.Queue()
    error_urls = Queue.Queue()
    max_threads = 21
    butian = Butian(links,error_urls)
    file = open('host1.txt','w')

    for i in range(1,136):
        links.put('http://butian.360.cn/company/lists/page/%d'%i)

    for i in range(1,max_threads):
        threads.append(
        threading.Thread(target=butian.crawl_link,args=(file,i))
        )

    for i in threads:
        i.setDaemon(True)
    
    for i in threads:
        i.start()
    
    for i in threads:
        i.join()
    
    butian.retry_crawl(file)
    return 0

main()