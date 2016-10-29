# -*- coding: UTF-8 -*-
import sys
import urllib2
import json
from optparse import OptionParser

usage = 'Usage:%prog -a ak -i ip'
parser = OptionParser(usage)
parser.add_option('-a',dest='ak',help='To register in baidu map')
parser.add_option('-i',dest='ip',help='On your own')
(options,args)=parser.parse_args()
ip = options.ip
ak = options.ak

if ip is None or ak is None:
    parser.print_help()
    sys.exit(0)

def get_ip_information(ip,ak):
    url='http://api.map.baidu.com/highacciploc/v1?qcip=%s&qterm=pc&ak=%s&coord=bd09ll&extensions=3'%(ip,ak)
    try:
        request = urllib2.Request(url)
        page = urllib2.urlopen(request, timeout=10)
    except:
        print 'can\'t open url:%s'%url
        sys.exit(0)
    data_json = page.read()
    data_dic = json.loads(data_json)
    if(data_dic.has_key("content")):
        content=data_dic["content"]
        address_component=content["address_component"]
        formatted_address=content["formatted_address"]
        print "该IP地址的具体位置为："
        print address_component["country"]
        print formatted_address
    else:
        print 'IP地址定位失败！'


if __name__ == '__main__':
    get_ip_information(ip,ak)
