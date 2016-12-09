import re
import sys
import socket

if len(sys.argv) != 2:
    print sys.argv[0] + " start_ip-stop_ip"
    sys.exit(0)

def get_ips(start_ip,last_ip):
    byte=[0,0,0,0]
    a=0
    for i in range(0,4):
        byte[i] = last_ip[i]-start_ip[i]
        if byte[i] > 0:
            a=0
        if byte[i] < 0 and a == 1:
            print "start_ip must smaller than stop_ip"
            sys.exit(0)
    
    a=1
    times=0
    for i in range(3,-1,-1):
        times+=byte[i]*a
        a*=256

    x = 0
    tmp=start_ip
    ips=[]
    tmps = [0,0,0,0]
    while x<=times:
        for i in range(0,4):
            tmps[i] = str(tmp[i])
        ips.append('.'.join(tmps))

        tmp[3]+=1
        for i in range(3,0,-1):
            if tmp[0]==256:
                print "exit"
                times = 0
            elif tmp[i]==256:
                tmp[i]=0
                tmp[i-1]+=1
        
        x+=1
    
    return ips,times

def dns_reverse_lookup(start_ip,stop_ip):
    ips,times = get_ips(start_ip,stop_ip)

    i=0
    while i<times+1:
        try:
            print ips[i]+": " +str(socket.gethostbyaddr(ips[i])[0])
        except (socket.herror,socket.error):
            pass
        
        i+=1

def check_ip(ipaddr):
    if len(ipaddr) != 4:
        print "It is an error ip"
        print "It is a legal IP: 192.168.0.1"
        sys.exit(0)
    
    for i in range(4):
        addr = [0,0,0,0]
        try:
            addr[i]=int(ipaddr[i])
        except:
            print "It is an error ip"
            print "IP address must be a number"
            sys.exit(0)
        
        if addr[i] > 255 or addr[i] < 0:
            print "It is an error ip"
            print "Can't bigger than 255 or smaller than 0"
            sys.exit(0)

start_ip,stop_ip = sys.argv[1].split('-')

stop_ip=stop_ip.split('.')
start_ip=start_ip.split('.')

check_ip(start_ip)
check_ip(stop_ip)

for i in range(0,4):
    stop_ip[i]=int(stop_ip[i])
    start_ip[i] = int(start_ip[i])

dns_reverse_lookup(start_ip,stop_ip)