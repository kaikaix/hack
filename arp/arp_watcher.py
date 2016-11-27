import sys
from optparse import OptionParser
from scapy.all import sniff,ARP,get_if_hwaddr
from signal import signal,SIGINT

ip_mac={}
test = True

usage = 'Usage:%prog -i interface -b bssid'
parser = OptionParser(usage)
parser.add_option('-i',dest="interface",help='the network card')
parser.add_option('-b',dest='bssid',help='the gateway\'s MAC')
(options,args)=parser.parse_args()

if len(sys.argv) < 3:
    parser.print_help()
    sys.exit(0)
default_mac = options.bssid
iface=options.interface
my_mac = get_if_hwaddr(iface)

def watch_arp(pkt):
    global default_mac
    global my_mac

    if pkt[ARP].op == 2:
        if default_mac==pkt[ARP].hwdst:
            print "MAC:"+default_mac+"  IP:"+pkt[ARP].pdst
        elif my_mac != pkt[ARP].hwsrc:
            print "Maybe this computer is attacked by %s,and ip is %s"%(pkt[ARP].hwsrc,pkt[ARP].psrc)

sniff(prn=watch_arp,filter="arp",iface=iface,store=0)
